# show function use     round(), pow(2, 3) , sqrt(16),
def print_numbers(max_value):   # function parameter [ function input ]
    sum = 0
    for i in range(1, max_value):
        print(i, end=' ')
        sum = sum + i
    print()
    return sum


# main program
print('main program')
# call the function ( sub program )
sum_result = print_numbers(101)
print('Sum result = ', sum_result)