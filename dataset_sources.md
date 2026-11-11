# Dataset Source Manifest

## Selected dataset

- Dataset: PID2Graph
- Zenodo record: https://zenodo.org/records/14803338
- DOI: https://doi.org/10.5281/zenodo.14803338
- Archive: PID2Graph.zip
- Source subset: Complete/Dataset PID
- Original files: 0.png and 0.graphml
- Dataset authors: Jan Marius Stürmer, Marius Graumann, Tobias Koch
- Publication date: 2025-02-14
- License for Dataset PID subset: CC BY-SA 4.0
- License: https://creativecommons.org/licenses/by-sa/4.0/

## Local file provenance

| Local file | Original source file |
|---|---|
| data/public/images/0.png | Complete/Dataset PID/0.png |
| data/public/labels/0.graphml | Complete/Dataset PID/0.graphml |

## SHA-256 checksums

| File | SHA-256 |
|---|---|
| 0.png | 29988daecbbfa9f82fd1339c81fb9b8dc3d8174ead3238ff4c14f70ac0d3bbe0 |
| 0.graphml | c21f687f28568cf8a776c92b61d3f606360d31823949fa702e44636f36a3ee1a |
| manual_review_0.csv | db6efcf77249d55c624248cf6f59abf5c5ed06460367e557c1b9ff4346928a8c |

## Ground-truth annotation provenance

- Drawing ID: 0
- Annotation file: data/public/labels/manual_review_0.csv
- Annotation entries: 84
- Eligible single-hyphen identifiers: 79
- Unsupported two-hyphen ERV identifiers: 5
- Annotation method: Manual visual transcription from drawing sections and enlarged screenshots.
- Reviewer: Project reviewer.
- Domain-expert validation: Not established.
- OCR predictions were not used as the sole source of manual annotations.

The GraphML file provides diagram-object and connectivity
annotations. It is not treated as complete OCR equipment-tag
ground truth.

## Evaluation scope

One drawing was evaluated. This is a single-drawing exploratory
benchmark, not a representative multi-drawing test set.

Results must be interpreted alongside annotation completeness,
tile-boundary handling, and the limitations of the baseline
identifier regular expression.

## Attribution and redistribution

The selected Dataset PID subset is identified by the PID2Graph
Zenodo record as CC BY-SA 4.0.

Redistributed material must retain appropriate attribution,
license information, and applicable ShareAlike obligations.

The license and provenance of other PID2Graph subsets must be
checked independently before redistribution.

## Outstanding limitations

- Only one drawing evaluated.
- Independent domain-expert validation not established.
- Complete annotation coverage not independently established.
- Five two-hyphen identifiers excluded from baseline evaluation.
- Historical 90 percent accuracy claim not reproduced.
