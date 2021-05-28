#Python Code 007

#Meal values:
child_meal = float(input('Tell me the price of the child\'s meal: $'))
adult_meal = float(input('Tell me the price of the adult\'s meal: $'))
soda = float(input('Tell me the price of the soda: $'))
bread = float(input('Tell me the price of bread: $'))

#People numbers:
childs = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))

#Tax rate:
tax = float(input('What is the sales tax rate? '))
tax_rate = float(tax / 100)

#Final prices
subtotal = ((child_meal * childs) + (adult_meal * adults) + (soda / (adults / 2)) + (bread / ((childs + adults) / 5)))
print(f'subtotal: ${subtotal:.2f}')
sales_tax = (subtotal * tax_rate)
print(f'Sales taxes: ${sales_tax:.2f}')
total_price = (subtotal + sales_tax)
print(f'Total: ${total_price:.2f}')

#Payment and change:

payment = float(input('What is the payment amount? $'))
change = (payment - total_price)
print(f'Change: ${change:.2f}')
if change <= 5.0:
    print('That\'s a very expensive food!')
elif change > 5 and change < 19:
    print('That\'s fair enough. Thank you!')
elif change > 20.0:
    print('I think that I can buy something more...')
