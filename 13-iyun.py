import copy

# a = [1,2,3,[4,5]]
# b = copy.copy(a)
# b[3].append(6)
# b.append(7)
# print(id(a[3]))
# print(id(b[3]))
# print(a)
# print(b)


a = [1,2,3,[4,5]]
b = copy.deepcopy(a)
b[3].append(6)
print(a)
print(b)