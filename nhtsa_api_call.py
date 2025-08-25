import requests

def get_vehicle_info(vin):
    """
    This function takes the parameter "vin" and uses the NHTSA Decode VIN API to retrive year, make, and model
    The API returns a JSON file which is not a dictionary so the file must be searched with a for loop by "Variable"
    For more API information visit https://vpic.nhtsa.dot.gov/api/
    """
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
		