from urllib import response
import requests


def get_rate():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {"X-CoinAPI-Key": "509C34C2-5F43-4BC5-84A6-8E9CF81F0AD3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error: {} {}".format(response.status_code, response.text))
