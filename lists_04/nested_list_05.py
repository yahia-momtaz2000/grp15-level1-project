# show nested lists
my_nested_list = [[101, 'ahmed', 'Cairo'], [102, 'mostafa', 'Alex']]
my_nested_list = [[101, 'ahmed', ['El Nasr Road', 'Nasr City', 'Cairo']],
                  [102, 'mostafa', 'Alex']]
print(my_nested_list)
print(my_nested_list[0][2])
print(my_nested_list[0][2][1])

for item in my_nested_list:
    print(item)