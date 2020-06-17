# Makefile of doom

.PHONY: refresh test clean

help:
	@echo ""
	@echo "    all"
	@echo "        refresh, test, clean."
	@echo ""
	@echo "    refresh"
	@echo "        Rebuild and install the project."
	@echo ""
	@echo "    test"
	@echo "        Tests the project."
	@echo ""
	@echo "    clean"
	@echo "        Cleans up build, dist, and other misc. stuff."
	@echo ""
	@echo "    publish"
	@echo "        Publishes it on PyPi."
	@echo ""

all: refresh test clean

refresh:
	sudo python3 setup.py build
	sudo python3 setup.py install

test:
	python3 tests/test.py

clean:
	- rm -rf build/ dist/ *.egg-info
	- find . -type d -name "__pycache__" -exec rm -rf {} \;
	- find . -type f -name "*.pyc" -exec rm {} \;

publish:
	sudo python3 setup.py sdist
	sudo python3 setup.py bdist_wheel
	twine upload dist/*
