"""1. declare a list call raw_tags
    2. convert this list to set using set() method
    3. write a condition to check if  "verified" is in the set
    4. declare a tuple called coordinates  
    5.Attempts to change coordinates[0] to 10 under the try block 
    and print the actual error message if it fails under the except block"""

raw_tags = ["premium", "active", "verified", "premium", "active"]
worked_tag = set(raw_tags)

if "verified" in worked_tag:
    print("Tag found")
else:
    print("Tag not found")


coordinates =  (6.5244, 3.3792)


try:
    coordinates[0] = 10
except TypeError as e: 
    print(f"Error: {e}")

