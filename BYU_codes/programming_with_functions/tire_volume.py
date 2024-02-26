# importing pi
import math
from datetime import datetime

# receiving the Date and Time from the system
current_date_and_time = datetime.now()

#creating the user input variables
w = float(input('Inform the width of the tire in milimiters, please: '))
a = float(input('Now inform the aspect ratio of the tire, please: '))
d = float(input('Finally, nform the diameter of the tire in inches, please: '))

# the volume calculation
v = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000

# printing the result
print(f'The aproximate volume is: {v:.2f} liters')

# creating and populating the volumes.txt
with open('volumes.txt', "a") as volume_file:
    volume_file.write(f"\nCurrent date: {current_date_and_time:%Y-%m-%d}"
                      f"\nWidth = {str(w)}"
                      f"\nAspect ratio of the tire is = {str(a)}"
                      f"\nDiameter of the wheel is = {str(d)}"
                      f"\nVolume of the tire is = {str(v)}"
                      f'\n')