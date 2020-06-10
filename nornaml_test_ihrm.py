import requests

url = "http://ihrm-test.itheima.net/api/sys/login"
data = {"username":"13800000002","password":"123456"}
response = requests.post(url=url, data=data)
