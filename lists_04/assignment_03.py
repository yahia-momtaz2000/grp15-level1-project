lst1 = [1, 6, 3, 5, 7, 4]
num1 = int(input('please enter your number: \n'))
if num1 in lst1:
    for i in range( len(lst1) ):
        if lst1[i] == num1:
            print(' the number is found on index = ', i )
else:
    print(' the number is not found ')