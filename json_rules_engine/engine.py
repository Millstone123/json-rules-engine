class RuleEngine:
    """Evaluate simple JSON-based rules with comparison operators."""

    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, data):
        for key, threshold in self.rules.items():
            if key in data and isinstance(threshold, (int, float)):
                if data[key] < threshold:
                    return {"passed": False, "field": key}
        return {"passed": True}
