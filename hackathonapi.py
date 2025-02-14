import requests
import json

# Set the base URL for NOAA's Tides and Currents API
base_url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
begindate = input("Enter the Date (YYYYMMDD): ")  # Keep it as a string
station = input("Enter the station ID: ")  # Keep it as a string

# Set the parameters for the API request
params = {
    "begin_date": begindate,  # Start date in YYYYMMDD format
    "end_date": begindate,    # End date in YYYYMMDD format
    "station": station,      # Station ID
    "product": "water_level",  # Product type (e.g., water_level, currents)
    "datum": "MLLW",           # Datum
    "units": "metric",         # Units
    "time_zone": "gmt",        # Time zone
    "application": "python_script",
    "format": "json"
}

# Make the API request
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()  # ✅ Use response.json() instead of json.loads(response.text)
    
    print(json.dumps(data, indent=4))  # Pretty print JSON

    # Extract water level values
    if "data" in data:  # ✅ Check if "data" key exists in JSON
        parsed_data = data["data"]  # Access the list inside "data"
        
        vvalues = [item["v"] for item in parsed_data]  # Extract "v" values
        svalues = [item["s"] for item in parsed_data]  # Extract "s" values
        
        print("Water Level (v):", vvalues)
        print("Quality (s):", svalues)
    else:
        print("No data available for the given station and date.")
else:
    print(f"Error: {response.status_code}, Response: {response.text}")


