import requests
import json
import csv



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
    with open('old_new_names.csv', 'r') as f:
        header = f.readline()
        reader = csv.reader(f)
        for row in reader:
            new_name = row[1]
            serial_num = row[2]
            update_device_name(serial_num, new_name)
            print(serial_num)




