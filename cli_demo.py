import nhtsa_api_call

def main():
    print("🚗 Welcome to the Car Dealership VIN Lookup!\n")
    keep_searching = True
    while keep_searching:
        vin = input("Please enter a valid VIN or 0 (zero) to exit: \n").strip()
        if vin == "" or vin == None: 
            keep_searching = True
            continue
        else:
            year, make, model = nhtsa_api_call.get_vehicle_info(vin)
            if year and make and model:
                print(f"✅ VIN {vin}")
                print(f"   Year: {year}")
                print(f"   Make: {make}")
                print(f"   Model: {model}")
                keep_searching = True
            elif vin == "0":
                keep_searching = False
                break
            else:
                print(f"❌ VIN {vin} not found in database. Try again.")
                keep_searching = True

if __name__ == "__main__":
    main()
