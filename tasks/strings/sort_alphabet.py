# H.w No. 6 #Write a program that takes an input string and displays its letters in alphabetical order.
# For instance, if the input is "Python", the output should be "Phnoty".
statement = 'python'
letters_list = []
for letter in statement:
    letters_list.append(letter)

print(letters_list)
letters_list.sort()
print(letters_list)
