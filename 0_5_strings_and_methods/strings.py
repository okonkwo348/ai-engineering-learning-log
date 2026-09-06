""" 1. declare the variable raw_input
    2. removine the leading and trailing whitespaces by using the method .strip() and assign it to a new variable call new_input
    3. convert to lower case using the method .lower()
    4. use conditional statement to be sure it worked by using .endswith("gmail.com")
    5. if the condition is true or false print the respective messages "Valid Gmail address" or "Not a Gmail address" accordingly """

    
raw_input = "  EMMANUEL@YAHOO.COM  "

new_input = raw_input.lower().strip()

if new_input.endswith("gmail.com"):
    print("Valid Gmail address")
else:
    print("Not a Gmail address")

print(new_input)



"""1. declare a variabe api_key_display
    2. extract the first 6 characters by slicing through the slice [0:6]
    3. extract the last 4 characters by slicing through the slice [-4:0]
    4. print "Key preview: sk-ant...z789"""

api_key_display = "sk-ant-abc123xyz789"
first_six = api_key_display[0:6]
last_four = api_key_display[-4:]
print(f"Key preview: {first_six}...{last_four}")
print(api_key_display[-4:0])
print(api_key_display[-4:])