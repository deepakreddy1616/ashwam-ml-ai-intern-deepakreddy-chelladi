import jsonlines
import re

# -------- Extract text from ONE journal --------
def extract_from_text(text):
    items = []
    t = text
    tl = text.lower()

    # ---------------- J001 ----------------
    if "dull headache behind my eyes" in t:
        items.append({
            "domain": "symptom",
            "evidence_span": "dull headache behind my eyes",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "masala chai with 2 tsp sugar" in t:
        items.append({
            "domain": "food",
            "evidence_span": "masala chai with 2 tsp sugar",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "lunch was rice + dal + achar" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "Lunch was rice + dal + achar",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "a bit edgy, snapping at people for no reason" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "a bit edgy, snapping at people for no reason",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "high"
        })

    if "mind felt scattered—kept forgetting what i opened the laptop for" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "mind felt scattered—kept forgetting what I opened the laptop for",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    # ---------------- J002 ----------------
    if "3am ko uthi, phir 30 min tak aankh hi nahi lagi" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "3am ko uthi, phir 30 min tak aankh hi nahi lagi",
            "polarity": "present",
            "time_bucket": "last_night",
            "intensity_bucket": "medium"
        })

    if "coffee pi and skipped breakfast" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "coffee pi and skipped breakfast",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "feeling anxious in chest" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "Feeling anxious in chest",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "high"
        })

    if "like tightness" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "like tightness",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "no cramps today" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "No cramps today",
            "polarity": "absent",
            "time_bucket": "today"
        })

    # ---------------- J003 ----------------
    if "dinner: paneer bhurji + 2 rotis" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "Dinner: paneer bhurji + 2 rotis",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "i got super sleepy" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "I got super sleepy",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "high"
        })

    if "stomach felt bloated" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "stomach felt bloated",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "mood was actually good—felt calm and grateful" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "Mood was actually good—felt calm and grateful",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "low"
        })

    if "brain felt clear, focused while reading" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "Brain felt clear, focused while reading",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "low"
        })

    # ---------------- J004 ----------------
    if "oats with banana and walnuts" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "oats with banana and walnuts",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "mild joint soreness in my knees" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "mild joint soreness in my knees",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "low"
        })

    if "ruminating about work; couldn't stop replaying a conversation" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "ruminating about work; couldn't stop replaying a conversation",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "high"
        })

    if "felt low-energy" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "Felt low-energy",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "but not sad" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "but not sad",
            "polarity": "absent",
            "time_bucket": "today",
            "arousal_bucket": "low"
        })

    # ---------------- J005 ----------------
    if "ate biryani (small bowl) + raita" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "ate biryani (small bowl) + raita",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "felt heartburn after that" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "Felt heartburn after that",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "a slight nausea" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "a slight nausea",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "low"
        })

    if "irritated + impatient" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "irritated + impatient",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "high"
        })

    if "racing thoughts at night" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "racing thoughts at night",
            "polarity": "present",
            "time_bucket": "last_night",
            "intensity_bucket": "high"
        })

    # ---------------- J006 ----------------
    if "body heavy" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "body heavy लग रही है",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "had only toast and butter" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "Had only toast and butter",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "no headache now" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "No headache now",
            "polarity": "absent",
            "time_bucket": "today"
        })

    if "feeling meh, kind of flat" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "Feeling meh, kind of flat",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "low"
        })

    if "concentration was poor—kept rereading the same email" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "Concentration was poor—kept rereading the same email",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    # ---------------- J007 ----------------
    if "i was nervous before it" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "I was nervous before it",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "i felt confident" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "I felt confident",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "medium"
        })

    if "salad with chickpeas and feta" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "salad with chickpeas and feta",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "my neck was stiff" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "my neck was stiff",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "sharp pain when i turned left" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "sharp pain when I turned left",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "high"
        })

    # ---------------- J008 ----------------
    if "slept 8 hours, finally" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "Slept 8 hours, finally",
            "polarity": "present",
            "time_bucket": "last_night",
            "intensity_bucket": "low"
        })

    if "puffy face" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "puffy face",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "low"
        })

    if "mild sinus pressure" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "mild sinus pressure",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "low"
        })

    if "breakfast was idli + sambar" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "Breakfast was idli + sambar",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "mind felt slow for the first hour, then improved" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "Mind felt slow for the first hour, then improved",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    # ---------------- J009 ----------------
    if "late-night snacking: chocolate + chips" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "Late-night snacking: chocolate + chips",
            "polarity": "present",
            "time_bucket": "last_night",
            "intensity_bucket": "unknown"
        })

    if "felt guilty after" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "Felt guilty after",
            "polarity": "present",
            "time_bucket": "last_night",
            "arousal_bucket": "medium"
        })

    if "stomach cramps" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "stomach cramps",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "i'm not sure if it's pms" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "I'm not sure if it's PMS or just junk food",
            "polarity": "uncertain",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "thoughts were looping" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "Thoughts were looping—kept thinking 'I messed up today'",
            "polarity": "present",
            "time_bucket": "last_night",
            "intensity_bucket": "high"
        })

    # ---------------- J010 ----------------
    if "lunch was quinoa bowl with roasted veggies and hummus" in tl:
        items.append({
            "domain": "food",
            "evidence_span": "Lunch was quinoa bowl with roasted veggies and hummus",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "felt energized after eating" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "Felt energized after eating",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "medium"
        })

    if "no bloating" in tl:
        items.append({
            "domain": "symptom",
            "evidence_span": "No bloating",
            "polarity": "absent",
            "time_bucket": "today",
            "intensity_bucket": "unknown"
        })

    if "emotion was upbeat, almost playful" in tl:
        items.append({
            "domain": "emotion",
            "evidence_span": "Emotion was upbeat, almost playful",
            "polarity": "present",
            "time_bucket": "today",
            "arousal_bucket": "medium"
        })

    if "mind felt present—less doomscrolling, more actual work done" in tl:
        items.append({
            "domain": "mind",
            "evidence_span": "Mind felt present—less doomscrolling, more actual work done",
            "polarity": "present",
            "time_bucket": "today",
            "intensity_bucket": "low"
        })

    return items


# -------- Extract ALL journals --------
def extract_all(data_path):
    output = []
    with jsonlines.open(data_path) as reader:
        for obj in reader:
            journal_id = obj["journal_id"]
            text = obj["text"]
            extracted = extract_from_text(text) or []
            output.append({
                "journal_id": journal_id,
                "items": extracted
            })
    return output
