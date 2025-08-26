"""
cli_demo.py

Author: Eugenia Tate
Date: August 24, 2025

A simple command-line application for a car dealership that allows users 
to look up vehicle information (year, make, and model) by VIN number. 
The app also lets a user view top 3 looked up vehicle makes.
The data is retrieved from the NHTSA (National Highway Traffic Safety 
Administration) VIN decoding API via the helper module `nhtsa_api_call.py`.

Usage:
    python cli_demo.py
"""
import nhtsa_api_call, re, csv, os
import pandas as pd

TOP3 = 3

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

def save_vehicle(year, make, model, filename = "vin_lookup_history.csv"):
    """Append VIN lookup result to a CSV file."""
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            # add first row
            writer.writerow(["year", "make", "model"])  
        writer.writerow([year, make, model])

def display_top3(filename = "vin_lookup_history.csv"):
    """Show top 3 car makes by lookup frequency"""
    # if file does not exist then there is no history yet
    if not os.path.isfile(filename):
        print("\nNo VIN lookup history found. Please look up some VINs first.\n")
        return
    # create a dataframe using file data 
    df = pd.read_csv(filename)
    # save number each make appears in the log as a series
    counts = df['make'].value_counts()
    # file exists but no data has been added yet
    if len(counts) == 0:
        print("\n No data in the log yet.\n")
        return
    # if there are  fewer than 3 data entries in the log then the program will 
    # at least display 1 or 2 most looked up makes
    if len(counts) < TOP3:
        print(f"\nNot enough data for displaying top 3. Showing top {len(counts)} instead:\n")
        top_makes = counts.head(len(counts))
    else:
        print(f"\n Top {TOP3} Car Makes from Lookups:\n")
        top_makes = counts.head(TOP3)

    for make, count in top_makes.items():
        print(f"   {make}: {count} lookups")
    # an empty line print to space out CLI prompts
    print()  

def main():
    """
    Run the command-line VIN lookup loop.

    Prompts the user for a VIN number, calls the NHTSA API,
    and prints out the vehicle information if found.
    Enter '0' to exit.
    """
    print("🚗 Welcome to the Car Dealership VIN Lookup!\n")
   
    while True:
        print("Choose an option from the menu:")
        print("1. Lookup a VIN")
        print("2. Show Top 3 Most Looked-up Makes")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()
        
        # exit condition gets checked first
        if choice == "0":
            print("👋 You chose to exit VIN lookup. Goodbye!")
            break
        # user selected to add a VIN
        elif choice == "1": 
            vin = input("Please enter a valid VIN or 0 (zero) to exit: \n").strip()
            if vin == "0":
                continue
            # check if vin is valid, and if not print error message
            if not is_valid_vin(vin): 
                print("Invalid VIN format. Must be 17 letters/numbers (no I, O, Q). Try again.\n")
                continue
            # vin is valid, perform VIN lookup
            else:
                year, make, model = nhtsa_api_call.get_vehicle_info(vin)
                if year and make and model:
                    print(f"✅ VIN {vin}")
                    print(f"   Year: {year}")
                    print(f"   Make: {make}")
                    print(f"   Model: {model}")
                    save_vehicle(year, make, model)     #save the data in the lookup history file
                else:
                    print(f"❌ VIN {vin} not found in database. Try again.")
        # user selected to view top3 vehicle makes 
        elif choice == "2":
            display_top3()
        # user entered something other than 1,2 or 0
        else:
            print("Invalid option. Please choose 1, 2, or 0.\n")

if __name__ == "__main__":
    main()
