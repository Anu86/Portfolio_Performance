from dotenv import load_dotenv
import requests
from flatten_json import flatten
import os

load_dotenv()
polygon_api_key = os.getenv("POLYGON_API_SECRET_KEY")
# polygon_name = os.getenv("NAME")


def retrieve_Market_data(symbol, range, start_date, end_date):
    URL = (
        "https://api.polygon.io/v2/aggs/ticker/"
        + symbol
        + "/range/"
        + range
        + "/day/"
        + start_date
        + "/"
        + end_date
        + "?adjusted=true&sort=asc&limit=120&apiKey="
        + polygon_api_key
    )
    session = requests.Session()
    response = session.get(URL)
    if response.status_code == 200:
        market_data = flatten(response.json())
        return market_data
    else:
        print(response.content)
        print("Polygon API Errored")
