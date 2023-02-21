import os

POSTGRES_USER = os.environ.get("PG_USER", "test")
POSTGRES_PASSWORD = os.environ.get("PG_PASS", "test")
POSTGRES_NAME = os.environ.get("PG_NAME", "test")
