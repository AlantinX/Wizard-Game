#!/usr/bin/env python3

import inventory as inv
import character_sheet as char
import os
import combat_practice as combat

os.system('clear')
playing = 1

print ("---------- | Welcome to Wizards of Reform! | ----------\n")
print ("What would you like to do?")
print ("   For a list of commands enter, 'help'\n")


while (playing == 1):
    command = ""
    command = input('-->')
    if command == "view inv":
        inv.view()
    elif command == "open inv":
        inv.access()
    elif command == "open char":
        char.access()
    elif command == "open combat":
        combat.access()
    elif command == "rest":
        char.rest()
    elif command == "exit":
        quit()
    elif command == "help":
        print (" view inv : show all items in your inventory\n",
"open inv : Open your inventory\n",
"open char : Open your character sheet\n",
"open combat: Test your magic skills in the practice room\n",
"rest : Rest your character and recover all lost health and magic points\n")

    else:
        print("you must input a valid command.\n enter 'help' for a list of valid commands\n")
