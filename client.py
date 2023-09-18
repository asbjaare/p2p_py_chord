import requests

# Define the URL of app2 (the client-side app)
app2_url = "http://172.21.21.183:65000/item/12"  # Replace with the actual IP and port

# Make a GET request to app2
response = requests.put(app2_url)
response = requests.get(app2_url)

# Check the response
if response.status_code == 200:
    print("Communication successful!")
    print("Response from App 2:")
    print(response.text)
else:
    print("Communication failed. Status code:", response.status_code)
