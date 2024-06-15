# import datetime

# year = datetime.datetime.now().year
# user_year = int(input("Tug'ilgan yilingizni kiriting: "))
# print(year - user_year)


# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().year)



# # datetime.timedelta(days=1) bu vaqtga kun,soat,minut,sekund qo'shish uchun ishlatilinadi
# next_month_day = datetime.date.today()+datetime.timedelta(days=20)
# print(next_month_day)


# import random

# random_number = random.randint(0, 3)

# students = ["Farux", "Avaz", "ali", "Vali"]

# print(students[random_number])




 
# MRO - Method Resolution Order - metodlar ketma-ketligi

class Dunyo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

   

class World(Dunyo):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
class Person(World):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"staff class"


class Salary(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    

    def get_salary(self):
        return 4000


class Director:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"director class"


class Teacher(Salary, Staff, Director):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def groups(self):
        print("Gruppalar: 1,2,3,4,5,6")

  

teacher1 = Teacher("Ali", 30, "Math")
print(teacher1.show())

    