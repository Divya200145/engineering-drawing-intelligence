# Engineering Drawing Intelligence — OCR Identifier Extraction

**Status:** Exploratory public-dataset evaluation completed. Further validation required.

## Project Overview

This project implements a reproducible baseline for extracting identifier-shaped text from engineering drawings using optical character recognition (OCR).

The pipeline combines Tesseract OCR, image preprocessing, regular-expression-based identifier extraction, and exact-match evaluation.

The objective is to measure extraction performance, understand failure cases, and establish a baseline for future improvements.

## Technologies

- Python
- Tesseract OCR and pytesseract
- Image preprocessing
- Regular expressions
- CSV and JSON
- Pytest
- GitHub

## Dataset

The exploratory benchmark uses one publicly sourced synthetic P&ID drawing from PID2Graph (Zenodo record 14803338).

The accompanying GraphML file contains diagram component and connectivity annotations, not verified identifier transcriptions.

A project reviewer manually recorded 84 identifier occurrences.

- Total annotations: 84
- Eligible identifier occurrences: 79
- Excluded two-hyphen ERV identifiers: 5
- OCR predictions: 39

The benchmark evaluates identifier-shaped text rather than independently verified equipment-tag classifications.

See `dataset_sources.md` for dataset provenance.

## Benchmark Results

| Metric | Result |
|---|---:|
| Ground-truth occurrences | 79 |
| OCR predictions | 39 |
| True positives | 38 |
| False positives | 1 |
| False negatives | 41 |
| Precision | 97.44% |
| Recall | 48.10% |
| F1 score | 64.41% |

The evaluation uses normalized exact-string matching within each drawing and retains duplicate identifier occurrences.

The results are reproducible from the saved ground-truth and prediction CSV files. They do not establish full end-to-end OCR reproducibility.

## Installation

Requirements:

- Python 3.10 or later
- Tesseract OCR

On Ubuntu:

`sudo apt-get install tesseract-ocr`

On macOS with Homebrew:

`brew install tesseract`

Install Python dependencies:

`python -m pip install -r requirements.txt`

Run tests:

`python -m pytest -q`

## Reproduce the Public Evaluation

From the repository root, run:

`python src/evaluate.py --truth data/public/labels/eligible_truth_0.csv --predictions reports/public_predictions.csv --output reports/public_reproduced_metrics.json`

This evaluates the saved OCR predictions against the 79 eligible manually reviewed identifier occurrences.

## Demonstration Pipeline

Run the synthetic demonstration extraction:

`python -m src.extract --input data/demo/images --output reports/demo_predictions.csv`

Evaluate the demonstration:

`python -m src.evaluate --truth data/demo/labels/ground_truth.csv --predictions reports/demo_predictions.csv --output reports/demo_metrics.json`

The demonstration and public exploratory benchmark are separate evaluations.

## Evaluation Methodology

The evaluator:

1. Normalizes identifiers by removing surrounding whitespace and converting text to uppercase.
2. Matches predictions and annotations by drawing ID and exact identifier string.
3. Retains repeated identifier occurrences.
4. Counts true positives, false positives, and false negatives.
5. Calculates precision, recall, and F1 score.

Spatial bounding boxes and diagram connectivity are not evaluated.

## Limitations

- The public benchmark covers only one synthetic drawing.
- The annotations were manually reviewed but not independently validated.
- The annotation inventory may be incomplete.
- Five two-hyphen ERV identifiers are outside the current evaluation scope.
- Exact-string matching does not verify spatial localization.
- The pipeline does not independently establish equipment-tag classification accuracy.
- Results cannot be generalized to real industrial drawings.

## Future Improvements

- Expand the dataset to multiple engineering drawings.
- Independently validate the annotations.
- Add bounding-box-level evaluation.
- Investigate missed identifiers and OCR failure modes.
- Improve preprocessing and extraction coverage.
- Compare alternative extraction methods against the baseline.

## Project Provenance

This is an independently authored reproducible baseline developed after an interview discussion.

A previously discussed 90% extraction result cannot be verified from the available original project materials. This benchmark does not establish or reproduce that earlier figure.

## Documentation

- `reports/FINAL_REPORT.md` — Evaluation results and limitations
- `reports/EVALUATION_METHODOLOGY.md` — Evaluation methodology
- `dataset_sources.md` — Dataset provenance
- `PROJECT_STATUS.md` — Project progress and outstanding work

## Responsible Use

Use only datasets with appropriate permissions and attribution. Do not upload proprietary engineering drawings, credentials, or confidential company information.