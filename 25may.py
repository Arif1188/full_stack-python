# ; encapsulation - class ichidagi obyektlarni class ichida yaratish
# ; name magling
# ; private

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

# person = Person("John",25)

# # print(person.__name)
# # name magling
# # obj._ClassName__variableName
# print(person._Person__name)



# getter va setter
# class Person:
#     def __init__(self,name,age):
#         self.__age = age
        
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self,value):
#         self.__age = value
        
# person = Person("John",30)
# print(person.age)
# person.age = 40



# class Person:
#     def __init__(self,name,age):
#         self.__age = age
        
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self,value):
#         try:
#             number = int(value)
#             self.__age = value
#         except ValueError:
#             print("Age must be a number")
        
# person = Person("John",30)
# print(person.age)
# person.age = "dsfsdfdsfs"




# M I S O L

# class Staff:
#     def __init__(self,first_name,last_name,salary_amount):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary_amount = salary_amount
        
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def get_salary(self):
#         return self.salary_amount * 0.8
    

# class Developer(Staff):
#     def __init__(self, first_name, last_name, salary_amount,age):
#         super().__init__(first_name, last_name, salary_amount)
#         self.age = age
        
#     def me(self):
#         return f"ismi : {self.first_name}\nyoshi : {self.age}"
    
#     def get_salary(self):
#         return self.salary_amount * 0.9
    
    
# man = Developer("Orifjon","nabiyev",3000000,21)
# print(man.me())
    

# class Devs:
#     def __init__(self):
#         self.__age = 0
        
#     def get_age(self):
#         return self.__age
    
#     def set_age(self,new_age):
#         if new_age > 0:
#             self.__age = new_age
#         else:
#              print(ValueError(f"{new_age} should  > 0"))
    
    
# man = Devs()
# man.set_age(44)
# print(man.get_age())
        


# from abc import ABC,abstractmethod

# class Hayvon(ABC):
#     def ovoz_ber():
#         pass
    
# class Mushuk(Hayvon):
#     def ovoz_ber():
#         return "MeW"
        
# print(Mushuk.ovoz_ber())

