import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content #Raw Json data

    def load_json(self):
        body = self.get_response_body()
        return json.loads(body) #Converts JSON string to python dict