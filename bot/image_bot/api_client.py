import requests


class APIClient:
    DOG_URL = "https://dog.ceo/api/breeds/image/random"
    CAT_URL = "https://api.thecatapi.com/v1/images/search?mime_types=jpg,png"
    FOX_URL = "https://randomfox.ca/floof/"

    def get_image_url(self, api_type: str) -> str:
        api_type = api_type.lower().strip()

        if api_type == "dog":
            data = self._get_json(self.DOG_URL)
            return data["message"]

        if api_type == "cat":
            data = self._get_json(self.CAT_URL)
            if not data:
                raise RuntimeError("Cat API bo'sh javob qaytardi")

            url = data[0].get("url")
            if not url:
                raise RuntimeError("Cat API url qaytarmadi")

            return url

        if api_type == "fox":
            data = self._get_json(self.FOX_URL)
            return data["image"]

        raise ValueError("api_type faqat: dog, cat, fox bo'lishi kerak")

    def _get_json(self, url: str):
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
