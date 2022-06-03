import requests
import json


class WebClient:
    def __init__(self, url, app_id):
        self.url = url
        self.app_id = app_id

    def __request_info(self):
        response = requests.get(f"{self.url}/api/latest.json?app_id={self.app_id}")
        json_data = json.loads(response.text)
        return json_data

    def request_rate(self, key):
        json_data = self.__request_info()
        rate = json_data["rates"][key]
        return rate
