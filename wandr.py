import pandas as pd
import csv
import json

class wandrMain():
    def __init__(self):
        self.gen3TypingChart = 'data/typingChart.csv'
    
    
    def WANDR(self, pokemonName):
        self.getTyping(pokemon=pokemonName)
        
        
    def getTyping(self, pokemon):
        with open('data/pokeTypeMasterSheet.json') as file:
            data = json.load(file)
        for pokemonName in data:
            if pokemonName["Name"].lower() == pokemon.lower():
                types = pokemonName["Type1"] + pokemonName["Type2"]
                return types
                # returns types as a list
            
    def resistanceFinder(self, typeList):
        data = pd.read_csv(self.gen3TypingChart, index_col=0)
        for defense in typeList:
            allTypes = data.loc[defense]
            resistanceOnly = {key for key, value in allTypes.items() if value == "1/2"}
            print(resistanceOnly)
 
 
    # Finds types that the pokemon is strong AGAINST.
    # For example, Charmander would return Grass, Ice, Steel and bug because those are the types that get hit 2x from fire.
    def weaknessFinder(self, typeList):
        data = pd.read_csv(self.gen3TypingChart, index_col=0)
        for defense in typeList:
            allTypes = data.loc[defense]
            resistanceOnly = {key for key, value in allTypes.items() if value == "2"}
            print(resistanceOnly)    


ia = wandrMain()
types = ia.getTyping("CHARMANDER")
ia.weaknessFinder(typeList=types)

"""
Welcome to the main python file for WANDR. Initially made for autoLocke,
WANDR is a script that quickly finds the types, weaknesses and resistances for a given Pokemon. (currently up to gen 3)

Order of operations:

First, the program is fed the pokemon's name. For the script to work, the 
pokemon name must be pre-spellchecked using fuzzywuzzy or something similar.

getTyping gets the typing of the given pokemon, and returns the types
as a list. For example, Bulbasaur would return ['Grass', 'Poison'].




"""