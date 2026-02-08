# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    
    # Remove the trailing '&' if params exist
    if params.endswith("&"):
        params = params[:-1]

    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params

    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        # Return the response as JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Catch network-related errors
        print("Network exception occurred:", e)
        return None


def post_review(data_dict):
    """
    Sends a POST request to add a new dealer review.
    
    data_dict: Dictionary containing all review fields required by the backend.
    """
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())  # Optional: for debugging
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Network exception occurred:", e)
        return None
    