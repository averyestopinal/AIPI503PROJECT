"""
VIN Decoder Streamlit App

This app allows users to input a Vehicle Identification Number (VIN) and fetch vehicle
information (year, make, model). The data is retrieved from the NHTSA (National Highway Traffic Safety 
Administration) VIN decoding API via the helper module `nhtsa_api_call.py`.
Useful for car dealerships who need quick VIN lookups.

Usage:
    streamlit run streamlit_vin_decoder.py

Author: Sharmil Nanjappa
Date: August 25, 2025
"""

import streamlit as st  # Import the Streamlit library for creating the web app
import nhtsa_api_call  # Import the API call function from external file
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the current directory
logo_img_file = os.path.join(BASE_DIR, "logo_image.png")
car_img_file = os.path.join(BASE_DIR, "car_image.png")

# Check if the 'make_history' key is already in Streamlit's session state
if "make_history" not in st.session_state:
    # If not, initialize it as an empty list to store searched vehicle makes
    st.session_state.make_history = []

# Define a function to track the vehicle make each time a VIN is decoded
def track_make(make):
    """
    Store the searched make in session state for pie chart stats.
    """
    # Proceed only if a valid make value is provided
    if make:
        # Capitalize and append the make to the session history list
        st.session_state.make_history.append(make.title())
        # Optional: Display the current list of searched makes in the sidebar for debugging
        #st.sidebar.write("Debug – History:", st.session_state.make_history)


def show_top_3_makes():
    """
Display a pie chart of the top 3 most searched vehicle makes.

    if not st.session_state.make_history:
            st.warning("No vehicle makes have been searched yet.")
            return
"""
    counts = Counter(st.session_state.make_history)
    top_3 = counts.most_common(3)                       # A tuple to hold values: (make_name, count)


    labels = [item[0].upper() for item in top_3]        # Label for the vehicle make, displayed in upper case for each slice of the pie chart
    sizes = [item[1] for item in top_3]                 # Count of each make in the Top3. Used to determine how large each slice of the pie chart is.
    colors = ['#4682B4', '#1E3F66', '#0B1F3A']    # Blue, dark blue, night blue   : colors of pie chart slices
    with st.container():
        
        st.markdown("""
                <div style="
                    max-width: 700px;
                    margin: 0 auto;
                    padding: 12px 24px;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    text-align: center;
                    font-size: 16px;
                    font-weight: 500;
                ">
                    Pie chart displaying the Top 3 Vehicles<br>
                    searched based on their Make
                </div>
            """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(3,3), dpi=150)
    
    # Draw pie chart with borders and percentage labels
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,          # autopct shows % and startangle starts the first slice from the top
         wedgeprops={'edgecolor': 'white', 'linewidth': 1}
        )
              
    ax.axis('equal')                                                    # Forces the chart to be a perfect circle

    # Style text and labels
    for text in texts:                                                  #The labels of each pie slice
        text.set_fontsize(5)
        text.set_color('#000')                                          # text color: Black
        text.set_fontweight('semibold')

    for autotext in autotexts:                                          #The percentages shown on each slice
        autotext.set_fontsize(5)
        autotext.set_color('#fff')                                       # text color: White
    
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

def get_vin(vin):
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
            status_area.warning(f"Incomplete vehicle data returned. Please verify the VIN and try again.")
        else:
            status_area.success("VIN decoded successfully!")
            
            track_make(make)
            with col1:     
                st.image(car_img_file, use_container_width=True)

            with col2:
                st.write(f"Below are the vehicle details :")
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

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(logo_img_file, width=180)
    with col2:
            st.markdown("""
                <div style='text-align: left; margin-top: 30px;'>
                    <h1 style='font-size: 38px;'>Vehicle VIN Decoder</h1>
                </div>
            """, unsafe_allow_html=True)
    st.write("*" * 50)

    st.markdown("<h5 style='text-align: center;'>Welcome to the Car Dealership VIN Lookup!</h5>", unsafe_allow_html=True)
    
    
    with st.expander("ℹ️ About this app"):
        st.write("This app is designed to help car dealerships and automotive professionals effortlessly decode Vehicle Identification Numbers (VINs) to retrieve key vehicle details such as model,make and model year. By simply entering a 17-character VIN, users can access verified vehicle information. The data is fetched in real-time from the National Highway Traffic Safety Administration (NHTSA). Whether you're validating trade-ins, checking vehicle specs, or streamlining inventory intake, this tool delivers quick and reliable insights.")

 
    
    st.markdown("Enter a **17-character VIN** below to decode the vehicle info.")

    vin = st.text_input("Enter VIN:", max_chars=17).strip().upper()
    if st.button("Decode VIN", use_container_width=True):
        if vin:
            get_vin(vin)
        else:
            st.error(f"❌ Please enter a VIN before fetching the vehicle information.")
    
     # Show top 3 searched makes
    st.markdown("---")
    if st.button("Top 3 Makes Searched", use_container_width=True):
        show_top_3_makes()
    
    st.markdown("___")
    st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Car Dealership VIN Lookup", unsafe_allow_html=True) #Footer for the webpage

   


if __name__ == "__main__":
    main()
