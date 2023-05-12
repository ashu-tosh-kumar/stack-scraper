import logging

from flask import Flask

from src.db_wrappers.in_memory_db import InMemoryDatabaseWrapper

# ---------- Flask ----------
app = Flask(__name__)


# ---------- Logger ----------
logger = logging.getLogger(__name__)


# ---------- Database ----------
db = InMemoryDatabaseWrapper(logger)
