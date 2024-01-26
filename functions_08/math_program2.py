# create 4 functions
"""
1. add_numbers : which add 2 parameters and return result
2. multiply_numbers : which multiply 3 parameters and return result
3. divide_numbers : which divide 2 parameters and return result and check not to divide by Zero
4. abs_numbers : which take 1 parameter : if it is negative just return +ive of this number
"""


def add_numbers(first_num, second_num):
    return first_num + second_num


def multiply_numbers(first_num, second_num, third_num):
    return first_num * second_num * third_num


def divide_numbers(first_num, second_num):
    if second_num != 0:
        return first_num / second_num
    else:
        print('cannot divide by Zero')
        # return -1

def abs_numbers(number):
    if number < 0:
        return number * (-1)
    else:
        return number


#main program
result_add = add_numbers(7, 6)
result_multiply = multiply_numbers(6, 2, 3)
result_divide = divide_numbers(6, 0)
result_abs = abs_numbers(8)

print(result_add, result_multiply, result_divide, result_abs)
print(add_numbers(7, 12))
