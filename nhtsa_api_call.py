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
    # year =
    # make = 
    # model = 
    print(year)
    print(make)
    print(model)
    return year, make, model	
		
vin_num = input("What is vin number")

get_vehicle_info(vin_num)