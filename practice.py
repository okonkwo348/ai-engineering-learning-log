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


magicians = ["alice", "david", "caroline"]
for guys in magicians:
    print(f"{guys.title()}, that was a great trick!")
    # print(f"I can't wait to see your next, {guys.title()}.\n")
print(f"I can't wait to see your next trick, {guys.title()}.\n")


#Using the range() Function
for value in range(0,5):
    print(value)


#Using range() to Make a List of Numbers
num = list(range(1,11,2))
print(num)

squares = []
for value in range(1, 12):
    squares.append(value **2)
print(squares)

# Simple Statistics with a List of Numbers
digit = []
for num in range(0,10):
    digit.append(num)

print(digit)
print(max(digit))
print(min(digit))
print(sum(digit))
