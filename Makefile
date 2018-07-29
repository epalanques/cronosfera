MAKEFLAGS += --warn-undefined-variables

export ENV_LOCATION ?= $(realpath $(shell pipenv --venv))
export WORKON_HOME=.venvs

prp := pipenv run python
pr  := pipenv run

GENERATED_SRC_FOLDER:=generated

.PHONY: \
	setup \
	test


setup:
	@echo installing python dependencies

	pipenv install         --skip-lock
	pipenv install --dev   --skip-lock
	${pr} pip install -e .

test:
	${prp} -m pytest -s -v -vv --ignore=tests/event tests/
