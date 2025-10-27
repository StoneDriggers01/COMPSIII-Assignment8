# Write your code here
# Import the requests library to handle HTTP requests
import requests

# Define a class to interact with the JSONPlaceholder API
class JSONPlaceholder:
    # Constructor method to initialize the base URL for API requests
    def __init__(self, base_url = "https://jsonplaceholder.typicode.com/posts"):
        self.base_url = base_url  # Default endpoint for posts

    # Method to perform a GET request to retrieve data from the API
    def get_request(self):
        response = requests.get(self.base_url)  # Send GET request to the base URL
        return {
            "status_code": response.status_code,  # HTTP status code (e.g., 200 OK)
            "headers": dict(response.headers),    # Response headers as a dictionary
            "content": response.content[:500]     # First 500 bytes of the response body
        }

    # Method to perform a POST request to create a new resource
    def post_request(self, data):
        response = requests.post(self.base_url, data=data)  # Send POST request with data payload
        return {
            "status_code": response.status_code,  # HTTP status code (e.g., 201 Created)
            "headers": dict(response.headers),    # Response headers
            "content": response.content[:500]     # First 500 bytes of the response body
        }

    # Method to perform a PUT request to update an existing resource
    def update_user(self, userId, title, body):
        url = f"{self.base_url}/{userId}"  # Construct URL for the specific post/user
        data = {
            "title": title,  # New title for the post
            "body": body     # New body content for the post
        }
        response = requests.put(url, data)  # Send PUT request to update the resource
        return {
            "status_code": response.status_code,  # HTTP status code (e.g., 200 OK)
            "headers": dict(response.headers),    # Response headers
            "content": response.content[:500]     # First 500 bytes of the response body
        }

    # Method to perform a DELETE request to remove a resource
    def delete_user(self, userId):
        url = f"{self.base_url}/{userId}"  # Construct URL for the specific post/user
        response = requests.delete(url)    # Send DELETE request to remove the resource
        return {
            "status_code": response.status_code  # HTTP status code (e.g., 200 OK or 204 No Content)
        }