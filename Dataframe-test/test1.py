#!/usr/bin/env python3

import pandas as pd


def playing():
    spell_list = pd.read_csv('global_spell_list.csv', index_col='Spell ID', dtype={'Spell ID':int, 'Spell':str,'Min-damage':int,'Max-damage':int,'Magic-Cost':int,'Description':str})

    print("\n", spell_list.head(10))

    print("\n---------Show me a Spell-------\n")
    SpellID = input("Enter a Spell ID: ")
    selected_spell = spell_list.iloc[[int(SpellID) - 1]]
    #print(selected_spell)
    spell_name = selected_spell.iat[0,0]
    magic_cost = selected_spell.iat[0,3]
    print("Casting %s will cost %s magic points" % (spell_name, magic_cost))

def getspellrecord(SpellID):
    spell_list = pd.read_csv('global_spell_list.csv', index_col='Spell ID', dtype={'Spell ID':int, 'Spell':str,'Min':int,'Max':int,'Cost':int,'Description':str})
    selected_spell = spell_list.iloc[[int(SpellID) - 1]]
    return selected_spell

