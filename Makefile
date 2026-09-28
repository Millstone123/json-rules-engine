.PHONY: bootstrap test

bootstrap:
	python3 -m venv .venv && .venv/bin/pip install -r requirements.txt --quiet && .venv/bin/python -m json_rules_engine.native_profile

test:
	.venv/bin/python -m pytest tests -q
