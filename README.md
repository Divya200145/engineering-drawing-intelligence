# Engineering Drawing Tag Extraction — Public Reproduction Starter

**Status: baseline implementation and synthetic smoke test only. NOT a completed public-dataset evaluation.**

This independently authored starter project is intended to make equipment-tag OCR and its evaluation reproducible. It is **not evidence of the previously stated 90% result**, and it does not claim to reproduce a prior project.

## What is included
- An OCR pipeline using Tesseract via `pytesseract` to identify equipment tags in images.
- Deterministic, one-to-one exact-match evaluation, with precision, recall and F1.
- Synthetic demonstration drawing and human-specified demonstration labels, explicitly marked as **synthetic**.
- Tests, data format, CLI, and a report template.

## Public engineering datasets to investigate
- PID2Graph: https://github.com/LatentSpaceIITB/pid_drawings
- PIDQA: https://github.com/mgupta70/PIDQA
- Zenodo P&ID source: https://zenodo.org/records/8028570

**These are candidate sources, not a claim that their labels support equipment-tag OCR.** Check licensing, actual contents, and annotation coverage before using any. Do not copy protected images into this repo without permission.

## Installation
Python 3.10+; Tesseract OCR must be installed separately:
- Ubuntu: `sudo apt-get install tesseract-ocr`
- macOS (Homebrew): `brew install tesseract`

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m src.extract --input data/demo/images --output reports/demo_predictions.csv
python -m src.evaluate --truth data/demo/labels/ground_truth.csv --predictions reports/demo_predictions.csv --output reports/demo_metrics.json
```

## Data format
Ground truth CSV columns: `drawing_id,tag`. One row per actual tag occurrence. Predicted CSV columns: `drawing_id,tag`. Duplicate tags count as separate occurrences. A prediction can match at most one ground-truth row. Matching uses uppercasing and trimming only. Spatial coordinates are NOT currently evaluated.

## Public benchmark protocol (not yet performed)
1. Select licensed public P&ID drawings, record URLs, versions, file hashes and permission terms in `dataset_sources.md`.
2. Manually transcribe visible equipment tags with a written tagging policy, recording drawing IDs. Keep these labels independent of OCR predictions.
3. Partition drawings into development and held-out test groups; freeze test labels before tuning.
4. Run `python -m src.extract --input PATH --output reports/public_predictions.csv`.
5. Run `python -m src.evaluate --truth PATH_TO_LABELED_CSV --predictions reports/public_predictions.csv --output reports/public_metrics.json`.
6. Publish the complete test manifest, counts, per-drawing predictions, failure analysis and actual measured scores.
7. Never call a new score a reproduction of an earlier 90% claim unless the original evidence exists.

## Limitations
The baseline uses OCR and a conservative tag pattern; it does not understand diagram connectivity, recognize all symbols, or validate engineering semantics. The synthetic smoke test is not representative of real P&IDs. OCR requires Tesseract installed on the machine. False positives and misses are expected on dense drawings.

## Provenance and disclosure
Created as a new, independent reproducible baseline after the interview. It does not establish what dataset or results were used in any prior project.

## Verified demonstration outputs
See `reports/demo_predictions.csv`, `reports/demo_metrics.json`, and `reports/EVALUATION_METHODOLOGY.md` for the **synthetic-only** smoke test. See `PROJECT_STATUS.md` for an honest requirement-by-requirement checklist.

## Publish to GitHub
1. Create a new public GitHub repository named `engineering-drawing-intelligence`.
2. From this folder, run `git init && git add . && git commit -m "Add reproducible OCR baseline and transparent evaluation"`.
3. Add the repository remote supplied by GitHub, then push your branch. Never upload company-proprietary drawings or credentials.
4. Verify that GitHub Actions passes and that the README prominently identifies the public-benchmark work as pending.
