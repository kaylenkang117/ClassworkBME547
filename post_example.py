import requests


message = {
    "user": "kaylenkang117",
    "message": "Hi what's up"
}

# r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=message)


r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Jimmy")
print(r.text)