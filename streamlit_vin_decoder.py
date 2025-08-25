"""
VIN Decoder Streamlit App

This app allows users to input a Vehicle Identification Number (VIN) and fetch vehicle
information (year, make, model). The data is retrieved from the NHTSA (National Highway Traffic Safety 
Administration) VIN decoding API via the helper module `nhtsa_api_call.py`.
Useful for car dealerships who need quick VIN lookups.

Usage:
    streamlit run streamlit_vin_decoder.py

Author: Sharmil Nanjappa
Date: August 24, 2025
"""

import streamlit as st  # Import the Streamlit library for creating the web app
import nhtsa_api_call  # Import the API call function from external file
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the current directory
logo_img_file = os.path.join(BASE_DIR, "logo_image.png")
car_img_file = os.path.join(BASE_DIR, "car_image.png")

def get_vin(vin, username):
    """ 
    Decodes the VIN and displays model,make, model year.
    Validates VIN format and displays vehicle details or error message.
    """
    status_area = st.empty()
    col1, col2 = st.columns([1, 1])

    if len(vin) != 17:
        status_area.error(f"VIN must be exactly 17 characters long.")
        return
    elif not re.match(r'^[A-HJ-NPR-Z0-9]{17}$', vin):
        status_area.error(f"VIN must be alpha-numeric and cannot include letters I, O, Q.")
        return
    else:
        status_area.info("Decoding VIN...")

    try: 
        year, make, model = nhtsa_api_call.get_vehicle_info(vin)

        if not all([year, make, model]) or any([v is None for v in [year, make, model]]):
            status_area.warning(f"Incomplete vehicle data returned. {username.capitalize()}, please verify the VIN and try again.")
        else:
            status_area.success("VIN decoded successfully!")
            

            with col1:     
                st.image(car_img_file, use_container_width=True)

            with col2:
                st.write(f"Below are the vehicle details, {username.capitalize()}:")
                st.write("🔍 Vehicle Information")
                st.write(f"**Make:** {make}")
                st.write(f"**Model:** {model}")
                st.write(f"**Model Year:** {year}")

    except Exception as e:
        status_area.error(f"An error occurred while decoding the VIN: {e}")

def main():
    """
    Sets Streamlitcomponents for the page layout, handles user input, and calls get_vin function.
    """
    st.markdown("<h1 style='text-align: center;'>Vehicle VIN Decoder</h1>", unsafe_allow_html=True)
    st.write("*" * 50)
    st.markdown("<h5 style='text-align: center;'>🚗 Welcome to the Car Dealership VIN Lookup!</h5>", unsafe_allow_html=True)
    st.image(logo_img_file, use_container_width=True)
    st.markdown("---")

    with st.expander("ℹ️ About this app"):
        st.write("This app is designed to help car dealerships and automotive professionals effortlessly decode Vehicle Identification Numbers (VINs) to retrieve key vehicle details such as model,make and model year. By simply entering a 17-character VIN, users can access verified vehicle information. The data is fetched in real-time from the National Highway Traffic Safety Administration (NHTSA). Whether you're validating trade-ins, checking vehicle specs, or streamlining inventory intake, this tool delivers quick and reliable insights.")

    st.write("*" * 80)
    st.subheader("UserName")
    name = st.text_input("Enter your name", key="username")

    if name:
        st.success(f"👋 Hello, {name.capitalize()}!")
        st.markdown("---")
        st.markdown("Enter a **17-character VIN** below to decode the vehicle info.")

    vin = st.text_input("Enter VIN:", max_chars=17).strip().upper()
    if st.button("Decode VIN", use_container_width=True):
        if vin:
            get_vin(vin, name)
        else:
            st.error(f"❌ Please enter a VIN before fetching the vehicle information, {name.capitalize()}.")
    
    st.markdown("___")
    st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Car Dealership VIN Lookup", unsafe_allow_html=True) #Footer for the webpage

if __name__ == "__main__":
    main()
