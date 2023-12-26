# FastAPI + SQLAlchemy 2.0 + SQLModel + alembic + pytest

### Первый запуск проекта

Устанавливаем virtualenv и все зависимости (python >= 3.11):

```bash
python3.11 -m venv .venv
```

или

```bash
/full/path/to/python3 -m venv .venv
```

Установка зависимостей можно выполнить упрощенной командой: `make envup`

В каталоге core необходимо скопировать config_local.py.example в config_local.py
и проставить параметры для БД:

```
cd core
cp config_local.py.example config_local.py
```

Либо прописать нужные параметры `.env` в корневом каталоге.

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=somedbpass
POSTGRES_PORT=5432
POSTGRES_DB=somedb
PYTEST_DBURL=postgresql+asyncpg://postgres:pgpassw@localhost:5432/somedb_test
SECRET_KEY=someappsecret
```

Необходимо провести миграции:

`make db_migrate`

Запуск вебсервера:

`make run`

# Доступные команды

```bash
# Запуск сервера
make run

# Запуск тестов
make test

# Проверка стиля кода
make style

# Создание новой миграции
make db_revision m="new name migration"
```
