from src.evaluate import score

def test_exact_matches():
    truth = [{"drawing_id":"a","tag":"P-101"},{"drawing_id":"a","tag":"V-202"}]
    pred = [{"drawing_id":"a","tag":"P-101"},{"drawing_id":"a","tag":"X-999"}]
    result = score(truth, pred)
    assert (result["true_positives"],result["false_positives"],result["false_negatives"]) == (1,1,1)
    assert result["f1"] == 0.5

def test_duplicate_instances_not_overcounted():
    truth = [{"drawing_id":"a","tag":"P-101"}]
    pred = [{"drawing_id":"a","tag":"P-101"},{"drawing_id":"a","tag":"P-101"}]
    result = score(truth, pred)
    assert (result["true_positives"],result["false_positives"],result["false_negatives"]) == (1,1,0)

def test_empty_predictions():
    result = score([{"drawing_id":"a","tag":"P-101"}],[])
    assert result["recall"] == 0
