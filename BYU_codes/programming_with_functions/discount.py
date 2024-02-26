# Import the necessary module
from datetime import datetime

# getting the date and weekday
current_date = datetime.now()
weekday = current_date.weekday() + 1

# creating the necessary variable
discount = 0.10
tax = 0.06
subtotal = float(input('Tell me how much was your shopping subtotal (just numbers). ex: 99.99: '))

# creating the conditional statements
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * discount, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
    total_tax = round(subtotal * tax, 2)
    total_amount = subtotal + total_tax
elif subtotal < 50.00 and (weekday == 1 or weekday == 2):
    total_tax = round(subtotal * tax, 2)
    total_amount = subtotal + total_tax
    difference_needed_for_discount = 50.00 - subtotal
    print(f'You need more {difference_needed_for_discount} to receive 10% of discount in your subtotal!')
else:
    total_amount = subtotal + (subtotal * tax)
    total_tax = subtotal * tax
    
# printing the result
print(f'Sales tax amount: {total_tax:.2f}')
print(f'Total: {total_amount:.2f}')
