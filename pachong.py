import requests

r = requests.get(url='http://www.baidu.com')

print(r.status_code)

print(r.content.decode('utf-8'))



