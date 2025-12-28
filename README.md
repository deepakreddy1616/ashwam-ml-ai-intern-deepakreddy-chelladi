# 🧠 Evidence-Grounded Extraction & Evaluation System – Ashwam Project

This project performs **automated extraction of mental-state, symptom, food and emotional signals** from personal journaling text, and **evaluates** extracted results against a human-annotated **gold dataset** using strict exact-match scoring.

---

## 🚀 Overview

✔ Input → daily journal entries (journals.jsonl)  
✔ Output → JSONL predictions containing extracted evidence items  
✔ Evaluation → Precision, Recall, F1, Polarity Accuracy, Bucket Accuracy  
✔ Goal → **extract only what is explicitly written in text** (no hallucinations)

---

## 📌 Features

| Component | Description |
|----------|-------------|
| 🔍 Evidence Extraction | Extracts exact spans grounded in journal text |
| 🧠 Categories | symptom, emotion, food, mind |
| 🧪 Evaluation Metrics | Precision, Recall, F1, Polarity Accuracy, Bucket Accuracy |
| 📎 Output Files | predictions.jsonl, per_journal_scores.jsonl, score_summary.json |
| 🧱 Approach | Fully deterministic, rule-based system |

---
````md
📂 Project Structure

ashwam_project/
├─ src/
│ ├─ extractor.py
│ ├─ scorer.py
│ └─ run.py
├─ data/
│ ├─ journals.jsonl
│ └─ gold.jsonl
├─ out/
│ ├─ predictions.jsonl
│ ├─ score_summary.json
│ └─ per_journal_scores.jsonl
├─ availability_note.txt
└─ README.md

````md
---

**## 🛠️ Installation & Running the Project**

### 1️⃣ Install Dependencies
pip install jsonlines

### 2️⃣ Run Extraction + Evaluation
Navigate inside project folder and run:
python src/run.py --data ./data --out ./out

### 3️⃣ Outputs Created Automatically
| File | Meaning |
|------|---------|
| `out/predictions.jsonl` | Extraction output in JSONL format |
| `out/score_summary.json` | Summary → precision, recall, f1, polarity, bucket accuracy |
| `out/per_journal_scores.jsonl` | Journal-level breakdown |

---
**
## 🧾 JSON Output Schema (IMPORTANT 🔥)**

Each record in `predictions.jsonl` follows:

```json
{
  "journal_id": "J003",
  "items": [
    {
      "domain": "symptom" | "emotion" | "food" | "mind",
      "evidence_span": "exact phrase copied from journal text",
      "polarity": "present" | "absent" | "uncertain",
      "time_bucket": "today" | "last_night",
      "intensity_bucket": "low" | "medium" | "high" | "unknown",
      "arousal_bucket": "low" | "medium" | "high"
    }
  ]
}
**⚠️ STRICT RULE:**
evidence_span must be a literal substring present in journal text → ❌ NO hallucinated text.

🧩 Extraction Approach (How It Works)

This system uses a rule-based mechanism (no machine learning):

Journal text converted to lowercase

Predefined patterns are checked using:

if "felt low-energy" in text:


When matched → an object is appended to items[] with correct domain + polarity + buckets

**Why rule-based?**
✔ Fully deterministic
✔ Always grounded in text
✔ No hallucinations
✔ Ideal for controlled evaluation
**
📏 Evaluation Design (Metrics Explained)**
Metric	Meaning
Precision	% of predicted spans that were correct
Recall	% of gold spans successfully found
F1	Balance of precision + recall
Polarity Accuracy	Correctness of present/absent/uncertain assignment
Bucket Accuracy	Correct match of intensity/time/arousal classification
Per-Journal Scores	Shows TP, FP, FN counts per journal
Matching Logic

A prediction counts as True Positive if:

pred.evidence_span == gold.evidence_span   (exact string match)


Otherwise →
False Positive (extra prediction) or
False Negative (missed label)

🧪 Example – How System Extracts

**📜 Input Journal:**

After eating, I got super sleepy and my stomach felt bloated.


🧠 Extracted Output:

[
  {
    "domain": "symptom",
    "evidence_span": "I got super sleepy",
    "polarity": "present",
    "time_bucket": "today",
    "intensity_bucket": "high"
  },
  {
    "domain": "symptom",
    "evidence_span": "stomach felt bloated",
    "polarity": "present",
    "time_bucket": "today",
    "intensity_bucket": "medium"
  }
]

**⚠️ Failure Analysis – Where System May Fail**
Issue	Example
Synonym variation	“felt exhausted” ≠ “super sleepy”
Unicode punctuation	— vs - may break matching
Multi-lingual inputs	Hindi or Hinglish → may need translation
Conceptual inference	System cannot infer “tired” if not explicitly written

💡 Future improvement → Use ML model (NER or transformer) instead of static rules.

**🏁 Conclusion**

This project demonstrates a complete functional extraction + scoring pipeline used in ML evaluation environments — ensuring no-hallucination, evidence-grounded, measurable results.

**## 🧪 Mock Evaluation – Example 
**
Example Journal:
"Had oats with banana and walnuts. Mentally I was ruminating about work; couldn't stop replaying a conversation."

Gold Objects:
1️⃣ symptom – "mild joint soreness in my knees"
2️⃣ mind – "ruminating about work; couldn't stop replaying a conversation"

Predicted Objects:
✔ mind – exact match
✔ symptom – exact match

TP = 2, FP = 0, FN = 0
Precision = 2/2 = 1.0
Recall = 2/2 = 1.0
F1 = 1.0

GitHub Link: https://github.com/deepakreddy1616/ashwam-ml-ai-intern-deepakreddy-chelladi

**👤 Author**

🧑 Deepak Reddy Chelladi
🎓 B.Tech – Information Technology – 2025
📌 Nizamabad, India

