import requests
from pprint import pprint
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/SHEETYAPIKEY/{PROJECT_NAME}/{SHEET_NAME}"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT)
        self.destination_data  = response.json()["prices"]
        return self.destination_data
    # sending a PUT request and using the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    