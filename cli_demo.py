"""
cli_demo.py

Author: Eugenia Tate
Date: August 24, 2025

A simple command-line application for a car dealership that allows users 
to look up vehicle information (year, make, and model) by VIN number. 
The data is retrieved from the NHTSA (National Highway Traffic Safety 
Administration) VIN decoding API via the helper module `nhtsa_api_call.py`.

Usage:
    python cli_demo.py
"""
import nhtsa_api_call, re

def is_valid_vin (vin):
    """
    Check whether vin is valid.
    A valid VIN is a VIN of 17 alphanumeric characters long and can not 
    include I, O, Q. 
    """
    vin = vin.upper()
    if len(vin) != 17:
        return False 
    if not re.match(r'^[A-HJ-NPR-Z0-9]{17}$', vin):
        return False
    return True

def main():
    """
    Run the command-line VIN lookup loop.

    Prompts the user for a VIN number, calls the NHTSA API,
    and prints out the vehicle information if found.
    Enter '0' to exit.
    """
    print("🚗 Welcome to the Car Dealership VIN Lookup!\n")
   
    while True:
        vin = input("Please enter a valid VIN or 0 (zero) to exit: \n").strip()
        # exit condition gets checked first
        if vin == "0":
            print("👋 You chose to exit VIN lookup. Goodbye!")
            break
        # check if vin is valid, and if not print error message
        if not is_valid_vin(vin): 
            print("⚠️ Invalid VIN format. Must be 17 letters/numbers (no I, O, Q). Try again.\n")
            continue
         # vin is valid, perform VIN lookup
        else:
            year, make, model = nhtsa_api_call.get_vehicle_info(vin)
            if year and make and model:
                print(f"✅ VIN {vin}")
                print(f"   Year: {year}")
                print(f"   Make: {make}")
                print(f"   Model: {model}")
            else:
                print(f"❌ VIN {vin} not found in database. Try again.")

if __name__ == "__main__":
    main()
