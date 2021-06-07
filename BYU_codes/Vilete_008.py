#Python Code 008

#Asking values:
value_1 = int(input('Tell me the first number: '))
value_2 = int(input('Tell me the second number: '))

#If/Else Statements:

#1st IF
if value_1 > value_2:
    print(f'The first number {value_1} is grater than the second {value_2}.')
else:
    print(f'The first number {value_1} is not greater than the second {value_2}.')
    
#2nd IF
if value_1 == value_2:
    print(f'The numbers are equal!')
else:
    print(f'The first number {value_1} are not equal the second {value_2}.')
    
#3th IF
if value_2 > value_1:
    print(f'The second number {value_2} is greater than the first {value_1}.')
else:
    print(f'The second number {value_2} is not greater than the first {value_1}.')

#Ask the animal:
my_fav_animal = 'Lion'
fav_animal = input('Tell me what is your favorite animal: ')

#Animal Comparison if:
if fav_animal.lower() == my_fav_animal.lower():
    print(f'Wow! So your favorite animal is {fav_animal}? That\'s my favorite animal too!!!')
else:
    print(f'oh ... That one {fav_animal} is not the same as mine that is {my_fav_animal}.')