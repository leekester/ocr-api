import requests
from os import listdir
from os.path import isfile, join
import time

start = time.time()

image = "/app/hello.jpg"
url = 'http://localhost:5000/ocr'  # Replace with your IP or domain name

model = 'all'

if model != "":
    headers = {
        "model": model,
    }
else:
    headers = {}

file = {'file': open(image, 'rb')}

try:
    response = requests.post(url, headers=headers, files=file)
    if response.status_code == 200:
        print("File uploaded successfully.")
        print(response.json())
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

end = time.time()
print('Elapsed time in seconds')
print(end - start)
