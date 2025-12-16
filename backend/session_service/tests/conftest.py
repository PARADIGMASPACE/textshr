import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def setup_test_env():
    os.environ["REDIS_HOST"] = "localhost"
    os.environ["REDIS_PORT"] = "6379"
    os.environ["REDIS_PASSWORD"] = "redis"
    os.environ["REDIS_DB"] = "0"