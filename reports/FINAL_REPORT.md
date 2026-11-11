# Engineering Drawing Extraction — Evaluation Report

**Status:** Exploratory public benchmark completed; further validation required.

## Objective

Evaluate a baseline OCR-based identifier extraction pipeline using a publicly sourced synthetic P&ID engineering drawing.

## Implementation

The baseline uses Tesseract OCR, grayscale and contrast enhancement, regular-expression-based identifier extraction, and exact-match evaluation.

## Dataset and Ground Truth

**Source:** PID2Graph, Zenodo record 14803338.

The evaluation uses one synthetic P&ID drawing and its associated GraphML file. The GraphML contains diagram component and connectivity annotations, not verified identifier transcriptions.

A project reviewer manually recorded 84 identifier occurrences. Of these, 79 meet the benchmark's identifier pattern, while five two-hyphen ERV identifiers are excluded.

The annotations have not been independently validated and may not be exhaustive.

## Benchmark Results

| Metric | Result |
|---|---:|
| Eligible ground-truth occurrences | 79 |
| OCR predictions | 39 |
| True positives | 38 |
| False positives | 1 |
| False negatives | 41 |
| Precision | 97.44% |
| Recall | 48.10% |
| F1 score | 64.41% |

## Reproducibility

The results were reproduced using `src/evaluate.py` with:

- Ground truth: `data/public/labels/eligible_truth_0.csv`
- Predictions: `reports/public_predictions.csv`
- Output: `reports/public_reproduced_metrics.json`

The evaluation matches normalized identifier strings within each drawing and retains repeated occurrences. It does not validate spatial localization.

## Interpretation

The baseline demonstrates high precision on this reviewed sample, but relatively low recall. It correctly matches 38 predictions while missing 41 annotated occurrences.

Improving OCR coverage and detecting missed identifiers are important priorities for future development.

## Limitations

- Evaluation covers only one synthetic drawing.
- Ground-truth annotations have not undergone independent expert review.
- Annotation coverage may be incomplete.
- Five two-hyphen ERV identifiers are excluded.
- Spatial localization and bounding-box accuracy are not evaluated.
- Identifier-shaped text is not separately verified as equipment tags.
- Results cannot be generalized to industrial engineering drawings.

## Prior Interview Statement

A previously discussed 90% extraction result cannot be verified using the available original project materials.

This exploratory benchmark is a separate evaluation and does not establish or reproduce that earlier figure.

## Next Steps

1. Independently validate annotations and drawing locations.
2. Expand evaluation to multiple engineering drawings.
3. Introduce spatial matching and bounding-box evaluation.
4. Analyze missed identifiers and OCR failure cases.
5. Compare improved extraction approaches against this baseline.