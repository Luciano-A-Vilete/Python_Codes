# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')

---------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f'Your BMI is {bmi:.0f}, you are underweight')
elif bmi > 18.5 and bmi <= 25:
    print(f'Your BMI is {bmi:.0f}, you have a normal weight')
elif bmi > 25 and bmi <= 30:
    print(f'Your BMI is {bmi:.0f}, you are slightly overweight')
elif bmi > 30 and bmi <= 35:
    print(f'Your BMI is {bmi:.0f}, you are obese')
elif bmi > 35:
    print(f'Your BMI is {bmi:.0f}, you are clinically obese')


---------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')

---------------------------------------------------------------------------------------

#Write your code below this line 👇
price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price += 1
if size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
    else:
        price = price
    if extra_cheese == "Y":
        price += 1
if size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1

print(f'Your final bill is: ${price}.')

---------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2

lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif (love_score >= 40) and (love_score <= 50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')

---------------------------------------------------------------------------------------

