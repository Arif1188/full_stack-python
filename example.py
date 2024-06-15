# def sum_nth_numbers(numbers, n):
#     i = 0
#     while i < numbers[-1]:
#         i+n
    
#     return i
    



# asa = sum_nth_numbers([1,2,3,12,5,5,7,8],2)
# print(asa)


# # outpu = 27

# def sum_nth_numbers(numbers, n):
#     total = 0
#     for i in range(n-1, len(numbers), n):  # Start at n-1 for the nth number
#         total += numbers[i]
#     return total

# asa = sum_nth_numbers([1, 5, 3, 12, 5, 5, 7, 8], 2)
# print(asa)  # Output: 27


# def is_cubic_square(n):
#     sq = (n**0.5) * (n ** 0.5)
#     cu = (n**(1/3)) * (n**(1/3)) * (n**(1/3)) 
#     if  sq == n and cu == n:
#         return True
#     else:
#         return False
    

# asa = is_cubic_square(64)
# print(asa)


# import math
# def solve_exponential(base, result):
#     i = 1
#     counter = 0
#     while i < result:
#         i *= base
#         counter+=1
#     return float(counter)

# asa = solve_exponential(2,8)
# print(asa)

# def convert_to_camel_case(s):
#     splited = s.split()
#     words = ""
#     for word in splited:
#         words += word.title()
        
#     return words
# asa = convert_to_camel_case("hello world aronjon")
# print(asa)

nums = [1,2,3]
asa = nums[::-1].append(4)
print(asa)