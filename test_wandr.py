import pytest
from . import wandr

wM = wandr.wandrMain()

def test_typing_type():
    assert type(wM.getTyping("Scyther")) == list
    
def test_getWeakness_type():
    types = wM.getTyping("Scyther")
    weakness = wM.getWeakness(types)
    assert type(weakness) == list
    assert weakness[0] == "Fire"
    assert weakness[3] == "Electric"
    



    

