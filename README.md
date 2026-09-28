# json-rules-engine

A lightweight Python rules engine for evaluating JSON-based business rules.

## Setup

```sh
make bootstrap
```

## Usage

```python
from json_rules_engine import RuleEngine

engine = RuleEngine({"min_score": 80})
result = engine.evaluate({"score": 90})
```

## Tests

```sh
make test
```
