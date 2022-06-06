import requests
import json
import psycopg2


class WebClient:
    def __init__(self, url, app_id):
        self.url = url
        self.app_id = app_id

    def request_info(self):
        response = requests.get(f"{self.url}/api/latest.json?app_id={self.app_id}")
        json_data = json.loads(response.text)
        return json_data

    def request_rate(self, key):
        json_data = self.__request_info()
        rate = json_data["rates"][key]
        return rate

    def write_to_base(self):
        response = requests.get(f"{self.url}/api/latest.json?app_id={self.app_id}")
        json_data = json.loads(response.text)
        rates = json_data["rates"]
        UAH = rates["UAH"]
        GBP = rates["GBP"]
        PLN = rates["PLN"]
        EUR = rates["EUR"]
        timestamp = json_data["timestamp"]
        conn = psycopg2.connect(host='localhost', database='scraper_db', user='scraper_user', password='qwerty')
        sql = f"INSERT INTO json_base \
              VALUES ({UAH}, {GBP}, {PLN}, {EUR}, {timestamp})"
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
