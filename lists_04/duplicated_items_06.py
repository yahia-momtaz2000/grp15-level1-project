# program to show unique items in a list and duplicated in another list
numbers_list = [13, 5, 6, 22, 7, 13, 5, 7, 14, 22, 13]
# unique_list = [13, 5, 6, 22, 7, 14]
# duplicated_list = [13, 5, 7, 22]
unique_list = []
duplicated_list = []
for item in numbers_list:
    if item not in unique_list:   # membership in, not in
        unique_list.append(item)
    elif item not in duplicated_list:
        duplicated_list.append(item)

print('Original list ', numbers_list)
print('Unique list ', unique_list)
print('Duplicated list ', duplicated_list)