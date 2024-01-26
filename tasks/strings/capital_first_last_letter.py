# Write a Python program to capitalize the first and last letters of each word in a given string.

str1 = "python exercises practice solution"
str1 = result = str1.title() # capitalize the first letter
# result = ""
words_list = str1.split()
for i in range(len(words_list)):
    # word[:-1] : from the beginning to the letter before the last
    # word[-1] : the last letter
    words_list[i] = words_list[i][:-1] + words_list[i][-1].upper()
    print(words_list[i])
    # result += word[:-1] + word[-1].upper() + " "
result = " ".join(words_list)
print(result)