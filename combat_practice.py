#!/usr/bin/env python3

import os
import pandas as pd
import random
import character_sheet as char

os.system('clear')

trainingspark = [1, 4]
basicfireshot = [1, 6]
basicshield = [2, 4]

global_spells = pd.read_csv('global_spell_list.csv', index_col='Spell ID', header=0)

spellnum = ("1","2","3")
spellslist = ["1: Spark", "2: Fire Shot", "3: Shield"]
spells = ["Spark","Fire Shot","Shield"]

enemyname = "Target Dummy"
totalbarrier = 0
newbarrier = 0


def access():
    print ("---------- | Welcome to Combat Practice! | ----------\n")
    print ("Would you like to train? \n   yes | no | rest")
    menucommand = input ('-->')
    if menucommand == "yes":
        enemyhealth = random.randrange(12,20)
        spelllist()
        begincombatround(enemyhealth)
    elif menucommand == "no":
        exit()
    elif menucommand == "rest":
        char.rest()
    else:
        print("\nPlease enter yes or no")

def spelllist(): 
    print ("\n--| Spellbook | --\n")
    for spell in spellslist:
            print("%s\n" % spell)
    return


def begincombatround(enemycurrenthealth):
    while enemycurrenthealth > 0:
        global totalbarrier 
        player_current_health= char.get_current_health()
        print("Enemy health = ", enemycurrenthealth,"\nPlayer Health = ",player_current_health,"\nShield Integrity ", totalbarrier)
        if player_current_health <=0:
            dead()
        else:
            print("\nPlayer's turn")
            enemycurrenthealth = playerturn(enemycurrenthealth)

        if enemycurrenthealth <= 0:
            victory()
        else:
            enemyturn()




def attack(min, max, name):
    attackdamage = random.randrange(min, max)
    print("%s deals %s damage" % (name,attackdamage),"\n")
    return attackdamage

def shield(min,max):
    global totalbarrier
    newbarrier = 0
    magicbarrier = random.randrange(min, max)
    newbarrier += magicbarrier
    print("Shield Integrity ", newbarrier,"\n")
    totalbarrier += newbarrier
    return(totalbarrier)

def playerturn(enemycurrenthealth):
    print("Enter a spell number...")
    select_spell = input('-->')
    while select_spell not in spellnum:
        print("please enter a number between 1 and 3")
        select_spell = input('-->')
    
    if select_spell == "1":
        print("%s to %s" % (trainingspark[0], trainingspark[1]))
        enemycurrenthealth = calculatedamage(enemycurrenthealth,attack(trainingspark[0], trainingspark[1], spells[0]))
    elif select_spell == "2":
        enemycurrenthealth = calculatedamage(enemycurrenthealth,attack(basicfireshot[0], basicfireshot[1], spells[1]))
    elif select_spell == "3":
        shield(basicshield[0], basicshield[1])
    return enemycurrenthealth


def enemyturn():
    global totalbarrier 
    
    remainingdamage = 0
#    randomspell = random.randrange(1,3)
    randomspell = 1
    print("\n%s's turn" % enemyname)
    if randomspell == 1:
        attackdamage = attack(trainingspark[0], trainingspark[1], spells[0])  
        attackdamage2 = attackdamage
#        print(attackdamage2, " ", attackdamage)
        totalbarrier2 = totalbarrier
#        print(totalbarrier2, " ", totalbarrier)
        totalbarrier -= attackdamage2
#        print("shield ",totalbarrier)
        if totalbarrier <= 0:
            remainingdamage = totalbarrier * -1
            totalbarrier = 0
#            print("shield ",totalbarrier)

        attackdamage -= totalbarrier2
#        print("damage ",attackdamage)
        if attackdamage <= 0:
            attackdamage = 0
            remainingdamage = attackdamage
#            print("remaining damage ", remainingdamage)
        char.hurt(remainingdamage)
"""
    elif randomspell == 2:
        attackdamage = attack(basicfireshot[0], basicfireshot[1], spells[1])      
        attackdamage2 = attackdamage
        print(attackdamage2, " ", attackdamage)
        totalbarrier2 = totalbarrier
        print(totalbarrier2, " ", totalbarrier)
        totalbarrier -= attackdamage2
        print("shield ",totalbarrier)
        if totalbarrier <= 0:
            remainingdamage = totalbarrier * -1
            totalbarrier = 0
            print("shield ",totalbarrier)

        attackdamage -= totalbarrier2
        print("damage ",attackdamage)
        if attackdamage <= 0:
            attackdamage = 0
            remainingdamage = attackdamage
            print("remaining damage ", remainingdamage)
        if remainingdamage > 0:
            char.hurt(remainingdamage)

    else:
        print("The training target rests")
"""

def calculatedamage(enemycurrenthealth,attackdamage):
#    print(enemycurrenthealth," - ",attackdamage,"\n")
    enemynewhealth = enemycurrenthealth - attackdamage
    global totalbarrier
    global newbarrier

    return enemynewhealth

def victory():
    print("You won!")
    access()

def dead():
    print("Dude you died during practice... \nHow lame can you get?")
    access()
