import requests

def get_vehicle_info(vin):
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json'
    response = requests.get(url);
    data = response.json()

    for item in data["Results"]:
        if item["Variable"] in ["Model Year"]:
            year = item["Value"]
        if item["Variable"] in ["Make"]:
            make = item["Value"]
        if item["Variable"] in ["Model"]:
            model = item["Value"]
    
    return year, make, model	
		