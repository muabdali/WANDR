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
            
    def getWeaknessDF(self, typeList):
        typingChart = pd.read_csv("data/typingChart.csv", index_col="Name")
        for pokeType in typeList:
            coloumn = typingChart[pokeType]
            typeRow = coloumn[coloumn == "2"]
            print(typeRow)
            if not typeRow.empty:
                # returns the type name (ground, water, rock for a fire input)
                return typeRow.index[0]
            else:
                return None
            
    def getWeakness(self, typeList, returnType="giveList"):
        typingChart = pd.read_csv("data/typingChart.csv", index_col="Name")
        weaknesses = []

        for poketype in typeList:
            column = typingChart[poketype]
            typeWeaknesses = column[column == "2"]
            
            if not typeWeaknesses.empty:
                weaknesses.extend(typeWeaknesses.index.tolist())
        
        if returnType == "giveList":
            return weaknesses
        elif returnType == "giveDict":
            self.weaknessCleanup(weaknessList=weaknesses)
        else:
            return weaknesses
 
        
    def getResistance(self, typeList):
        typingChart = pd.read_csv("data/typingChart.csv", index_col="Name")
        for poketype in typeList:
            coloumn = typingChart[poketype]
            typeRow = coloumn[coloumn == "2"]
            print(typeRow)
            if not typeRow.empty:
                return typeRow.index[0]
            else:
                return None

    def weaknessCleanup(self, weaknessList):
        weaknessDict = {
            "Ground":0,
            "Fire":0,
            "Water":0,
            "Grass" : 0,
            "Ice" :0,
            "Electric" : 0,
            "Rock" : 0,
            "Flying" : 0,
            "Normal" : 0,
            "Fighting": 0,
            "Poison" : 0,
            "Psychic": 0,
            "Bug": 0,
            "Ghost": 0,
            "Dragon" : 0,
            "Steel" : 0,
            "Dark" :0,        
        }
        for elemental in weaknessList:
            weaknessDict[elemental] += 2
        print(weaknessDict)
            
            
 
    # Finds types that the pokemon is strong AGAINST.
    # For example, Charmander would return Grass, Ice, Steel and bug because those are the types that get hit 2x from fire.
    
   
ia = wandrMain()
types = ia.getTyping("Scyther")
toa = ia.getWeakness(types, returnType="giveDict")
print(toa)
   
    
"""

Welcome to the main python file for WANDR. Initially made for autoLocke,
WANDR is a script that quickly finds the types, weaknesses and resistances for a given Pokemon. (currently up to gen 3)

Order of operations:

First, the program is fed the pokemon's name. For the script to work, the 
pokemon name must be pre-spellchecked using fuzzywuzzy or something similar.

getTyping gets the typing of the given pokemon, and returns the types
as a list. For example, Bulbasaur would return ['Grass', 'Poison'].






Example:

ia = wandrMain()
types = ia.getTyping("CHARMANDER")
ia.getWeakness(types)

The following code uses Charmander as an example.
getTyping would return a list of the pokemon's types, in this case it would return
['Fire'].

getWeakness() returns a pandas dataframe



"""