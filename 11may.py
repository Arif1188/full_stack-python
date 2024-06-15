# import time

# def timer(func):  #func = add and example_function endi wrapper == add and example_function ning logikasiga
#     def wrapper(*args,**kwargs):
#         start = (time.time())
#         func(*args,**kwargs)
#         end_time = time.time()
#         print(end_time-start)
#     return wrapper


# @timer
# def example_function():
#     print("SAlom ")
    
# @timer
# def add(x,y):
#     print(x+y)
    
    
# example_function()
# add(1,2)



# def logger(func):
#     def ichki(a,b):
#         print(f"Funksiya berilgan argument({a},{b})")
#         print(f"Funksiyadan qaytarilgan narsa {func(a,b)}")
#     return ichki


# @logger
# def substract(a,b):
#     return a-b

# substract(10,3)


# def authenticate(func):
#     def ichki(*args, **kwargs):
#         user = kwargs.get('user')
#         if user in logged_in_users:
#             return func(*args, **kwargs)
#         else:
#             print("STOP!!!!STOP!!!!STOP!!!!")
#     return ichki

# logged_in_users = ['user1','user2','user3']

# @authenticate
# def sensetive_operation(user):
#     print(f"{user} Sen borsan, Salom!!")
    
    
# sensetive_operation(user='user1')
# sensetive_operation(user='user4')



# def uppercase(func):
#     def ichki(name):
#         a = name.upper()
#         return func(a)
#     return ichki

# @uppercase
# def greet(name):
#     return f"Hello {name}"

# print(greet("alice"))


# def twice(func):
#     def ichki(name):
#         a = name.upper()
#         return f"{func(a)}\n{func(a)}"
    
#     return ichki

# @twice
# def greet(name):
#     return f"Hello {name}"

# print(greet("alice"))



# def tekshir_argumentlar(func):
#     def ichki(a,b):
#         if b != 0:
#             return func(a,b)
#         else:
#             print(TypeError)
#     return ichki




 
# @tekshir_argumentlar
# def bolish(a, b):
#     return a / b

# natija = bolish(10, 2)  # Hech qanday xatolik yo'q
# print(natija)          # Chiqish: 5

# natija = bolish(10, 0)  # TypeError xatolik chiqarishi kerak: TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!



# def salomlash(func):
#     def ichki(ism):
#         print("Assalomu alaykum!")
#         return func(ism)
#     return ichki


# @salomlash
# def salom(ism):
#     print(f"Ismingiz nima? {ism}")

# salom("Ali")  
