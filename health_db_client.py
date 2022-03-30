import requests

server = "http://127.0.0.1:5000"


def upload_patient_data_to_server(patient_name, patient_id,
                                  patient_blood_type):
    new_patient = {"name": patient_name,
                   "id": patient_id,
                   "blood_type": patient_blood_type}
    r = requests.post(server + "/add_patient", json=new_patient)
    return r.text

# r = requests.get(server + "/get_results/101")
# print(r.status_code)
# print(r.text)
