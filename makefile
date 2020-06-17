# Makefile of doom

.PHONY: refresh test clean

help:
	@echo ""
	@echo "    all"
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

all: lint install test clean

lint:
	flake8

install:
	sudo pip3 install .

test:
	pytest
#	pytest --maxfail=2

clean:
	- rm -rf build/ dist/ *.egg-info
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -name "*.pyc" -type f -exec rm -r "{}" \;

publish:
	sudo python3 setup.py sdist
	sudo python3 setup.py bdist_wheel
	twine upload dist/*

uninstall:
	- yes | sudo python3 -m pip uninstall quizmake
