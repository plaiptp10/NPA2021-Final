import json
import requests
import time
requests.packages.urllib3.disable_warnings()

api_url = "https://10.0.15.108/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback62070147"

headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")

accesstoken = "NWUwYzNiZTQtN2Q4ZC00Mzg0LTkyNmEtMWI4YTM1MDFhYjFkNWQ3ZWZmNmEtODdj_P0A1_4a252141-f787-4173-a4c9-bde69c553a24"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl"
url = "https://webexapis.com/v1/messages"

def show_status():
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    if resp.status_code == 200:
        response_json = resp.json()
        if response_json["ietf-interfaces:interface"]["oper-status"] == "up":
            return "Loopback62070147 - Operational status is up"
        else:
            return "Loopback62070147 - Operational status is down"
    else:
        return "Loopback62070147 - Operational status is down"

headers_webex = {
    'Authorization': 'Bearer {}'.format(accesstoken),
    'Content-Type': 'application/json'
}

Params = {
            "roomId": room_id,
            "max": 1
        }

while 1:
    response = requests.get(url, headers=headers_webex, params=Params).json()
    if response["items"][0]["text"] == "62070147":
        postParams = {
            "roomId": room_id,
            "markdown": show_status()
        }
        response = requests.post(url, headers=headers_webex, json=postParams)
    time.sleep(1)