import requests
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from email_notification_manager import Email
#storing specified destination data in data_manager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
ORIGIN_CITY_IATA = "SAN"
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# getting the flights within the next three months
tomorrow = datetime.now() + timedelta(days=1)
three_month_from_today = datetime.now() + timedelta(days=(3 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=three_month_from_today
    )
    try:
        if flight.price < destination["lowestPrice"]:
            email = Email("DestinationEmail")
            email.send(f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
)
    except:
        print("We could not find any flight for this city")
