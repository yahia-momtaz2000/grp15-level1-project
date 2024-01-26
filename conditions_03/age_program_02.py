# check for person age
person_name = input('please enter person name ')
person_age = input('please enter person age ')
# convert from str to int [ casting ]
person_age = int(person_age)

if person_age > 16:
    print('You are a man')
# elif person_age >= 11 and person_age <= 16:
elif person_age >= 11:
    print('You are a boy')
else:
    print('You are a child')

