import logging

from .minio_factory import MinioSettings

logger = logging.getLogger(__name__)

class MinioClient:
    def __init__(self):
        self.minio_factory = MinioSettings()

