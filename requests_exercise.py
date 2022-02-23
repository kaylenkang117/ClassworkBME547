import requests

url = "http://vcm-7631.vm.duke.edu:5002"

r = requests.get(url + "/get_patients/kk431")
print(r.text)

r = requests.get(url + "/get_blood_type/M6")
print(r.text)

r = requests.get(url + "/get_blood_type/F6")
print(r.text)


answer = {"Name": "kk431", "Match": "Yes"}

r = requests.post(url + "/match_check", json=answer)
print(r.text)
