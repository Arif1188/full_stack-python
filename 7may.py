# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def calculator(foo,x,y):
#     return foo(x,y)

# result = calculator(sub, 10 ,20)
# result2 = calculator(add, 10 ,20)
# print(result)
# print(result2)


# def tashqi(n):
#     def ichki(num):
#         print(num**n)       
#     return ichki

# result = tashqi(2)

# result(3)
# result(4)


# def check_age(func):
#     def checking(name,age):
#         if age >= 18:
#             func(name,age)
#         else:
#             print("Siz juda yoshsiz")
#     return checking


# @check_age
# def passport(name,age):
#     print(name)
    
# @check_age
# def driving_l(name,age):
#     print(name,age)
    
# passport("Ali", 15)
# driving_l("Ali",20)



# def check_len(func):
#     def checking(name):
#         if len(name)>50:
#             print("Error")
#         else:
#             func(name)
#     return checking



# @check_len
# def creat_diplom(name):
#     print(name)
    
# @check_len
# def create_passport(name):
#     print(name)
    

# creat_diplom("123456789012345678901234567890123456789012345678900")




son1 = {
    1:"bir",
    2:"ikki",
    3:"uch"
}

son2 = {
    11:"o'nbir",
    12:"o'nikki",
    13:"o'nuch" 
}

son3 = {
    10:"o'n",
    20:"yigirma",
    30:"o'ttiz"
}

ask = int(input("Enter number: "))
# if son1[ask]:
#     print(son1[ask])
# elif son2[ask]:
#     print(son2[ask])
# elif son3[ask]:
#     print(son3[ask])
# else:
#     print(son3[ask]+son1[ask])


for i,j in (son2 or son1 or son3).items():
    if ask == i:
        print(j)
