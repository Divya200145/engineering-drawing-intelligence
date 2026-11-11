# Evaluation Methodology and Reproducibility

## 1. Scope

This project evaluates a baseline OCR pipeline for extracting identifier-shaped text from engineering drawing images.

The pipeline uses Tesseract OCR, image preprocessing, and regular-expression-based identifier extraction.

It does not interpret P&ID connectivity, verify engineering semantics, or distinguish every identifier from a true equipment tag.

## 2. Demonstration Evaluation

The original demonstration uses a synthetic image containing two human-specified text labels.

Files:

- `data/demo/images/demo_001.png`
- `data/demo/labels/ground_truth.csv`

The demonstration evaluation produced:

| Metric | Result |
|---|---:|
| Ground-truth labels | 2 |
| Predictions | 2 |
| True positives | 2 |
| False positives | 0 |
| False negatives | 0 |
| Precision | 100% |
| Recall | 100% |
| F1 | 100% |

These results are a functional smoke test, not evidence of performance on real engineering drawings.

## 3. Exploratory Public P&ID Benchmark

### Dataset

The benchmark uses one synthetic P&ID drawing sourced from PID2Graph, Zenodo record 14803338.

Files:

- `data/public/images/0.png`
- `data/public/labels/0.graphml`
- `data/public/labels/manual_review_0.csv`

The GraphML contains component and connectivity annotations, not verified OCR text transcriptions.

A project reviewer manually recorded 84 identifier occurrences from the drawing.

### Identifier eligibility

The benchmark includes identifiers matching:

`[A-Z]{1,4}-[0-9]{2,5}[A-Z]?`

Of the 84 annotations:

- 79 meet the identifier pattern.
- Five two-hyphen ERV identifiers are excluded.

The eligible ground-truth file is:

`data/public/labels/eligible_truth_0.csv`

These annotations have not been independently reviewed by a domain expert and may not be exhaustive.

## 4. Evaluation Procedure

The evaluator normalizes drawing IDs and identifier strings by trimming whitespace and converting text to uppercase.

Predictions are matched against ground-truth annotations using exact `(drawing_id, tag)` pairs.

Repeated identifiers are counted as separate occurrences. Each prediction can match at most one corresponding ground-truth occurrence.

The evaluation does not compare bounding boxes or verify that a prediction came from the correct location in the drawing.

Metrics are calculated as follows:

- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 = 2 × Precision × Recall / (Precision + Recall)

When a denominator is zero, the implementation reports zero.

## 5. Reproduce the Public Benchmark

From the repository root, run:

`python src/evaluate.py --truth data/public/labels/eligible_truth_0.csv --predictions reports/public_predictions.csv --output reports/public_reproduced_metrics.json`

This reproduces the evaluation of saved predictions. It does not independently rerun the complete OCR extraction process.

## 6. Reproduced Results

| Metric | Result |
|---|---:|
| Evaluated drawings | 1 |
| Eligible ground-truth occurrences | 79 |
| Predictions | 39 |
| True positives | 38 |
| False positives | 1 |
| False negatives | 41 |
| Precision | 97.44% |
| Recall | 48.10% |
| F1 | 64.41% |

The baseline achieves high precision on the reviewed sample but misses 41 of the 79 eligible annotated occurrences.

## 7. Limitations and Validation Status

- Only one synthetic P&ID drawing has been evaluated.
- Manual annotations have not undergone independent expert validation.
- The annotation inventory may be incomplete.
- Five two-hyphen identifiers are excluded from the evaluation.
- Spatial matching and bounding-box accuracy are not measured.
- Identifier-shaped strings are not separately validated as equipment tags.
- A held-out multi-drawing test set has not been established.
- Reproducibility has been demonstrated for the saved CSV evaluation, not yet for the full OCR extraction pipeline.

The earlier 90% extraction claim cannot be verified using the available original project materials. This benchmark is separate and does not reproduce that result.

## 8. Future Evaluation Improvements

1. Independently validate the annotations.
2. Expand the dataset to multiple drawings.
3. Establish a frozen, drawing-level held-out test set.
4. Evaluate bounding-box and spatial matching.
5. Analyze OCR misses and false positives.
6. Rerun the full extraction pipeline and document the environment and preprocessing settings.
7. Compare improved extraction approaches against the baseline.