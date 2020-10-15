# fighting basics for text based game
import random
import sys
playerhealth = 20
playerattack = 5
playerdefence = 1
playerMove = 1
enemymove = 1
enemyhealth = 30
enemyattack = 0
enemydefence = 1
print('FIGHT BEGINS!!!')
print('You found a scary looking training dummy.......just attack it.')
while True:
    print('enemy health ' + str(enemyhealth))
    print('player health ' + str(playerhealth))
    while True:
        print('Enter your move: (a)ttack, (d)fend, (r)un or (s)tats')
        playerMove = input()
        if playerMove == 'r':
            sys.exit()  # Quit the program.
        if playerMove == 'a' or playerMove == 'd' or playerMove == 's':
                break  # Break out of the player input loop.
        print('Type one of a, d, r or s.')

    if playerMove == 'a':       # player attack
        print('You attack...')
        playerattackdamage = playerattack + random.randint(-2, 2) - enemydefence
        if playerattackdamage < enemydefence:
            print('...you missed')
        elif playerattackdamage > enemydefence:
            print('...you hit for ' + str(playerattackdamage))
            enemyhealth = enemyhealth - playerattackdamage
        elif playerattackdamage == enemydefence:
            print('...you hit...but it does nothing...')

    elif playerMove == 'd':             # player defence
        print('You defend...')
        playerdefence = playerdefence + 1
        print('...your defence has increased')

    elif playerMove == 's':             # displays player stats
        print('player health ' + str(playerhealth) + ' player attack ' + str(playerattack) + ' player defence ' + str(playerdefence))

    if enemymove == 'd':
        enemydefence = enemydefence - 1

    randomnumber = random.randint(1, 4)
    if randomnumber == 1:
        enemymove = 'd'

    elif randomnumber >= 2:
        enemymove = 'a'

    if enemymove == 'a':
        print('enemy attacks...')
        enemyattackdamage = enemyattack + random.randint(-2, 1) - playerdefence + random.randint(0, 1)
        if enemyattackdamage < playerdefence:
            print('...they missed')
        elif enemyattackdamage > playerdefence:
            print('...you got hit for ' + str(enemyattackdamage) + ' damage.....how did you manage that?')
            playerhealth = playerhealth - 1
        elif enemyattackdamage == playerdefence:
            print('...they hit...but it does nothing')

    elif enemymove == 'd':
        print('enemy defends...somehow...')
        enemydefence = enemydefence + 1
        print('...their defence increased')

    if playerMove == 'd':
        playerdefence = playerdefence - 1

    if enemyhealth <= 0:
        print('Congrats! You won! enter (f) to fight again or (q) to quit.')
        enemyhealth = 30
        playerhealth = 20
        playerchoice = input()
        if playerchoice == 'f':
            continue
        elif playerchoice == 'q':
            sys.exit()

    if playerhealth <= 0:
        print('......How did you even manage this.......you were not meant to be able to lose this fight.....?')
        print('...enter any key to leave and hang your head in shame.')
        playerchoice = input()
        if playerchoice != '':
            sys.exit()
        elif playerchoice == '':
            sys.exit()