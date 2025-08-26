# Car Dealership VIN Lookup App

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

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/averyestopinal/AIPI503PROJECT

2. Install Dependencies
This app uses only standard Python libraries (no external dependencies).
However, make sure you are running Python 3.7+.

3. Run the Application
bash
Copy code
python main.py
🧩 Project Structure
bash
Copy code
.
├── main.py              # Entry point for the application
├── nhtsa_api_call.py    # Helper module for API requests
├── README.md            # Project documentation
📡 API Reference
The app uses the NHTSA VIN Decoder API which provides vehicle details when supplied with a VIN number.

Example request:
ruby
Copy code
https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/<VIN>?format=json


👨‍💻 Author
Developed as part of a learning project by
1. Avery Estopinal
2. Sharmil K.
3. Eugenia Tate
4. Jaideep Aher

Contributions are welcome!
Feel free to fork and submit a pull request 🚀
