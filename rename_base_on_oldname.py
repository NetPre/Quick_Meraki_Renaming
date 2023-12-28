import requests
import json
import csv



def get_inventory():
    url = "https://api.meraki.com/api/v1/organizations/1496803/devices"

    payload = {}
    headers = {
    'Authorization': 'Bearer 449fa52401cfd25624456470d8935d09a21fcc4a'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def get_serial_num(name,inventory):
    for device in inventory:
        if device['name'] == name:
            return device['serial'] 

def update_device_name(serial_um, new_name):
    url = "https://api.meraki.com/api/v1/devices/"+serial_um
    payload = json.dumps({
    "name": new_name
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 449fa52401cfd25624456470d8935d09a21fcc4a'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response)

if __name__ == '__main__':
    inventory = get_inventory()
    with open('old_new_names.csv', 'r') as f:
        header = f.readline()
        reader = csv.reader(f)
        for row in reader:
            old_name = row[0]
            new_name = row[1]
            serial_num = get_serial_num(old_name,inventory)
            update_device_name(serial_num, new_name)
            print(serial_num)




