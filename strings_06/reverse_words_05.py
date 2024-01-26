# program to reverse a string words
statement = "i like this program very much"
# "much very program this like i"
print(statement)
# convert string to list [ split() ]
words_list = statement.split()

# reverse the list
words_list.reverse()

# convert reversed list to string [ join() ]
statement = ' '.join(words_list)
print(statement)
