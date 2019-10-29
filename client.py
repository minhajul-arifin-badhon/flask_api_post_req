import requests

url = "http://127.0.0.1:5000/create_event"
json_param = {
    "event_name": "Event One",
    "event_desc": "This is a test event",
    "event_note": "Event related note",
}

response = requests.post(url = url, json = json_param)
json_data = response.json()

print(json_data['event_name'])
