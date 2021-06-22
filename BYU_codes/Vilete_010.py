#Python Code 010

#Python Code 010

#Starting:
print('You buy a sea trip around the asia continent, but someday your trip is over … and you woke up on an isolated island, alone … ')
print('When you look around, you see nothing and no one else with you … You see just 3 things:')

#The GAME:
print('The items that you see are: \n1. ROCK \n2. WOOD STICK \n3. A ROPE. \nWhat of them will you choose? ')
choice_1 = input('Choose between a ROCK, a WOOD STICK or a ROPE: ')
if choice_1.upper() in ('ROCK','WOOD STICK','ROPE'):
    if choice_1.upper() in 'ROCK':
        choice_2 = input(f'With {choice_1} you can: \nMAKE FIRE \nor \nTRY TO FIND AN ANIMAL TO KILL \nWhat do you want to do? ')
        if choice_2.upper() in 'MAKE FIRE':
            choice_2_1 = input('Now, with FIRE, something very bad happens: \nYou have called the attention of cannibal tribes that live in this island. What will you do? \nRUN \nor \nDIE:  ')
            if choice_2_1.upper() in 'RUN':
                print('You try to RUN off from the cannibals, but they know that field very well. You\'ve failed. Sorry.')
            elif choice_2_1 in 'DIE':
                print('Try again another time! See you!')
            else:
                print('You need to choose between the valid options, please, try again!')
        elif choice_2.upper() in 'FIND AN ANIMAL TO KILL':
            choice_2_2 = input('Can you tell me where will you hunt that animal? You can Choose between: \nFOREST \nand \nCAVE: \n')
            if choice_2_2.upper() in 'FOREST':
                print('When you search in the forest for some wild animal, you get caught on a trap of the cannibal tribes. Try again.')
            elif choice_2_2.upper() in 'CAVE':
                print('In the caves, you were attacked by a horde of bats until your death. Bye bye!')
            else:
                print('You need to choose between the valid options, please, try again!')
        else:
            print('You need to choose between the valid options, please, try again!')
    elif choice_1.upper() in 'WOOD STICK':
        choice_3 = input(f'Sounds good! With {choice_1} you can do: \nMAKE A SPEAR TO HUNT SOMETHING \nor \nTAKE FRUITS ON THE TREES \nWhat will you do? \n')
        if choice_3.upper() in 'MAKE A SPEAR TO HUNT SOMETHING':
            choice_3_1 = input('You see two animals, who can you choose to kill? \nA LITTLE BEAR \nor \nLION: \n')
            if choice_3_1.upper() in 'A LITTLE BEAR':
                print('Now you have sufficient meat for eat until you find a abandoned boat on the shore to escape from the island. CONGRATULATIONS!!!')
            elif choice_3_1.upper() in 'LION':
                print('Oh man ... You find the biggest pride of lion that you ever see ... They hunt you ... Bye bye!')
            else:
                print('You need to choose between the valid options, please, try again!')
        elif choice_3.upper() in 'TAKE FRUITS ON THE TREES':
            choice_3_2 = input('Oh man, you are very lucky! You find a very good mango tree next to an avocado tree and catch the biggest and best fruits in the island. Now that you are not hungry anymore, what will you do? \nREST \nor \nTRY TO FIND SOME WAY TO SCAPE: \n')
            if choice_3_2.upper() in 'REST':
                print('The canibbals finds you and your very delicious flesh... bye bye!')
            elif choice_3_2.upper() in 'TRY TO FIND SOME WAY TO SCAPE':
                print('You get it!!! You\'ve found and abandoned boat on the shore and now are able to scape!!! CONGRATULATIONS!!!')
            else:
                print('You need to choose between the valid options, please, try again!')
        else:
            print('You need to choose between the valid options, please, try again!')
    elif choice_1.upper() in 'ROPE':
        choice_4 = input(f'Great! Now, with {choice_1} you can decide between these two actions: \nUSE IT TO CLIMB A TREE AND BE SAFE FROM THE ANIMALS \nor \nMAKE A ROPE BOWL TO GATHER FRUITS: \n')
        if choice_4.upper() in 'USE IT TO CLIMB A TREE AND BE SAFE FROM THE ANIMALS':
            print('You achieved your first athletical trophy! You climb a tree just using a rope! You are safe now ... Just until the monkeys start to fight with you for their homes...')
        elif choice_4.upper() in 'MAKE A ROPE BOWL TO GATHER FRUITS':
            choice_4_1 = ('GREAT! Now you need to search for those fruits. Where do you will search them? \nValley \nor \nFOREST: \n')
            if choice_4_1.upper() in 'VALLEY':
                print('Oh gosh ... the wild predators find you first ... Bye bye ... ')
            elif choice_4_1.upper() in 'FOREST':
                print('You find some very good fruit trees, and bonus, a good place to rest. Go to eat and sleep and try to live another day.')
            else:
                print('You need to choose between the valid options, please, try again!')
        else:
            print('You need to choose between the valid options, please, try again!')
else:
    print('You can just choose between the 3 items that you have seen...')