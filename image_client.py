from tkinter import filedialog
import base64
import requests

server = "http://vcm-21170.vm.duke.edu"


def upload_image_driver():
    filename = get_filename_image()
    b64_string = convert_file_to_b64_string(filename)
    answer = send_b64_string_to_server(b64_string)


def convert_file_to_b64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding="utf-8")
    return b64_string


def send_b64_string_to_server(b64_string):
    out_json = {"image": b64_string, "net_id": "kk431", "id_no": 5}
    r = requests.post(server + "/add_image", json=out_json)
    print(r.status_code)
    print(r.text)
    return r.text


def get_filename_image():
    filename = filedialog.askopenfilename()
    return filename


def download_image():
    r = requests.get(server + "get_image/kk431/5")
    if r.status_code != 200:
        print(r.text)
        return False
    else:
        save_base64_string_to_file(r.text, "new_file.jpg")


def save_base64_string_to_file(b64_str, filename):
    image_bytes = base64.b64decode(b64_str)
    with open(filename, "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == '__main__':
    upload_image_driver()
    download_image()
