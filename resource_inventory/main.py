# resources = [
#   {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
#   {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
#   {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
# ]

def load_task():
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    

resources = load_task()

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

def add_resouce(ID, name, category, total, available):
    new ={"id": "R00"+ ID, "name": name, "category": category, "total": total, "available": available}
    global resources
    for item in resources:
        if item["id"] == new["id"]:
            return "ID of this resource already exist"
       
    resources.append(new)
    return resources

def list_resources():
    for item in resources:
      print(item)

def borrow(fellow_Id, resources_id, name, category, quantity):
    
    if fellow_Id in fellows.keys():
        global resources
        for item in resources:
            if item["id"] == resources_id:
                if quantity <= 0:
                    return "Invalid quantity"

                if  quantity > item["available"]:
                    return "Quantity not available"

                item["available"] -= quantity
                return f"Resource borrowed successfully. Remaining available: {item['available']}"
                    
        return "Resource ID not found"
    else:
        return "fellow ID notfound"
    return "rejected without changing stock"



def return_resource(fellow_Id, resources_id, name, category, quantity):
        if fellow_Id in fellows.keys():
            global resources
            for item in resources:
                if item["id"] == resources_id:
                    if quantity >= item["total"] - item["available"]:
                        return "Invalid quantity to return"

                    item["available"] += quantity
                    return f"Resource returned successfully. Remaining available: {item['available']}"

            return "Resource ID not found"
        else:
            return "fellow ID not found"
    
        return "rejected without changing stock"



print(return_resource("F002", "R002", "laptop", "Electronics", 2))


def search_resourse(name):
    global resources
    for item in resources:
        if item["name"].lower() == name.lower():
            return item
    return "Resource not found"

def save_task():
    with open("file.json", "w") as file:
        json.dump(tasks, file, indent=2)



state = True
while state:
    print("Welcome to Resource Management App!")
    input_var = input(": Enter: 'add' to add resources, 'list' to list all resources, 'borrow' to borrow a resource, 'return' to return a resource, 'search' to search for a resource, 'exit' to quit > ")
    response = input_var.lower().strip()

    if respose == "add": 






            


    



# print(borrow("F002", "R002", "laptop", "Electronics",2 ))
# print(add_resouce("1","car","vehicle",10,10))
# list_resource()
# for item in resources:
#     car = {"id": "R004", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
#     if item["id"] == car["id"]:
#         print("yes")
#     else:
#          print("no")
