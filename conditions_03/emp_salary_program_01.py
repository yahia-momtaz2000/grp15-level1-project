# calculate net salary based on Gross Salary
# 10% tax if G.S >= 5000        0% tax if G.S < 5000

emp_name = 'Yahia Momtaz'
emp_gross_salary = 7000

if emp_gross_salary >= 5000:
    tax = 10
    print('tax = 10')
else:
    tax = 0
    print('tax = 0')

# calculate net salary equation
emp_net_salary = emp_gross_salary - emp_gross_salary * tax / 100;
print('emp monthly net salary = ', emp_net_salary)
# calculate annual salary
emp_net_annual_salary = emp_net_salary * 12
print('emp annual net salary = ',emp_net_annual_salary)