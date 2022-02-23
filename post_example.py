import requests

out_data = {
   "name": "Kaylen Kang",
   "net_id": "kk431",
   "e-mail": "kaylen.kang@duke.edu"
}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.text)
