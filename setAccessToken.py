import requests
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()
# Your credentials and endpoint
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
refresh_token = os.getenv('REFRESH_TOKEN')
token_url = 'https://oauth2.googleapis.com/token'  # Example for Google OAuth

# Prepare the request payload
payload = {
    'grant_type': 'refresh_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token
}

# Make the POST request to get a new access token
response = requests.post(token_url, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    response_data = response.json()
    access_token = response_data['access_token']
else:
    print('Error:', response.status_code, response.text)
