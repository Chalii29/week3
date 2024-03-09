list_a = [1, 2, 3, 4, 5]
# indexes 0, 1, 2, 3, 4

list_a[0] = 10
list_a.append(6)
list_a.insert(len(list_a), 7)
list_a.extend([8, 9])
list_a.pop(0)
list_a.remove(3)
del list_a[3]


print(list_a[ : ])