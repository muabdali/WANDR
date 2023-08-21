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
            print(types)