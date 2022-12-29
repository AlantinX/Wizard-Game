#!/usr/bin/env python3

import pandas as pd
import os

os.system('clear')
using = 1
charactername = "Daniel Storm"
characterlevel = 1

character_stats = pd.read_csv('playerstats.csv', index_col='Stat', header=0)
current_health = character_stats.iat[0,0]
max_health = character_stats.iat[0,1]
current_magic = character_stats.iat[1,0]
max_magic = character_stats.iat[1,1]
armor = character_stats.iat[2,0]
current_gold = character_stats.iat[3,0]

def access():
    while (using == 1):
        print ("Welcome to the Character Sheet")
        print ("view | rest | hurt | heal | money | exit")
        command = input('-->')

        if command == "view":
            view()

        elif command == "rest":
            rest()

        elif command == "hurt":
            print("How much?")
            attackdamage = input ('-->')
            currenthealth = hurt(int(attackdamage))

        elif command == "heal":
            heal()

        elif command == "money":
            money()

        elif command == "exit":
            break

        else:
            print("you must input a valid command")


def view():
    current_health = character_stats.iat[0,0]
    max_health = character_stats.iat[0,1]
    current_magic = character_stats.iat[1,0]
    max_magic = character_stats.iat[1,1]
    armor = character_stats.iat[2,0]
    current_gold = character_stats.iat[3,0]
    print("\n---------- | Character Stats | ----------\n")
    print("Name: %s     | Level: %s\n\n" % (charactername, characterlevel))
    print("Health: %s / %s" % (current_health, max_health))
    print("Magic: %s / %s" % (current_magic, max_magic))
    print("Armor: %s" % armor)
    print("Gold: %s" % current_gold)
    print("\n-----------------------------------------\n\n")

def rest():
    character_stats.iat[0,0] = max_health
    character_stats.to_csv('playerstats.csv')
    get_current_health()
    print("Current Health: ", current_health)

def hurt(attackdamage):
    get_stats()
#    print("current health ", current_health, " - ", attackdamage)
    new_health = current_health - attackdamage
    character_stats.iat[0,0] = new_health
    character_stats.to_csv('playerstats.csv')

def get_current_health():
    get_stats()
    current_health = character_stats.iat[0,0]
    return int(current_health)


def get_stats():
    global current_health
    global max_health
    global current_magic
    global max_magic
    global armor
    global current_gold
    global character_stats
    character_stats = pd.read_csv('playerstats.csv', index_col='Stat', header=0)
    current_health = character_stats.iat[0,0]
    max_health = character_stats.iat[0,1]
    current_magic = character_stats.iat[1,0]
    max_magic = character_stats.iat[1,1]
    armor = character_stats.iat[2,0]
    current_gold = character_stats.iat[3,0]

