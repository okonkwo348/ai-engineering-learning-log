# class UserProfile:
#     def __init__(self, username, phone_no, age):
#         self.name = username
#         self.phone = phone_no
#         self.age = age
#         self.is_active = True

#     def update_phone(self, new_phone):
#         self.phone = new_phone
#         return f" {self.name}'s phone number has been updated!"

#     def current_status(self, is_active):
#         self.is_active = is_active
#         return f"{self.name} is currently not Active "

#     def get_summary(self):
#         return f"User: {self.name} | Age: {self.age} | Active: {self.is_active} "

# user1 = UserProfile("Jehu", "08038448", 23)
# user2 = UserProfile("Alex", "07034444", 34)

# print(user1.phone)
# # print(user1.update_phone("090445"))
# print(user1.phone)
# print(user1.current_status(False))
# print(user1.get_summary())

class BankAccount:
    def __init__(self, owner_name, strating_balance = 0.0):
        self.holder = owner_name
        self.balance = strating_balance

    def deposite(self, amount):
        self.balance += amount
        print(f" Depoosite ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <=  self.balance:
            self.balance -= amount
            return True
            

        else:
            print("Tranction Declined: Insuficient funds !")
            return False
            


    def transfer(self, target_account, amount):
        success = self.withdraw(amount)
        if success:
            target_account.balance += amount
            print(f"✅ Transferred ${amount} to {target_account.holder}!")


account1 = BankAccount("Emma", 200)
account2 = BankAccount("Jerry", 300)
account1.transfer(account2,100)
print(account1.balance)
