£ While Loop
x = 1
while 11 > x:
    if x % 2 == 0:
        x += 1
        continue

    if x == 9:
        break

    print(x)
    x += 1


£ Request

import  requests

response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.json())
# print(response.json().get("current_user_url"))

data = response.json()
print(data)
print(data.get("current_user_url"))
