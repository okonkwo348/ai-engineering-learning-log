# resources = [
#   {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
#   {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
#   {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
# ]
import json
def load_resources():
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    

resources = load_resources()

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

def add_resouce(ID, name, category, total, available):
    new ={"id": ID, "name": name, "category": category, "total": total, "available": available}
    global resources
    for item in resources:
        if item["id"] == new["id"]:
            return "ID of this resource already exist"
       
    resources.append(new)
    return resources

def list_resources():
    for item in resources:
      print(item)

def borrow(fellow_id, resources_id, name, category, quantity):
    
    if fellow_id in fellows.keys():
        global resources
        for item in resources:
            if item["id"] == resources_id:
                if quantity <= 0:
                    return "Invalid quantity"

                if  quantity > item["available"]:
                    return f"Quantity not available: {item["available"]} avaliable"

                item["available"] -= quantity
                return f" {fellow_id} borrows {quantity} {item["name"]} - available {item["name"]} units = {item['available']}"
                    
        return "Resource ID not found"
    else:
        return "fellow ID notfound"
    return "rejected without changing stock"



def return_resource(fellow_id, resources_id, name, category, quantity):
        if fellow_id in fellows.keys():
            global resources
            for item in resources:
                if item["id"] == resources_id:
                    if quantity > item["total"] - item["available"]:
                        return f"{fellow_id} returns {quantity} {name} — rejected without changing stock"

                    item["available"] += quantity
                    return f"{fellow_id} returns {quantity} {name} — available {name} units = {item['available']}"

            return "Resource ID not found"
        else:
            return "fellow ID not found"
    
        return "rejected without changing stock"

def report():
    global resources
    total = 0
    borrowed = 0
    available = 0
    highest_borrowed = 0
    lowest_stock = resources[0]
    sentence_lowest_stock = ""
    sentence_highest_borrowed = ""
    for item in resources:
        total += item["total"]
        available += item["available"]
        borrowed_item= item["total"] - item["available"]
        borrowed += borrowed_item
        if item["available"] < lowest_stock["available"]:
            lowest_stock = item
            sentence_lowest_stock += f"{item["name"]} low stock ({lowest_stock["available"]})"
        
        if borrowed_item > highest_borrowed:
            highest_borrowed = borrowed_item
            sentence_highest_borrowed += f"{item["name"]} is most borrowed ({highest_borrowed})"


    print(f" Generate the report — overall units {total}, available {available}, borrowed {borrowed}, {sentence_lowest_stock}; {sentence_highest_borrowed}.")
        







def search_resourse(name):
    global resources
    for item in resources:
        if item["name"].lower() == name.lower():
            return f"find {item["name"].title()}, ignoring case"
    return "Resource not found"

def save_task():
    with open("file.json", "w") as file:
        json.dump(resources, file, indent=2)



state = True
while state:
    print("Welcome to Resource Management App!")
    input_var = input(""": Enter: 
                        'add' to add resources, 
                        'list' to list all resources, 
                        'borrow' to borrow a resource, 
                        'return' to return a resource, 
                        'search' to search for a resource, 
                        'report' to get summry of resource management,
                        'exit' to quit
     > """)
    response = input_var.lower().strip()

    if response == "add": 
        Id = input("Enter an Id eg..R001, R002, R003, R004> ").title()
        name = input("Enter an Item you need eg..car, laptop, shoe, shirt> ").title()
        category = input("Enter the category of item you want eg..electronics, vehicle, cloth, footware> ").title()

        try:
             total = int(input("Enter the total no of items> "))
             available = total
        except ValueError:
            print("Invalid total: integers are accepted only")

        new = add_resouce(Id, name, category, total, available)
        save_task()


    elif response == "list":
        list_resources()

    elif response == "borrow":
        fellow_id = input("Enter your student no eg..F001, F002, F003> ")
        resource_id = input("Enter your student no eg..R001, R002, R003> ")
        item_name = input("Enter the item name> ")
        category = input("Enter the catergory eg.. cloth, electronic")

        try:
            quantity = int(input("Enter the quantity to be borrowed eg..1, 2, 3> "))
        except ValueError:
            print("Invalid quantity: integer accepted only")
        print(borrow(fellow_id, resource_id, item_name, category, quantity))
         

    elif response == "return":
        fellow_id = input("Enter your student no eg..F001, F002, F003> ")
        resource_id = input("Enter your student no eg..R001, R002, R003> ")
        item_name = input("Enter the item name> ")
        category = input("Enter the catergory eg.. cloth, electronic")

        try:
            quantity = int(input("Enter the quantity to be returned eg..1, 2, 3> "))
        except ValueError:
            print("Invalid quantity: integer accepted only")
        print(return_resource(fellow_id, resource_id, item_name, category, quantity))


    elif response == "search":
        name = input("Enter the name of item you are looking for")
        print(search_resourse(name))
        
    elif response == "report":
        report()

    elif response == "exit":
        state = False

    






            


    



# print(borrow("F002", "R002", "laptop", "Electronics",2 ))
# print(add_resouce("1","car","vehicle",10,10))
# list_resource()
# for item in resources:
#     car = {"id": "R004", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
#     if item["id"] == car["id"]:
#         print("yes")
#     else:
#          print("no")
