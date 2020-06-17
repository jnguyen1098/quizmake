# Makefile of doom

TESTDIR = tests/

.PHONY: refresh test clean

help:
	@echo ""
	@echo "======================== Main Recipes ============================="
	@echo ""
	@echo "    all"
	@echo "        installs, tests, uninstalls"
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

all: lint install test uninstall

lint:
	flake8
	isort --recursive --diff
	black --check .
	mypy

install:
	sudo pip3 install .

test:
	pytest $(TESTDIR)/smoke_tests/
	pytest $(TESTDIR)/end_to_end_tests/
	pytest $(TESTDIR)/regression_tests/
	pytest $(TESTDIR)/integration_tests/
	pytest $(TESTDIR)/unit_tests/

uninstall:
	- yes | sudo python3 -m pip uninstall quizmake

# External Stuff

piptest:
	pipenv install --dev --deploy
	pipenv run pytest $(TESTDIR)/smoke_tests/
	pipenv run pytest $(TESTDIR)/end_to_end_tests/
	pipenv run pytest $(TESTDIR)/regression_tests/
	pipenv run pytest $(TESTDIR)/integration_tests/
	pipenv run pytest $(TESTDIR)/unit_tests/
	pipenv --rm

push:
	git add *
	git status
	git commit -a
	git push

publish:
	sudo python3 setup.py sdist
	sudo python3 setup.py bdist_wheel
	twine upload dist/*

# Housekeeping

clean:
	- rm -rf build/ dist/ *.egg-info
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -name "*.pyc" -type f -exec rm -r "{}" \;

