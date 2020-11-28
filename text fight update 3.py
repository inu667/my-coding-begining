#!/usr/bin/env python3
import sys
import random
import os
import time
def calculateAC():
    playerdata = open(playername)
    line = playerdata.readlines()
    dexmod = int(line[3])  # dexmod is 3rd line
    if playerclass == 'warrior':
        ac = 13 + dexmod
    elif playerclass == 'rogue':
        ac = 11 + dexmod
    elif playerclass == 'wizard':
        ac = 10 + dexmod
    playerdata = open(playername, 'a')
    playerdata.write(str(ac) + '\n')
    playerdata.close()
def playerhealth():
    playerdata = open(playername)  # conmod is 5th line
    lines = playerdata.readlines()
    conmod = int(lines[5])
    if playerclass == 'warrior':
        playermaxhealth = 10 + conmod
        playercurrenthealth = 10 + conmod
    elif playerclass == 'rogue':
        playermaxhealth = 8 + conmod
        playercurrenthealth = 8 + conmod
    elif playerclass == 'wizard':
        playermaxhealth = 6 + conmod
        playercurrenthealth = 6 + conmod
    playerdata = open(playername, 'a')
    playerdata.write(str(playermaxhealth) + '\n' + str(playercurrenthealth) + '\n' + playerclass + '\n')
    playerdata.close()
def wizardmagicdamage():
    playerdata = open(playername)  # intmod is 7th line
    lines = playerdata.readlines()
    intmod = int(lines[7])
    return random.randint(1, 6) + intmod
    playerdata.close()
def wizardattack():
    playerdata = open(playername)  # intmod is 7th line
    lines = playerdata.readlines()
    intmod = int(lines[7])
    return random.randint(1, 20) + intmod
    playerdata.close()
def warriorattack():
    playerdata = open(playername)  # strmod is 9th line
    lines = playerdata.readlines()
    strmod = int(lines[9])
    return random.randint(1, 20) + strmod
    playerdata.close()
def rogueattack():
    playerdata = open(playername)  # dexmod is 3rd line
    lines = playerdata.readlines()
    dexmod = int(lines[3])
    return random.randint(1, 20) + dexmod
    playerdata.close()
def rogueweapondamage():
    playerdata = open(playername)  # dexmod is 3rd line
    lines = playerdata.readlines()
    dexmod = int(lines[3])
    return random.randint(1, 4) + dexmod
    playerdata.close()
def warriorweapondamage():
    playerdata = open(playername)  # strmod is 9th line
    lines = playerdata.readlines()
    strmod = int(lines[9])
    return random.randint(1, 8) + strmod
    playerdata.close()
def enemyweapondamage():
    return random.randint(1, 4) + edexmod
