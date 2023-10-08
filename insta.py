from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace ACCESS_TOKEN with your access token
access_token = 'IGQWRPT0J4ZADRtcjdVT2ZAyMjZAydDZAUWTAwV0hXdUl3YV9pQXRnRlVVRDk5X0hNSEVDRXQtUWhsSnk1SDl6bWdzdXJtdmoxMnJTX09fVHctMTdtNmRCTWhHU1NJdWlzTkZACZAlFvU2xiSkd3MmVJNFpOQ3VtZAzRGN00ZD'

@app.route('/')
def index():
    return 'Redirection is Successful'

@app.route('/profile_data')
def get_profile_data():
    # Get user ID
    response = requests.get(f'https://graph.instagram.com/me?fields=id&access_token={access_token}')
    user_id = response.json()['id']

    # Get profile data
    response = requests.get(f'https://graph.instagram.com/{user_id}?fields=id,username,account_type,media_count,followers_count&access_token={access_token}')
    
    # Check if redirection is successful or not
    if response.status_code == 200:
        profile_data = response.json()
        # Return profile data as JSON and session message
        return jsonify(profile_data) 
    else:
        return 'Redirection not successful'

if __name__ == '__main__':
    app.run()