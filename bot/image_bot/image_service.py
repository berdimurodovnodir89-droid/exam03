from .api_client import APIClient


class ImageService:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def fetch_random_image(self, animal: str) -> str:
        animal = animal.lower().strip()
        if animal not in ("dog", "cat", "fox"):
            raise ValueError("animal faqat: dog, cat, fox bo'lishi kerak")

        return self.api_client.get_image_url(animal)
