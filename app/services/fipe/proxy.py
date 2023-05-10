import json

import requests

from app.config import settings
from app.exceptions import HTTPError


class Fipe:
    def __init__(self):
        self.url = settings.fipe_base_url

    def _request(self, endpoint, method, data=None):
        if data is None:
            data = {}
        url = self.url + endpoint
        headers = {
            "Content-Type": "application/json",
        }
        try:
            response = requests.request(method, url, json=data, headers=headers)
        except Exception as e:
            raise HTTPError(status_code=404, detail=str(e))
        else:
            if not response.ok:
                return HTTPError(status_code=response.status_code, detail=response.text)
        return json.loads(response.text)

    def load_brands(self):
        method = "GET"
        endpoint = ""
        result = self._request(endpoint, method)
        return result

    def set_model_info(self, brand):
        method = "POST"
        endpoint = "model"
        result = self._request(endpoint, method, {"brand": brand})
        return result
