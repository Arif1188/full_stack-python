# class BankAccount:
#     def __init__(self,balance=0):
#         if balance < 0:
#             raise ValueError("Balance Cannot be Negative")
#         self.balance = balance
        
#     def add(self,amount):
#         self.balance += amount
        
#     def withdraw(self,amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient balance")
#         self.balance -= amount
        
#     def check_balance(self):
#         return self.balance
    
    
# account = BankAccount(100)
# account.add(100)
# print(account.check_balance())
# account.withdraw(50)
# print(account.check_balance())


 
class ATMOperations:
    def __init__(self):
        self.currencies = {
            "1000": 50, "5000": 90, "10000": 100, "20000": 100, 
            "50000": 100, "100000": 77, "200000": 100
        }

    def withdraw(self, amount):
        withdrawn_notes = {} # yechiladigan pullar
        remaining_amount = amount # qolgan summa
        notes_names = [key for key in self.currencies.keys() if self.currencies[key] > 0][::-1]
        for note in notes_names:
            note_value = int(note)

            # Nechta pul olib chiqish kerakligini aniqlash
            potential_notes = remaining_amount // note_value 

            # Agar pullar mavjud bo'lsa, ularni hisobga olish
            notes_to_withdraw = 0
            while notes_to_withdraw < potential_notes and notes_to_withdraw < self.currencies[note]:
                notes_to_withdraw += 1
            
            if notes_to_withdraw > 0:
                withdrawn_notes[note] = notes_to_withdraw
                remaining_amount -= notes_to_withdraw * note_value
                self.currencies[note] -= notes_to_withdraw

        if remaining_amount == 0:
            print("Yechilgan pullar:")
            for note, count in withdrawn_notes.items():
                print(f"{note}: {count}")
        else:
            print("Bankomatda pul yetarli emaas")

    def check_balance(self):
        total_balance = 0
        for note, count in self.currencies.items():
            total_balance += int(note) * count
        return total_balance

    

atm = ATMOperations()
atm.withdraw(150000)