# define screen clearing based on operating system
def screen_clear():
    # posix is any *nix system
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    # for windows system
def apply_stat_points():
    statpoints = 27
    strength = 8
    strmod = -1
    dexterity = 8
    dexmod = -1
    constitution = 8
    conmod = -1
    wisdom = 8
    wismod = -1
    intelligence = 8
    intmod = -1
    charisma = 8
    chamod = -1
    while statpoints != 0:
        print('you have ' + str(statpoints) + ' stat points')
        strength = int(input('what do you want to raise strength up to? (enter (8) to not raise this stat)  '))
        if strength == 15:
            statpoints -= 9
            strmod = 2
            break
        elif strength == 14:
            statpoints -= 7
            strmod = 2
            break
        elif strength == 13:
            statpoints -= 5
            strmod = 1
            break
        elif strength == 12:
            statpoints -= 4
            strmod = 1
            break
        elif strength == 11:
            statpoints -= 3
            strmod = 0
            break
        elif strength == 10:
            statpoints -= 2
            strmod = 0
            break
        elif strength == 9:
            statpoints -= 1
            strmod = -1
            break
        elif strength > 15:
            print('you can\'t go over 15 at this time.')
            continue
        elif strength == 8:
            playerchoice = input('are you sure you don\'t want to raise your strength? (y)es or (n)o.  ')
            if playerchoice == 'y':
                strmod = -1
                break
            else:
                continue
        elif strength < 8:
            print('you can\'t go under 8 in any stat.')
            continue
        print('ok. moving on to the next stat.')
    while statpoints != 0:
        print('you have ' + str(statpoints) + ' stat points')
        intelligence = int(input('what do you want to raise intelligence up to? (enter (8) to not raise this stat)  '))
        if intelligence == 15:
            statpoints -= 9
            intmod = 2
            break
        elif intelligence == 14:
            statpoints -= 7
            intmod = 2
            break
        elif intelligence == 13:
            statpoints -= 5
            intmod = 1
            break
        elif intelligence == 12:
            statpoints -= 4
            intmod = 1
            break
        elif intelligence == 11:
            statpoints -= 3
            intmod = 0
            break
        elif intelligence == 10:
            statpoints -= 2
            intmod = 0
            break
        elif intelligence == 9:
            statpoints -= 1
            intmod = -1
            break
        elif intelligence > 15:
            print('you can\'t go over 15 at this time.')
            continue
        elif intelligence == 8:
            playerchoice = input('are you sure you don\'t want to raise your intelligence? (y)es or (n)o.  ')
            if playerchoice == 'y':
                intmod = -1
                break
            else:
                continue
        elif intelligence < 8:
            print('you can\'t go under 8 in any stat.')
            continue
        print('ok. moving on to the next stat.')
    while statpoints != 0:
        print('you have ' + str(statpoints) + ' stat points')
        dexterity = int(input('what do you want to raise dexterity up to? (enter (8) to not raise this stat)  '))
        if dexterity == 15:
            statpoints -= 9
            dexmod = 2
            break
        elif dexterity == 14:
            statpoints -= 7
            dexmod = 2
            break
        elif dexterity == 13:
            statpoints -= 5
            dexmod = 1
            break
        elif dexterity == 12:
            statpoints -= 4
            dexmod = 1
            break
        elif dexterity == 11:
            statpoints -= 3
            dexmod = 0
            break
        elif dexterity == 10:
            statpoints -= 2
            dexmod = 0
            break
        elif dexterity == 9:
            statpoints -= 1
            dexmod = -1
            break
        elif dexterity > 15:
            print('you can\'t go over 15 at this time.')
            continue
        elif dexterity == 8:
            playerchoice = input('are you sure you don\'t want to raise your dexterity? (y)es or (n)o.  ')
            if playerchoice == 'y':
                dexmod = -1
                break
            else:
                continue
        elif dexterity < 8:
            print('you can\'t go under 8 in any stat.')
            continue
        print('ok. moving on to the next stat.')
    while statpoints != 0:
        print('you have ' + str(statpoints) + ' stat points')
        wisdom = int(input('what do you want to raise wisdom up to? (enter (8) to not raise this stat)  '))
        if wisdom == 15:
            statpoints -= 9
            wismod = 2
            break
        elif wisdom == 14:
            statpoints -= 7
            wismod = 2
            break
        elif wisdom == 13:
            statpoints -= 5
            wismod = 1
            break
        elif wisdom == 12:
            statpoints -= 4
            wismod = 1
            break
        elif wisdom == 11:
            statpoints -= 3
            wismod = 0
            break
        elif wisdom == 10:
            statpoints -= 2
            wismod = 0
            break
        elif wisdom == 9:
            statpoints -= 1
            wismod = -1
            break
        elif wisdom > 15:
            print('you can\'t go over 15 at this time.')
            continue
        elif wisdom == 8:
            playerchoice = input('are you sure you don\'t want to raise your wisdom? (y)es or (n)o.  ')
            if playerchoice == 'y':
                wismod = -1
                break
            else:
                continue
        elif wisdom < 8:
            print('you can\'t go under 8 in any stat.')
            continue
        print('ok. moving on to the next stat.')
    while statpoints != 0:
        print('you have ' + str(statpoints) + ' stat points')
        constitution = int(input('what do you want to raise constitution up to? (enter (8) to not raise this stat)  '))
        if constitution == 15:
            statpoints -= 9
            conmod = 2
            break
        elif constitution == 14:
            statpoints -= 7
            conmod = 2
            break
        elif constitution == 13:
            statpoints -= 5
            conmod = 1
            break
        elif constitution == 12:
            statpoints -= 4
            conmod = 1
            break
        elif constitution == 11:
            statpoints -= 3
            conmod = 0
            break
        elif constitution == 10:
            statpoints -= 2
            conmod = 0
            break
        elif constitution == 9:
            statpoints -= 1
            conmod = -1
            break
        elif constitution > 15:
            print('you can\'t go over 15 at this time.')
            continue
        elif constitution == 8:
            playerchoice = input('are you sure you don\'t want to raise your constitution? (y)es or (n)o.  ')
            if playerchoice == 'y':
                conmod = -1
                break
            else:
                continue
        elif constitution < 8:
            print('you can\'t go under 8 in any stat.')
            continue
        print('ok. moving on to the next stat.')
    while statpoints != 0:
        print('you have ' + str(statpoints) + ' stat points')
        charisma = int(input('what do you want to raise charisma up to? (enter (8) to not raise this stat)  '))
        if charisma == 15:
            statpoints -= 9
            chamod = 2
            break
        elif charisma == 14:
            statpoints -= 7
            chamod = 2
            break
        elif charisma == 13:
            statpoints -= 5
            chamod = 1
            break
        elif charisma == 12:
            statpoints -= 4
            chamod = 1
            break
        elif charisma == 11:
            statpoints -= 3
            chamod = 0
            break
        elif charisma == 10:
            statpoints -= 2
            chamod = 0
            break
        elif charisma == 9:
            statpoints -= 1
            chamod = -1
            break
        elif charisma == 8:
            playerchoice = input('are you sure you don\'t want to raise your charisma? (y)es or (n)o.  ')
            if playerchoice == 'y':
                chamod = -1
                break
            else:
                continue
        elif charisma > 15:
            print('you can\'t go over 15 at this time.')
            continue
        elif charisma < 8:
            print('you can\'t go under 8 in any stat.')
            continue
    print('congrats on setting your stats.')
    playerdata = open(playername, 'w')
    playerdata.write(str(charisma) + '\n' + str(chamod) + '\n' + str(dexterity) + '\n' + str(dexmod) + '\n' + str(constitution) + '\n' + str(conmod) + '\n' + str(intelligence) +
    '\n' + str(intmod) + '\n' + str(strength) + '\n' + str(strmod) + '\n' + str(wisdom) + '\n' + str(wismod) + '\n')
    playerdata.close()
