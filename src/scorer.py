import jsonlines

def load_gold(path):
    gold_map = {}
    with jsonlines.open(path) as reader:
        for obj in reader:
            gold_map[obj["journal_id"]] = obj["items"]
    return gold_map


def score(pred, gold):
    tp = fp = fn = 0
    pol_correct = pol_total = 0
    bucket_correct = bucket_total = 0
    coverage_count = coverage_total = 0

    per_journal = {}

    for journal_id, pred_items in pred.items():
        gold_items = gold.get(journal_id, [])

        # lists for checking evidence spans
        gold_texts = [i["evidence_span"] for i in gold_items]
        pred_texts = [i["evidence_span"] for i in pred_items]

        # ---- OBJECT-LEVEL P/R/F1 ----
        for span in pred_texts:
            if span in gold_texts:
                tp += 1
            else:
                fp += 1

        for span in gold_texts:
            if span not in pred_texts:
                fn += 1

        # ---- Polarity accuracy ----
        for g in gold_items:
            for p in pred_items:
                if p["evidence_span"] == g["evidence_span"]:
                    pol_total += 1
                    if "polarity" in p and p["polarity"] == g["polarity"]:
                        pol_correct += 1

        # ---- Bucket accuracy (time, intensity, arousal) ----
        for g in gold_items:
            for p in pred_items:
                if p["evidence_span"] == g["evidence_span"]:
                    # time bucket
                    if "time_bucket" in p and "time_bucket" in g:
                        bucket_total += 1
                        if p["time_bucket"] == g["time_bucket"]:
                            bucket_correct += 1
                    # intensity / arousal (optional)
                    if "intensity_bucket" in p and "intensity_bucket" in g:
                        bucket_total += 1
                        if p["intensity_bucket"] == g["intensity_bucket"]:
                            bucket_correct += 1

        # ---- Evidence coverage ----
        text = ""  # we do not have full journal text passed here
        # coverage_count += number_of_predicted_spans fully inside text

        per_journal[journal_id] = {
            "tp": tp, "fp": fp, "fn": fn
        }

    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    polarity_acc = pol_correct / pol_total if pol_total else 0
    bucket_acc = bucket_correct / bucket_total if bucket_total else 0

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "polarity_accuracy": polarity_acc,
        "bucket_accuracy": bucket_acc,
        "per_journal": per_journal
    }
