#Python Code 009

#Starting:
print('You buy a sea trip around the asia continent, but someday your trip is over … and you woke up on an isolated island, alone … ')
print('When you look around, you see nothing and no one else with you … You see just 3 things:')

#The GAME:
print('The items that you see are: \n1. ROCK \n2. WOOD STICK \n3. A ROPE. \nWhat of them will you choose? ')
choice_1 = input('Choose between a ROCK, a WOOD STICK or a ROPE: ')
if choice_1.upper() in ('ROCK','WOOD STICK','ROPE'):
    print(f'Ok. Good choice. With {choice_1} let\'s see what we can do now...')
    if choice_1.upper() in 'ROCK':
        choice_2 = input(f'With {choice_1} you can: \nMAKE FIRE \nor \nTRY TO FIND AN ANIMAL TO KILL \nWhat do you want to do? ')
        if choice_2.upper() in 'MAKE FIRE':
            choice_2_1 = input('Now, with FIRE, something very bad happens: \nYou have called the attention of cannibal tribes that live in this island. What will you do? \nRUN \nor \nDIE:  ')
            if choice_2_1.upper() in 'RUN':
                print('You try to RUN off from the cannibals, but they know that field very well. You\'ve failed. Sorry.')
            else:
                print('Try again another time! See you!')
        elif choice_2.upper() in 'FIND AN ANIMAL TO KILL':
            choice_2_2 = input('Can you tell me where will you hunt that animal? You can Choose between: \nFOREST \nand \nCAVE: \n')
            if choice_2_2.upper() in 'FOREST':
                print('When you search in the forest for some wild animal, you get caught on a trap of the cannibal tribes. Try again.')
            elif choice_2_2.upper() in 'CAVE':
                print('In the caves, you were attacked by a horde of bats until your death. Bye bye!')
else:
    print('You can just choose between the 3 items that you have see...')