playerweapon = 1
enemystrength = 8
estrmod = -1
enemydexterity = 8
edexmod = -1
enemyconstitution = 8
econmod = -1
enemyhealth = 10 + random.randint(1, 6) + econmod
eac = 10 + edexmod
enemymove = 1
while True:
    print('Trainer: Good, You\'re awake. come on it\'s time for training...')
    time.sleep(1.5)
    playername = input('...uh, what was your name again?  ')
    print(playername + ': I\'ve already been here a year and you still can\'t remember my name. it\'s ' + str(playername))
    time.sleep(1)
    print('Trainer: ah right. well you should know how bad I am with names. anyways, you were training with a..(crap what where they working on?)..well just pick one. ')
    time.sleep(1)
    print(playername + ': You are unbelievable. You even forgot what weapon I was learning. Fine I guess I\'ll work with a...')
    while playerweapon != 'd' or 'l' or 'm':
        playerweapon = input('System: choose either a (d)agger a (l)ongsword or (m)agic to train with.  ')
        if playerweapon == 'd':
            playerweapon = 'dagger'
            playerclass = 'rogue'
            break
        elif playerweapon == 'l':
            playerweapon = 'longsword'
            playerclass = 'warrior'
            break
        elif playerweapon == 'm':
            playerweapon = 'magic'
            playerclass = 'wizard'
            break

    print('Trainer: alright, ' + str(playerweapon) + ' it is.')
    time.sleep(1.5)
    screen_clear()
    print('Trainer: Ok I\'ll admit that I forgot basically everything about what we have been doing.(I really should quit drinking so much) Just tell me what we were doing.')
    print('system: Time to choose your stats. you have six stats, strength, wisdom, dexterity, intelligence, constitution and charisma.')
    print('(Please note that not all stats are used at this point in development)')
    print('They will each start at eight with a max of 20. you will have 27 points to distribute however you see fit.')
    print('At this point you can only raise them to 15. This chart will tell you how much it will cost to raise a stat.')
    print('Score    cost\n 9        1\n 10       2\n 11       3\n 12       4\n 13       5\n 14       7\n 15       9')
    apply_stat_points()
    playerhealth()
    screen_clear()
    calculateAC()
    print('FIGHT BEGINS!!!')
    print('You found a scary looking training dummy.......just attack it.')
    while True:
        playerdata = open(playername)  #playercurrenthealth is line 13
        line = playerdata.readlines()
        playercurrenthealth = int(line[13])
        ac = int(line[15])
        playerdata.close()
        print('enemy health ' + str(enemyhealth))
        print('player health ' + str(playercurrenthealth))
        while True:
            playerMove = input('Enter your move: (a)ttack, (d)efend, (r)un or (s)tats: ')
            if playerMove == 'r':
                print('You run away....from a dummy....are you proud of yourself?')
                time.sleep(5)
                sys.exit()  # Quit the program.
            if playerMove == 'a' or playerMove == 'd' or playerMove == 's':
                    break  # Break out of the player input loop.
            print('Type one of a, d, r or s.')

        if playerMove == 'a':
            if playerclass == 'warrior':
                weapondamage = warriorweapondamage()
                attackroll = warriorattack()
            elif playerclass == 'rogue':
                weapondamage = rogueweapondamage()
                attackroll = rogueattack()
            elif playerclass == 'wizard':
                weapondamage = wizardmagicdamage()
                attackroll = wizardattack()
            print('You attack...')
            if attackroll < eac:
                print('...you missed')
            elif attackroll > eac:
                print('...you hit for ' + str(weapondamage))
                enemyhealth -= weapondamage
            else:
                print('...you hit...but it is a glancing blow...')

        elif playerMove == 'd':             # player defence
            print('You defend...')
            ac += 2
            print('...your defence has increased')

        elif playerMove == 's':             # displays player stats
            print('player health ' + str(playerhealth) + ' strength ' + str(strength) + ' player armor class ' + str(ac))

        if enemyhealth <= 0:
            playerchoice = input('Congrats! You won! enter (q) to quit. ')
            if playerchoice == 'q':
                sys.exit()
            else:
                print('To bad. thats all there is right now. hope you had fun.')
                time.sleep(3)
                sys.exit()
        if enemymove == 'd':
            eac -= 2

        randomnumber = random.randint(1, 4)
        if randomnumber == 1:
            enemymove = 'd'

        elif randomnumber >= 2:
            enemymove = 'a'

        if enemymove == 'a':
            eweapondamage = enemyweapondamage()
            print('enemy attacks...')
            if random.randint(1, 20) <= ac:
                print('...they missed')
            elif random.randint(1, 20) > ac:
                print('...you got hit for ' + str(eweapondamage) + ' damage')
                playercurrenthealth -= eweapondamage
        elif enemymove == 'd':
            print('enemy defends...somehow...')
            eac += 2
            print('...their defence increased')
        if playerMove == 'd':
            ac -= 2

        if playercurrenthealth <= 0:
            print('......How did you even manage this.......you were not meant to be able to lose this fight.....?')
            playerchoice = input('...enter any key to leave and hang your head in shame.')
            if playerchoice != '':
                sys.exit()
            elif playerchoice == '':
                sys.exit()
        if input() == '':
            screen_clear()
        elif input() != '':
            screen_clear()