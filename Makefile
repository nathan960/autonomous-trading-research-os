.PHONY: compile dry-run test check diff

compile:
	python -m compileall src scripts tests

dry-run:
	python scripts/run_all_dry_run.py

test:
	python -m unittest discover -s tests

check: compile dry-run test

diff:
	git diff --stat && git diff
