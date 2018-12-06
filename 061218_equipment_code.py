# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:43:07 2018

@author: danie
"""
import random

class Chest:
    
    #defines a chest which contains an item and indicates whether it is open or closed
    
    def __init__(self, item):
        
       self.item = item
       self.open = True
       
    def __str__(self):
        
        #prints the status of the chest dependent on whether it is open or closed or contains an item
        
        if self.open == False:
            print('the chest is unopened')
        
        if self.open == True and self.item == 'no_item':#placeholder string
            
            print('the chest is empty')
            
        elif self.open == True and self.item != 'no_item':#placeholder string
            
            print(f'the chest is open. it contains {self.item.title}')        
        
#%%
            
class Potion:
    
    ### an item which, when used, will change one of the players stats by a certain amount
    
    def __init__(self, title, stat, effect):
        ### each potion has a name, a stat which it will change, and an amount that it will change it by
        self.title = title
        self.stat = stat
        self.effect = effect
        
    def __str__(self):
        
        print(f'drinking this potion will have some effect on your {self.stat}')

#%%
        
### defines a new class for items which will be equipped to characters
class Equipment:
    
    ### equipment has a name, a slot to be equipped to, and a set of statistics
    def __init__(self, title, slot, eqtype, atk, dfc, matk, mdfc):
        self.title = title
        self.slot = slot
        self.eqtype = eqtype
        self.atk = atk
        self.dfc = dfc
        self.matk = matk
        self.mdfc = mdfc
    
    def __str__(self):
        print(f'\n{self.title} is a {self.eqtype} to be equipped as a {self.slot}')
        print(f'{self.title} has the following attributes: ')
        print(f'attack: {self.atk}')
        print(f'defense: {self.dfc}')
        print(f'magic attack: {self.matk}')
        print(f'magic defense: {self.mdfc}')

#%%
        
loweq1 = Equipment('loweq1', 'helm', 'helmet', 0, 2, 0, 0)       
loweq2 = Equipment('loweq2', 'armour', 'light armour', 0, 4, 0, 0)
loweq3 = Equipment('loweq3', 'shield', 'round shield', 0, 2, 0, 0)
loweq4 = Equipment('loweq4', 'weapon', 'axe', 5, 0, 0, 0)

mideq1 = Equipment('mideq1', 'shield', 'magic orb', 0, 1, 0, 5)
mideq2 = Equipment('mideq2', 'weapon', 'magic staff', 0, 0, 5, 0)
mideq3 = Equipment('mideq3', 'helm', 'hat', 0, 0, 0, 2)
mideq4 = Equipment('mideq4', 'armour', 'robe', 0, 1, 0, 4)

hieq1 = Equipment('hieq1', 'helm', 'helmet', 0, 3, 0, 1)
hieq2 = Equipment('hieq2', 'armour', 'heavy armour', 0, 5, 0, 2)
hieq3 = Equipment('hieq3', 'shield', 'kite shield', 0, 3, 0, 0)
hieq4 = Equipment('hieq4', 'weapon', 'sword', 3, 0, 0, 0)

#%%

lowpot1 = Potion('lowpot1', 'attack', 2)
lowpot2 = Potion('lowpot2', 'attack', 2)
lowpot3 = Potion('lowpot3', 'attack', 2)

midpot1 = Potion('midpot1', 'defence', 1)
midpot2 = Potion('midpot2', 'defence', 1)
midpot3 = Potion('midpot3', 'defence', 1)

hipot1 = Potion('hipot1', 'magic attack', 3)
hipot2 = Potion('hipot2', 'magic attack', 3)
hipot3 = Potion('hipot3', 'magic attack', 3)

#%%

lowitem = {loweq1 : range(0, 1500), loweq2 : range(1500, 3000), loweq3 : range(3000, 4500), loweq4 : range(4500, 6000), lowpot1 : range(6000, 7000), lowpot2 : range(7000, 7500), lowpot3 : range(7500, 8001)}
miditem = {mideq1 : range(0, 2000), mideq2 : range(2000, 4000), mideq3 : range(4000, 5000), mideq4 : range(5000, 5500), midpot1 : range(5500, 7000), midpot2 : range(7000, 7200), midpot3 : range(7200, 8001)}
hiitem = {hieq1 : range(0, 1000), hieq2 : range(1000, 2000), hieq3 : range(2000, 3000), hieq4 : range(3000, 4000), hipot1 : range(4000, 6000), hipot2 : range(6000, 7000), hipot3 : range(7000, 8001)}

#%%

def item_generator(level, seed):
    
    global lowitem
    global miditem
    global hiitem
    
    if 0 < level < 20:
        for i in lowitem:
            if seed in lowitem[i]:
                item = i
    
    elif 20 <= level < 40:
        for i in miditem:
            if seed in miditem[i]:
                item = i
    
    elif 40 <= level < 60:
        for i in hiitem:
            if seed in hiitem[i]:
                item = i
                
    
    print(seed)            
    print(item.title)
    return item

#%%
