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


square = [value**2 for value in range(1,11)]
print(square)


# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


#Tuple
dimensions = (200, 50)
for i in dimensions:
    print(i)

# to print the index of a tuple
print(dimensions.index(50))
    


#If statement
car = 'subaru'
print(car == "subaru")

print(car == "audi")


# Diction

alien_0 = {"color": "green", "points" : 5}

print("\n" + alien_0['color'])
# accessing a dictionary using get() method
print(alien_0.get('poin', "doesn't exixt"))


alien_0["X_cordinate"] = True
alien_0["Z_cordinate"] = True
alien_0["Y_cordinate"] = False
print(f"\n  {alien_0}") 

#deleting a key-value in a dic
del alien_0["color"]
print(f"\n  {alien_0}") 

# Looping Through a Dictionary’s Keys using keys() method
for i in alien_0.keys():
    print(i)

print()

#OR

for i in alien_0:
    print(i)

print()
# Looping Through a Dictionary’s Keys in a Particular Order
for i in sorted(alien_0):
    print(i)

print()
# Looping Through All Values in a Dictionary using value() method
for i in alien_0.values():
    print(i)
print()

#The set() method prevent duplicate
for i in set(alien_0.values()):
    print(i)

# A List of Dictionaries
aliens = []
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] =15

for alien in aliens[:5]:
    print(alien)


# A List in a Dictionary
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }

for liz in pizza["toppings"]:
    print(liz)



users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

# A Dictionary in a Dictionary
# Summary of the RuleUse .items() if you want both the key and value at the same time using two variables (for k, v in dict.items()).
# Drop .items() if you only want the key using one variable (for k in dict).

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print()

    #USER INPUT 
name = input("Please enter your name: ")
print(f"Hello, {name}")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"\nHello, {name}")

# Using int() to Accept Numerical Input
age = input("How old are? ")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you' re a little older.")


# while Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
    if message != 'quit':
        print(message)


