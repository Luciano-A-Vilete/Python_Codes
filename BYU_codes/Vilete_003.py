#Python Code 003

#Variables:
print('Please enter the required information below:')
print('')
first_name = input('Tell me your first name, please: ')
last_name = input('Tell me your last name, please: ')
email_address = input('Tell me your e-mail, please: ')
phone_number = input('Tell me your phone number, please: ')
job_title = input('Tell me your job title, please: ')
id_number = input('Tell me your id number, please: ')

#Additional information:
hair_color = input('Tell me your hair color: ')
eye_color = input('Tell me your eye color: ')
month = input('Tell me the month that you have started here: ')
advanced_training = input('Tell me if you have completed the advanced training: ')
print('')

#Console Output:
print('The ID Card is:')
print('')
print(45*'-')
print('{}, {}'.format(last_name.upper(), first_name.title()))
print('{}'.format(job_title.title()))
print('ID = {}'.format(id_number))
print('')
print(email_address)
print(phone_number)
print('')
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {month:14} Training: {advanced_training}')
print(45*'-')