# Car Dealership VIN Lookup App

![alt text](logo_image.png)

## 📌 Overview
This is a simple app for a car dealership that allows users to look up vehicle information (year, make, and model) by entering a VIN number.  

Additionally, the app keeps track of search frequency and lets users view the **Top 3 most looked-up vehicle makes**.  

All vehicle data is retrieved from the [NHTSA (National Highway Traffic Safety Administration) VIN decoding API](https://vpic.nhtsa.dot.gov/api/), accessed via the helper module [`nhtsa_api_call.py`](./nhtsa_api_call.py).

---

## ⚙️ Features
- 🔍 Lookup vehicle details (year, make, model) by VIN number 
- 📊 View the **Top 3 most searched vehicle makes**  
- 🌐 Fetches real-time data from the **NHTSA VIN API**  
- 🖥️ Simple and interactive command-line interface  

---
## 📦 Python Version

Tested on: Python 3.10

---
## 🚀 Getting Started

**How to run locally**

1. Clone the Repository
git clone https://github.com/averyestopinal/AIPI503PROJECT
cd AIPI503PROJECT

2. Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

3. Install Dependencies
This app uses only standard Python libraries (no external dependencies).However, make sure you are running Python 3.7+.
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run streamlit_app.py

**How to Run cli_demo.py**
This is a simple command-line version of the VIN decoder. Make sure your terminal is in the same directory as cli_demo.py.

python cli_demo.py

**Link to the Hugging Faces Space**


---

🧩 Project Structure
.
├── streamlit_app.py                # Entry point for the Streamlit application
├── cli_demo.py                     # Command-line interface version of the VIN decoder
├── nhtsa_api_call.py               # Helper module for API requests
├── car_image.png                   # Image file used in the Streamlit application
├── logo_image.py                   # Logo image file used in the Streamlit application
├── README.md                       # Project documentation
├── requirements.txt                # Python Dependencies 

---
📡 API Reference
The app uses the NHTSA VIN Decoder API which provides vehicle details when supplied with a VIN number.

Example request: https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/<VIN>?format=json

---
🙌 Credits
NHTSA Vehicle API
Streamlit
Hugging Face Spaces

---
👨‍💻 Author
Developed as part of a learning project by
1. Avery Estopinal
2. Sharmil K
3. Eugenia Tate
4. Jaideep Aher
---

Contributions are welcome!
Feel free to fork and submit a pull request 🚀
