# Ex No. 3 : # Create a function to check a number if it is even number:
# function  : check_even function,      parameter: 1 parameter [int],
# output: boolean       Even : true   |   Odd :   false
"""
def check_even(x):
    is_even = False  # Flag
    if x % 2 == 0:
        is_even = True
    return is_even

# main program
# call function
result = check_even(6)
if result:
    print('it is even no')
else:
    print('it is odd no.')
"""
def check_even(x):
    """
    this function will return a dictionary as a key of a number, value of boolean
    :param x: should be int value param
    :return: will return a dictionary
    """
    my_dict = {}
    if x % 2 == 0:
        my_dict[x] = True
    else:
        my_dict[x] = False
    return my_dict

#main program
num = 12
res_dict = check_even(num)
print(res_dict)



