import requests
url = "http://localhost:8080/"
for i in range(0,20):
    headers = {
        'cache-control': "no-cache",
        'postman-token': "bd13fae3-0fe7-f7c2-5240-06748e6f2b8e"
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    if i%6==5:
        print("\n\n")