import requests

data = {
    "name": "Tom",
    "age": "20"
}

response = requests.get("http://httpbin.org/get", params=data)
print(response.text)
