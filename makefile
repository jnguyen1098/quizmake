SHELL := /bin/bash
TESTDIR = tests/

.PHONY: run install test uninstall lint clean piptest push publish

help:
	@echo -e ""
	@echo -e "======================== Main Recipes ============================="
	@echo -e ""
	@echo -e "    \e[7mall\e[0m"
	@echo -e "        install, lint, test"
	@echo -e ""
	@echo -e "          \e[7minstall\e[0m"
	@echo -e "              uninstalls existing copies, then installs"
	@echo -e ""
	@echo -e "          \e[7mlint\e[0m"
	@echo -e "              checks code with isort, mypy, black, flake8, pylint"
	@echo -e ""
	@echo -e "          \e[7mtest\e[0m"
	@echo -e "              smoke, end-to-end, regression, integration, unit"
	@echo -e ""
	@echo -e "                  \e[7msmoke\e[0m: runs a quick sanity test"
	@echo -e ""
	@echo -e "                  \e[7mend-to-end\e[0m: runs an exhaustive test suite"
	@echo -e ""
	@echo -e "                  \e[7mregression\e[0m: tests for problem regression"
	@echo -e ""
	@echo -e "                  \e[7mintegration\e[0m: tests for module cooperation"
	@echo -e ""
	@echo -e "                  \e[7munit\e[0m: tests individual modules in isolation"
	@echo -e ""
	@echo -e "    \e[7mclean\e[0m"
	@echo -e "        cleans up all extraneous files/folders"
	@echo -e ""
	@echo -e "    \e[7muninstall\e[0m"
	@echo -e "        uninstalls quizmake"
	@echo -e ""
	@echo -e "====================== Release Recipes ============================"
	@echo -e ""
	@echo -e "    \e[7mpiptest\e[0m"
	@echo -e "        runs tests in a pipenv virtual environment"
	@echo -e ""
	@echo -e "    \e[7mpush\e[0m"
	@echo -e "        pushes current progress to GitHub"
	@echo -e ""
	@echo -e "    \e[7mpublish\e[0m"
	@echo -e "        uploads current build to PyPi using twine"
	@echo -e ""
	@echo -e "==================================================================="
	@echo -e ""

# Main stuff

# Level 1: -e testing
# Level 2: make all
# Level 3: formal pip install
# Level 4: venv?
# Level 5: pipenv?
# Level 6: git push into github actions
# Level 7: push to pypi

all:
	make install
	make lint
	make test

install: uninstall
	pip3 install --editable .

lint:
	isort --recursive --diff
	mypy --strict --show-error-context --show-column-numbers --show-error-codes --pretty
	black --diff --check .
	flake8 --count --show-source --statistics
	pylint quizmake
	pylint tests/*/*.py

clean:
	- rm -rf build/ dist/ *.egg-info .mypy_cache .pytest_cache .coverage coverage.xml
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -name "*.pyc" -type f -exec rm -r "{}" \;

uninstall:
	- yes | pip3 uninstall quizmake

# Testing

test:
	pytest --cov=quizmake --cov-report term-missing --cov-report xml \
            $(TESTDIR)/smoke_tests/ $(TESTDIR)/end_to_end_tests \
            $(TESTDIR)/regression_tests/ $(TESTDIR)/integration_tests/ \
            $(TESTDIR)/unit_tests/

smoke:
	pytest --cov=quizmake --cov-report term-missing $(TESTDIR)/smoke_tests/

end-to-end:
	pytest --cov=quizmake --cov-report term-missing $(TESTDIR)/end_to_end_tests/

regression:
	pytest --cov=quizmake --cov-report term-missing $(TESTDIR)/regression_tests/

integration:
	pytest --cov=quizmake --cov-report term-missing $(TESTDIR)/integration_tests

unit:
	pytest --cov=quizmake --cov-report term-missing $(TESTDIR)/unit_tests/

# Production

piptest:
	pipenv install
	pipenv run pytest $(TESTDIR)/smoke_tests/ $(TESTDIR)/end_to_end_tests \
                      $(TESTDIR)/regression_tests/ $(TESTDIR)/integration_tests/ \
                      $(TESTDIR)/unit_tests/
	pipenv --rm

coveralls:
	test -f "coverage.xml"

push: coveralls
	coveralls
	git add .
	git status
	git commit -a
	git push

publish:
	vim setup.py
	sudo python3 setup.py sdist
	sudo python3 setup.py bdist_wheel
	twine upload dist/*
