.PHONY: style test ci_check envup run db_revision

VENV_BIN_PATH = ./.venv/bin
PYTHONPATH = $(shell pwd)
SOURCE_DIR = ./source/

envup:
	$(VENV_BIN_PATH)/pip3 install -c ${SOURCE_DIR}constraints-pre.txt -r ${SOURCE_DIR}requirements-pre.txt
	$(VENV_BIN_PATH)/pip3 install -c ${SOURCE_DIR}constraints.txt -r ${SOURCE_DIR}requirements.txt
	$(VENV_BIN_PATH)/pip3 install -c ${SOURCE_DIR}constraints-dev.txt -r ${SOURCE_DIR}requirements-dev.txt

style:
	$(VENV_BIN_PATH)/flake8 core
	$(VENV_BIN_PATH)/flake8 --ignore=D tests

test:
	$(VENV_BIN_PATH)/python3 -m pytest --verbose tests/

xtest:
	$(VENV_BIN_PATH)/python3 -m pytest -x tests/

ci_check: style test

run:
	PYTHONPATH=$(PYTHONPATH) $(VENV_BIN_PATH)/uvicorn core.app:app --reload --workers 1 --host 0.0.0.0 --port 8095

db_revision:
	PYTHONPATH=$(PYTHONPATH) $(VENV_BIN_PATH)/alembic revision --autogenerate -m "${m}"

db_migrate:
	PYTHONPATH=$(PYTHONPATH) $(VENV_BIN_PATH)/alembic upgrade head
