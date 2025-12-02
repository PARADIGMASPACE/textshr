from minio import Minio
from ..config import MinioSettings

def create_MinioClient():
    settings = MinioSettings()
    return  Minio(
        endpoint=settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=settings.MINIO_SECURE
    )
