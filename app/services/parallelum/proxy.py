import json

import requests
from starlette.responses import JSONResponse

from app.config import settings
from app.exceptions import HTTPError


class Parallelum:
    def __init__(self):
        self.url = settings.parallelum_base_url

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

    def get_brands(self):
        method = "GET"
        endpoint = "carros/marcas"
        result = self._request(endpoint, method)
        return result

    def get_models_info(self, model_id):
        method = "GET"
        endpoint = f"carros/marcas/{model_id}/modelos"
        result = self._request(endpoint, method, {})
        return result
