import requests

# Define the base URL for the BRAILS API
base_url = "https://brails.simcenter.designsafe-ci.org/api"

# Define the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": "Token [YOUR_API_TOKEN]"
}

# Define the parameters for the API request
params = {
    "sim_id": "[YOUR_SIMULATION_ID]",
    "metric": "[YOUR_METRIC]",
    "start": "[START_DATE]",
    "end": "[END_DATE]"
}

# Send the API request
response = requests.get(f"{base_url}/metrics/", headers=headers, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()
    # Do something with the data
    print(data)
else:
    # Handle the error
    print(f"Request failed with status code {response.status_code}")
    
    
    
### Note that you will need to replace [YOUR_API_TOKEN], [YOUR_SIMULATION_ID], [YOUR_METRIC], [START_DATE], and [END_DATE] with the appropriate values for your specific use case. Also, you will need to install the requests library in order to run this code.
