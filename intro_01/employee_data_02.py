# program to show employee data
employee_id = 101               # int data type variable
employee_name = 'Ahmed Omar'    # string data type variable
employee_job = 'Python developer' # string data type variable
employee_salary = 7000.55         # float data type variable

print('-------------- Concatenation with strings ----------')
print(employee_name + ' works as '+employee_job)

print('------------ Concatenation with int or float to str ---------------')
# convert data type from int to string :   Casting
print(employee_name + ' has id '+ str(employee_id) )
print(employee_name + ' take salary '+ str( employee_salary) )

print('---------------- Casting from float to int [ to remove decimal ] -------')
print(employee_salary)      # 7000.55
print( int(employee_salary) ) # 7000

emp_sal = 2000
total_sal = emp_sal + 5.5
print(total_sal)
print(type(total_sal))

emp_name = 'Mostafa' # string
emp_name = 5000 # dynamic data type in python : int
print(emp_name)

num = 5.5 + 5.5
print(num)
print(type(num))
