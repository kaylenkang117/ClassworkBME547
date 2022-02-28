import requests

server = "http://127.0.0.1:5000"
# r = requests.get(server)

# r = requests.get(server + "/info")

# out_data = {"name": "Kaylen", "hdl_results": 65}
# r = requests.post(server + "/hdl_check", json=out_data)

out_data = {"a": 3, "b": 5}
r = requests.post(server + "/add", json=out_data)
print(r.status_code)
print(r.text)
a = r.json()
print(a[0])
