#!/usr/bin/env python3

import pandas as pd
import os

os.system('clear')

def access():
    using = 1
    while (using == 1):
        print ("Welcome to your inventory")
        print ("view | add | remove | exit\n")
        command = input('-->')

        if command == "view":
            view()

        elif command == "add":
            add()

        elif command == "remove":
            remove()

        elif command == "exit":
            break

        else:
            print("you must input a valid command")


def view():
    item_list = pd.read_csv('winventory.csv')
    print ("\n-------------------------------------------\n")
    print(item_list)
    print ("\n-------------------------------------------\n")
    

def add():
    item_list = pd.read_csv('winventory.csv')
    print ("\nWhat are you adding to your inventory?")
    additemname = input ('-->')
    print ("\nwhat kind of item is it?")
    additemtype = input ('-->')
    add_item = {'item-name': [additemname], 'item-type': [additemtype]}
    added_item = pd.DataFrame(data=add_item)
    item_list = pd.concat([item_list,added_item], join="inner", ignore_index=True)
    print ("\n-------------------------------------------\n")
    print(item_list)
    print ("\n-------------------------------------------\n")
    item_list.to_csv('winventory.csv', index=False)
    

def remove():
    item_list = pd.read_csv('winventory.csv')
    print("\nenter the item name of the item you wish to remove")
    print ("\n-------------------------------------------\n")
    print(item_list)
    print ("\n-------------------------------------------\n")
    removeitemnum = input ('-->')
    new_item_list = item_list[item_list['item-name'].str.contains('%s' % removeitemnum) == False]
    new_item_list.to_csv('winventory.csv', index=False)
    


