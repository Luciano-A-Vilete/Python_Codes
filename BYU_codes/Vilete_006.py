#Python Code 006

#Asking the Fahrenheit temperature:
fahrenheit = float(input('What is the Fahrenheit temperature? '))
celsius = float((fahrenheit - 32) * (5 / 9))

#Showing the Celsius temperature:
if celsius <= 0.0:
	print(f'Wow! It\'s freezing! It\'s {celsius:.1f} Cº!')
elif celsius >= 28.0:
	print(f'Oh man!!! It\'s very hot today!!! It\'s {celsius:.1f} Cº')
else:
	print(f'That\'s a normal day, it\'s just {celsius:.1f} Cº')