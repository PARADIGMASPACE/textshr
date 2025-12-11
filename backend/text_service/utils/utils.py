import uuid
from passlib.hash import bcrypt


def generate_key() -> str:
    return str(uuid.uuid4())


def hash_password(password: str) -> str:
    return bcrypt.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)
