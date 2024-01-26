# program to merge 2 lists to 1 dictionary
emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

people_dict = {}
# people_dict[101] = 'Ahmed'
# people_dict[102] = 'Omar'
# people_dict[103] = 'Sarah'

for i in range(len(emp_ids_list)):
    people_dict[  emp_ids_list[i]  ]  = emp_names_list[i]

print(people_dict)


