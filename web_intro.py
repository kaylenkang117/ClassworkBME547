import requests

r = requests.get(
    "https://api.github.com/repos/kaylenkang117/ClassworkBME547/branches")


print(r)
print(type(r))
print("Status code = {}".format(r.status_code))
print("Text = {}".format(r.text))


if r.status_code != 200:
    print("THere was a problem")
    print(r.text)
    exit()

answer = r.json()

for branch in answer:
    print(branch["name"])


print("done")
