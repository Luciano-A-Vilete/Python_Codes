import math

items = int(input('Enter the number of items: '))
items_per_boxes = int(input('Enter the number of items per box: '))

result = print(f'For {items} items, packing {items_per_boxes} items in each box, you will need {math.ceil(items/items_per_boxes)} boxes')