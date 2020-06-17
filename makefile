# Makefile of doom

TESTDIR = tests/

.PHONY: refresh test clean

help:
	@echo ""
	@echo "    default"
	@echo "        lint, install, test, clean."
	@echo ""
	@echo "    install"
	@echo "        Rebuild and install the project."
	@echo ""
	@echo "    test"
	@echo "        Tests the project."
	@echo ""
	@echo "    clean"
	@echo "        Cleans up build, dist, and other misc. stuff."
	@echo ""
	@echo "    lint"
	@echo "        runs flake8"
	@echo ""
	@echo "    publish"
	@echo "        Publishes it on PyPi."
	@echo ""
	@echo "    uninstall"
	@echo "        Uninstalls quizmake."
	@echo ""

# Main stuff

test:
	flake8
	isort --recursive --diff
	black --check .
	mypy
	pytest $(TESTDIR)

install:
	sudo pip3 install .

uninstall:
	- yes | sudo python3 -m pip uninstall quizmake

# External Stuff

piptest:
	pipenv install --dev --deploy
	pipenv run pytest

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

