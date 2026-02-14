from .api_client import APIClient
from .image_service import ImageService
from .handlers import Handlers


class ImageBot:
    def __init__(self, token: str):
        self.token = token

        self.api_client = APIClient()
        self.image_service = ImageService(self.api_client)
        self.handlers = Handlers(self.image_service)
