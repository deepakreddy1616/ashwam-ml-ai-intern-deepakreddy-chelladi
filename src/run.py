import argparse
import json
import jsonlines
import os
from extractor import extract_all
from scorer import load_gold, score

def main(data_path, out_folder):
    print("Running extraction...")

    # Ensure output folder exists
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    # Run extraction
    predictions = extract_all(f"{data_path}/journals.jsonl")

    # ---------- SAVE PREDICTIONS ----------
    pred_file = f"{out_folder}/predictions.jsonl"
    with jsonlines.open(pred_file, "w") as writer:
        for item in predictions:
            writer.write(item)
    print(f"Predictions file written to: {pred_file}")

    print("Loading gold data...")
    gold = load_gold(f"{data_path}/gold.jsonl")

    # Convert predictions list → dict
    pred_map = {obj["journal_id"]: obj["items"] for obj in predictions}

    print("Scoring...")
    results = score(pred_map, gold)

    # ---------- SAVE SCORE SUMMARY ----------
    score_file = f"{out_folder}/score_summary.json"
    with open(score_file, "w") as f:
        json.dump(results, f, indent=2)

    # ---------- SAVE PER-JOURNAL SCORES ----------
    per_journal_file = f"{out_folder}/per_journal_scores.jsonl"
    with jsonlines.open(per_journal_file, "w") as writer:
        for jid, stats in results["per_journal"].items():
            writer.write({
                "journal_id": jid,
                **stats
            })

    print("\nDONE! 🎉")
    print("Score written to:", score_file)
    print("Per journal scores written to:", per_journal_file)
    print("Final Results Summary:", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="./data")
    parser.add_argument("--out", default="./out")
    args = parser.parse_args()

    main(args.data, args.out)

