# program to show exceptions types and how to solve
try:
    first_number = int( input('Enter your first number : ') )
    second_number = int( input('Enter your second number : ') )

    result = first_number / second_number
    print('The result = ', result)

    open('C:\\my_files\\programming.txt')
except ValueError as err_msg:
    print('Please Enter only numbers not text', err_msg)
except ZeroDivisionError as err_msg:
    print('Cannot divide By Zero - take Care !!', err_msg)
except Exception as err_msg:
    print('Error happened - PLease contact administrator at 01231231212', err_msg)
finally:
    print('This is finally statement - executed any time')

print('Continue or End of The program')