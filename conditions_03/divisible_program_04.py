# program to check if a no. is divisible by 2, 3, 6 or not

num = int (input("Enter the number: "))
if num % 2 == 0 and num % 3 == 0 and num % 6 == 0:
    print("The number is divisble")
else:
    print("The number is not divisible")