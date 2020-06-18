SHELL := /bin/bash
TESTDIR = tests/

.PHONY: refresh test clean

help:
	@echo ""
	@echo "======================== Main Recipes ============================="
	@echo ""
	@echo "    all"
	@echo "        lints, installs, tests, uninstalls"
	@echo ""
	@echo "    lint"
	@echo "        lints the code"
	@echo ""
	@echo "    install"
	@echo "        builds and installs quizmake"
	@echo ""
	@echo "    test"
	@echo "        runs all tests"
	@echo ""
	@echo "    uninstall"
	@echo "        uninstalls quizmake."
	@echo ""
	@echo "======================== Dev. Recipes ============================="
	@echo ""
	@echo "    piptest"
	@echo "        runs the above tests in a pipenv virtual environment"
	@echo ""
	@echo "    push"
	@echo "        pushes current progress to GitHub"
	@echo ""
	@echo "    publish"
	@echo "        uploads current build to PyPi using twine"
	@echo ""
	@echo "    clean"
	@echo "        cleans up all extraneous files/folders"
	@echo ""
	@echo "==================================================================="
	@echo ""

# Main stuff

# Level 1: -e testing
# Level 2: make all
# Level 3: formal pip install
# Level 4: venv?
# Level 5: pipenv?
# Level 6: git push into github actions
# Level 7: push to pypi

all: lint install test uninstall

lint:
	isort --recursive --diff
	mypy
	black --diff --check .
	flake8
	pylint quizmake
	pylint tests/*/*.py

install:
	pip3 install --editable .

test:
	- pytest $(TESTDIR)/smoke_tests/ $(TESTDIR)/end_to_end_tests \
           $(TESTDIR)/regression_tests/ $(TESTDIR)/integration_tests/ \
           $(TESTDIR)/unit_tests/

uninstall:
	- yes | pip3 uninstall quizmake

# External Stuff

piptest: clean
	pipenv install --dev --deploy
	pipenv run pytest $(TESTDIR)/smoke_tests/ $(TESTDIR)/end_to_end_tests \
                      $(TESTDIR)/regression_tests/ $(TESTDIR)/integration_tests/ \
                      $(TESTDIR)/unit_tests/
	pipenv --rm

push: clean
	git add .
	git status
	git commit -a
	git push

publish: clean
	vim setup.py
	sudo python3 setup.py sdist
	sudo python3 setup.py bdist_wheel
	twine upload dist/*

# Housekeeping

clean:
	- rm -rf build/ dist/ *.egg-info
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -name "*.pyc" -type f -exec rm -r "{}" \;
