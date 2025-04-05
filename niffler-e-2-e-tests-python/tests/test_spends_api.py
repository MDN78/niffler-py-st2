from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient


def test_auth(auth_api_token):
    print(auth_api_token)



# import requests
# import json

# url = "http://gateway.niffler.dc:8090/api/categories/add"
#
# payload = json.dumps({
#   "id": "e6c1702d-41ab-492c-b13c-fb83a4042bd7",
#   "name": "test",
#   "username": "stas",
#   "archived": True
# })
# headers = {
#   'accept': '*/*',
#   'Authorization': 'Bearer eyJraWQiOiJjYzFmZjY1MC0zMTQxLTQ2M2MtYjgxZC1jNGRiNTIxY2Y2ZjkiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzdGFzIiwiYXVkIjoiY2xpZW50IiwibmJmIjoxNzQzODY1NTkwLCJzY29wZSI6WyJvcGVuaWQiXSwiaXNzIjoiaHR0cDovL2F1dGgubmlmZmxlci5kYzo5MDAwIiwiZXhwIjoxNzQzODcyNzkwLCJpYXQiOjE3NDM4NjU1OTAsImp0aSI6ImM3YTE1OWU0LTFhY2EtNGE0My1hNzY0LWEwYzU3YWZkODY0MCJ9.dVnyFFPnX4BQAJAqDRKWrWuJv9teH9qi7daAIVfDMIJHEVTjpLWPGscslOWAtPFUshuoF21ytU6sCSmb2LeDO1keIX3aYQkHOheIHMW_I5dPfHJZFxsXQ5P-xVLgKmzEMeBSi2DUzdYNH_Kvixilol1wpGHO7yuZQPb5Qk33DKrQkPOfUZulQsEi-LyxjEEomZHUQFDk4m2HLr3iwTZ0jQhp-di8fQBftWSycM3clv4JJVRVdwryZOO-3ZBFAQ41gwbUaayDlAaF6j_L5hafsR5QVkpdkH3jcC-pBWwl8IIeyQczswAPa4R0B-yf3NDB-zM9GykNTLMgp4fxL8O_kA',
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)



#
#
# def test_add_spend(auth_api_token):
#     cat = CategoryHttpClient("http://gateway.niffler.dc:8090", auth_api_token).add_category()



# import requests
# import json
#
# url = "http://gateway.niffler.dc:8090/api/spends/add"
#
# payload = json.dumps({
#   "amount": "222",
#   "description": "QA.GURU Python Advanced 1",
#   "currency": "RUB",
#   "spendDate": "2025-02-12T17:51:25.301Z",
#   "category": {
#     "name": "school"
#   }
# })
# headers = {
#   'Accept': 'application/json',
#   'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#   'Authorization': 'Bearer eyJraWQiOiI4ZjBiNjg0My01ZmYzLTQxZDYtYjA4ZS03MDg0ZWRlYjBkNWMiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzdGFzIiwiYXVkIjoiY2xpZW50IiwiYXpwIjoiY2xpZW50IiwiYXV0aF90aW1lIjoxNzM5MzgxNDI5LCJpc3MiOiJodHRwOi8vYXV0aC5uaWZmbGVyLmRjOjkwMDAiLCJleHAiOjE3MzkzODMyMjksImlhdCI6MTczOTM4MTQyOSwianRpIjoiN2Y3MTY1MjQtMGIzYy00ZDA1LTk3OTgtMGY3OTA3NmRjYWNhIiwic2lkIjoiaWpJMVNxdGxseDBpdU1mQ0pzaTZueEFDTWQ4TUJubFhGRy1mYWh6TGs1USJ9.j90Mu8syQ-GOBbhEvqlj17-8JnE9lV1dxW51OfsLd6Zqme-jJPwpPVqP6ITbcVAIuEUdf_xGLT6ClaITr58hib-bm-3NPz_GWc2MP2QiWs101rZ3oIEp2fJHqYWiWrxHe08jQUs6n5SACtyABfnBBuLzYNrGYSnhZznYYJVF5Fxms-CElXetWE7tm2jd_blLy4zUQr5YL4e92mPgQ_92_J4waRkaYIwS-lrTq2Ctil1ajB23voKMFh1w5nCNFGW3RRL6-vQg_rMaC2rMrb5VX6ryvEG9rLUzXTrJCIeE4Q3AZUUYTqG00pPzoeJlAIleWoaoLuyajSgx0nAPkJXNdw',
#   'Connection': 'keep-alive',
#   'Content-Type': 'application/json',
#   'Cookie': 'JSESSIONID=37911390ABA770ED3BBE39BD019A88D8',
#   'Origin': 'http://frontend.niffler.dc',
#   'Referer': 'http://frontend.niffler.dc/',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
