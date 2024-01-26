# program to calc sum, count of even numbers,
# sum, count of odd numbers in a list
my_list = [15, 2, 3, 20, 7, 9, 10]

sumEven, sumOdd, countEven, countOdd = 0, 0, 0, 0
for item in my_list:
    if item % 2 == 0:  # even
        sumEven = sumEven + item
        countEven = countEven + 1
    else:    # odd
        sumOdd = sumOdd + item
        countOdd = countOdd + 1

# end of loop
print(sumEven, countEven, sumOdd, countOdd)