empty_set = set()

empty_dictionary = {}

# print('Data type of empty_set: ', type(empty_set))
# data type of set
# print('Data type of empty_dictionary: ', type(empty_dictionary))
# data type of set

house_id = {20, 21, 22, 23, 24}
location = {100, 101, 102, 103, 104}
print('Initial Set:', house_id)

#using add() method
house_id.add(30)
house_id.update(location)
print('Updated Set:', house_id)

house_id.discard(22)
print(len(house_id))