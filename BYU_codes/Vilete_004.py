#Python Code 004

#Library import
import random

#Words lists
adjectives = ['attractive', 'brainy', 'brave', 'charming', 'smart']
animals = ['zebra', 'elephant', 'lion', 'dog', 'cat', 'bat']
verbs1 = ['run', 'scream', 'fly', 'walk', 'think']
exclamations = ['wow!', 'amazing!', 'great!!!', 'Wonderful!', 'Awesome!']
verbs2 = ['fight', 'clean', 'say', 'have', 'know']
verbs3 = ['make', 'take', 'use', 'work', 'feel']
#Just Trying to create a list of lists
verbs_total = [verbs1, verbs2, verbs3]

#Story
story = (f'The other day, I was really in trouble. It all started when I saw a very {random.choice(adjectives)} {random.choice(animals)} {random.choice(verbs1)} down the hallway. "{random.choice(exclamations)}" I yelled. But all I could think to do was to {random.choice(verbs2)} over and over. Miraculously, that caused it to stop, but not before it tried to {random.choice(verbs3)} right in front of my family.')

print(story)