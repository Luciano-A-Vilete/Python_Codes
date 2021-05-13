#Python Code 001

#Asking the favorite color and showing them in the console.

name = input('Please tell me, what is your name? ')
print('Hello ' 'nice to meet you!!!')
fav_color = input('Now {}, can you tell me what is your favorite color? ' .format(name))
if fav_color.lower() == 'Green':
    print('Green??? The same as my favorite color! GREAT!!!')
elif fav_color.lower() == 'Blue':
    print('It is wonderful to know that your favorite color is {}, the same fav color as my wife.' .format(fav_color))
else:
    print(f'It is wonderful to know that your favorite color is {fav_color}')