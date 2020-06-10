import json
import os

def read_login_data():
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + '/data/login_data.json'
    with open(login_data_path, mode='r',encoding='utf-8') as f:
        jsonData = json.load(f)
        login_list = []
        for login_data in jsonData:
            login_list.append(tuple(login_data.values()))
    print(login_list)
    return login_list

# read_login_data()