text = input("How old are you? ")
age = int(text)

max_heart_rate = 220 - age
lower_limit = max_heart_rate * 0.65 
upper_limit = max_heart_rate * 0.85

print(f'When you exercise to strengthen your heart, you should\nkeep your heart rate between {lower_limit:.0f} and {upper_limit:.0f} beats per minute.')