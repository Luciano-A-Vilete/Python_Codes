# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first = int(two_digit_number[0])
second = int(two_digit_number[1])

final_number = first + second

print(final_number)

------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_height = float(height)
num_weight = float(weight)

bmi = int(num_weight/(num_height**2))
print(bmi)

------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

------------------------------------------------------------------------------------

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15 "))
tip_with_bill = bill * (1+ tip / 100)
bill_per_person = float(input(f'Each person should pay {tip_with_bill}'))