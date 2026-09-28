from json_rules_engine import RuleEngine

def test_valid_rule():
    engine = RuleEngine({"min_score": 80})
    assert engine.evaluate({"score": 90})["passed"] == True

def test_failing_rule():
    engine = RuleEngine({"min_score": 80})
    assert engine.evaluate({"score": 50})["passed"] == False
