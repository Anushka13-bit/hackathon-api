import requests
import json

# Set the base URL for NOAA's Tides and Currents API
base_url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"

# Set the parameters for the API request
params = {
    "begin_date": "20250101",  # Start date in YYYYMMDD format
    "end_date": "20250101",    # End date in YYYYMMDD format
    "station": "9410230",      # Station ID (replace with your desired station)
    "product": "water_level",  # Product type (e.g., water_level, currents)
    "datum": "MLLW",           # Datum (e.g., MLLW, NAVD)
    "units": "metric",         # Units (e.g., metric, english)
    "time_zone": "gmt",        # Time zone (e.g., gmt, lst)
    "application": "python_script",  # Application name
    "format": "json"           # Response format
}

# Make the API request
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code}")
    

