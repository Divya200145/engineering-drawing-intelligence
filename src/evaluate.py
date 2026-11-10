import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

def normalize(value):
    return value.strip().upper()

def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        if not {"drawing_id","tag"}.issubset(row):
            raise ValueError("Required CSV columns: drawing_id, tag")
    return rows

def score(truth, predictions):
    t = Counter((normalize(r["drawing_id"]), normalize(r["tag"])) for r in truth)
    p = Counter((normalize(r["drawing_id"]), normalize(r["tag"])) for r in predictions)
    tp = sum(min(t[k], p[k]) for k in t.keys() | p.keys())
    fp = sum(p.values()) - tp
    fn = sum(t.values()) - tp
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "true_positives": tp, "false_positives": fp, "false_negatives": fn,
        "ground_truth_count": sum(t.values()), "prediction_count": sum(p.values()),
        "precision": precision, "recall": recall, "f1": f1,
        "matching": "one-to-one drawing_id and normalized exact tag; duplicates retained"
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--truth", required=True)
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = score(load_csv(args.truth), load_csv(args.predictions))
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
