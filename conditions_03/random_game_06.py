# random calculation game
import random  # random module
count_correct = 0
count_wrong = 0
for i in range(5): # loop 5 times
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(first_number,'+', second_number, ' = ')
    user_result = int( input() )

    # check for the user result and the correct result
    correct_result = first_number + second_number
    if user_result == correct_result:
        print('Thanks - Correct answer')
        count_correct = count_correct + 1
    else:
        print('Sorry - Failed answer')
        count_wrong = count_wrong + 1

# after the loop
print('Correct answers = ', count_correct)
print('Wriong answers = ', count_wrong)