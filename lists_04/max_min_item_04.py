# program to show the max value, min value from a list
numbers_list = [14, 5, 6, 2, 17, 22, 6]

max_item = numbers_list[0]
min_item = numbers_list[0]
for item in numbers_list:
    if item > max_item:
        max_item = item

    if item < min_item:
        min_item = item

print('Max value = ', max_item)
print('Min value = ', min_item)
print(max(numbers_list))  # general function :   len, sum, min, max
print(min(numbers_list))

