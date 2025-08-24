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
import nhtsa_api_call

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
        # empty vin condition
        if not vin: 
            print("⚠️  VIN cannot be empty. Please try again.\n")
            continue
        # exit condition
        elif vin == "0":
            print("👋 Exiting VIN lookup. Goodbye!")
            break
         # perform VIN lookup
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
