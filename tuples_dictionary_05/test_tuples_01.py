
# create a tuple
person_tuple = (101, 'Yahia Momtaz', 7000.0, 'IT')
print(person_tuple)
print(type(person_tuple))

# access a tuple element
print(person_tuple[2] )
# person_tuple[2] = 9000.0   ERRROR

# concatenation
person_job = ('Python Developer', 'Senior')
person_tuple = person_tuple + person_job
print(person_tuple)

# looping note : not very important
for item in person_tuple:
    print(item)

# list of tuples
print('----------  list of tuples  ---------')
emp_ahmed = (101, 'Ahmed','Mostafa', 9000.0)
emp_marwa = (102, 'Marwa','Adham', 10000.0)
emp_ibrahim = (103, 'Ibrahim','Ehab', 14000.0)

emps_list = [ emp_ahmed, emp_marwa, emp_ibrahim]
print(emps_list)
print(emps_list[2])
