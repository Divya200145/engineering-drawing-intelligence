# Evaluation methodology and reproducibility

## Scope
The implemented baseline extracts equipment-tag-shaped text from raster drawing images using Tesseract OCR and a regular expression. It does not infer P&ID connections or validate engineering meaning.

## Ground truth
The included `data/demo/labels/ground_truth.csv` is an independently specified list of two text labels drawn into an **original synthetic image** (`data/demo/images/demo_001.png`). It is a functional smoke-test fixture, **not** a public engineering dataset or a domain-expert-reviewed benchmark.

## Evaluation procedure
1. Run `python -m src.extract --input data/demo/images --output reports/demo_predictions.csv`.
2. Run `python -m src.evaluate --truth data/demo/labels/ground_truth.csv --predictions reports/demo_predictions.csv --output reports/demo_metrics.json`.
3. Matching is by `(drawing_id, tag)` after trimming and uppercasing. Each prediction can match at most one ground-truth occurrence. Duplicates are counted.
4. TP = matched instances; FP = unmatched predictions; FN = unmatched truth instances. Precision = TP/(TP+FP), recall = TP/(TP+FN), F1 = 2PR/(P+R). Undefined denominators are reported as 0 by this baseline.

## Verified demonstration result
- Drawings: 1 (synthetic)
- Ground truth: 2 tags
- Predictions: 2 tags
- True positives: 2; false positives: 0; false negatives: 0
- Precision: 1.0; recall: 1.0; F1: 1.0

**Interpretation:** this only demonstrates that the software can identify two large, clear text labels in a synthetic fixture. It says nothing about performance on real P&ID drawings.

## Required for Bechtel's requested public benchmark
- Identify and license-check an actual public P&ID dataset.
- Determine whether it includes equipment-tag text labels; otherwise create and independently verify labels, recording provenance.
- Freeze drawing-level held-out test split before tuning.
- Publish exact data manifest, evaluation labels, raw predictions, test commands, failures, and results.
- Report measured public benchmark precision, recall, F1; do not imply the interview's 90% figure is independently reproduced.
