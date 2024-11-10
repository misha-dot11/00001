import requests


for a in range(11):
    print(a)

text = requests.get("https://github.com/misha-dot11/00001").text
print(text)