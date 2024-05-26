help:
	@echo "Please use \`make <target>' where <target> is one or more of"
	@echo "  build        generate both sdist and wheel suitable for upload to PyPI"
	@echo "  clean        delete intermediate work product and start fresh"
	@echo "  coverage     run pytest with coverage"
	@echo "  test         run unit tests using pytest"
	@echo "  test-upload  upload distribution to TestPyPI"
	@echo "  upload       upload distribution tarball to PyPI"

.PHONY: build
build:
	rm -rf dist
	python -m build
	twine check dist/*

.PHONY: clean
clean:
	fd -t d "^__pycache__$$" . -x rm -rf
	fd -e pyc -I -x rm
	rm -rf dist .coverage .DS_Store

.PHONY: coverage
coverage:
	py.test --cov-report term-missing --cov=src tests/

.PHONY: test
test:
	pytest -x

.PHONY: test-release
test-release: build
	twine upload --repository testpypi dist/*

.PHONY: release
release: clean build
	twine upload dist/*
