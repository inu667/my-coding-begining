import sys
import random
def rogueweapondamage():
    random.randint(1, 4)
def warriorweapondamage():
    random.randint(1, 8)
enemystrength = 8
estrmod = -1
enemydexterity = 8
edexmod = -1
enemyconstitution = 8
econmod = -1
enemyhealth = 10 + econmod
eac = 10 + edexmod
eweapondamage = random.randint(1, 4) + edexmod
enemymove = 1
while True:
    while True:
        print('Please select your class')
        print('You can choose either (w)arrior or (r)ogue')
        while True:
            playerclass = input()
            if playerclass == 'w' or playerclass == 'r':
                break
            print('type either (w) or (r)')
        if playerclass == 'w':
            playerclass = 'warrior'
        elif playerclass == 'r':
            playerclass = 'rogue'
        print('Are you sure you want to be a ' + str(playerclass) + '?')
        print('(y)es or (n)o?')
        playerchoice = input()
        if playerchoice == 'y':
            print('Good choice!')
            break
        elif playerchoice == 'n':
            continue
    if playerclass == 'warrior':
        strength = 18
        strmod = 4
        dexterity = 13
        dexmod = 1
        constitution = 15
        conmod = 2
        playerhealth = 10 + random.randint(1, 10) + conmod
        ac = 12 + dexmod
        weapondamage = warriorweapondamage() + strmod
    elif playerclass == 'rogue':
        strength = 13
        strmod = 1
        dexterity = 18
        dexmod = 4
        constitution = 13
        conmod = 1
        playerhealth = 8 + random.randint(1, 8) + conmod
        ac = 11 + dexmod
        weapondamage = rogueweapondamage() + dexmod
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
            if random.randint(1, 20) < eac:
                print('...you missed')
            elif random.randint(1, 20) > eac:
                print('...you hit for ' + str(weapondamage))
                enemyhealth -= weapondamage
            elif random.randint(1, 20) == eac:
                print('...you hit...but it is a glancing blow...')

        elif playerMove == 'd':             # player defence
            print('You defend...')
            ac += 2
            print('...your defence has increased')

        elif playerMove == 's':             # displays player stats
            print('player health ' + str(playerhealth) + ' strength ' + str(strength) + ' player armor class ' + str(ac))

        if enemymove == 'd':
            eac -= 2

        randomnumber = random.randint(1, 4)
        if randomnumber == 1:
            enemymove = 'd'

        elif randomnumber >= 2:
            enemymove = 'a'

        if enemymove == 'a':
            print('enemy attacks...')
            if random.randint(1, 20) < ac:
                print('...they missed')
            elif random.randint(1, 20) > ac:
                print('...you got hit for ' + str(eweapondamage) + ' damage.....how did you manage that?')
                playerhealth -= eweapondamage
            elif random.randint(1, 20) == ac:
                print('...they hit...but it does nothing')

        elif enemymove == 'd':
            print('enemy defends...somehow...')
            eac += 2
            print('...their defence increased')

        if playerMove == 'd':
            ac -= 2
        if enemyhealth <= 0:
            print('Congrats! You won! enter (q) to quit.')
            if playerchoice == 'q':
                sys.exit()

        if playerhealth <= 0:
            print('......How did you even manage this.......you were not meant to be able to lose this fight.....?')
            print('...enter any key to leave and hang your head in shame.')
            playerchoice = input()
            if playerchoice != '':
                sys.exit()
            elif playerchoice == '':
                sys.exit()