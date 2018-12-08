# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:03:44 2018

@author: daniel
"""

import random

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
###define all the equipment that will appear in the game
        
empty_slot = Equipment('no item equipped', '', '', 0, 0, 0, 0)

war_helm = Equipment('warriors helm', 'helm', 'helmet', 0, 2, 0, 0)       
ch_mail = Equipment('chainmail', 'armour', 'light armour', 0, 4, 0, 0)
w_buck = Equipment('wooden buckler', 'shield', 'round shield', 0, 2, 0, 0)
ir_axe = Equipment('iron axe', 'weapon', 'axe', 5, 0, 0, 0)

mag_orb = Equipment('mages orb', 'shield', 'magic orb', 0, 1, 0, 5)
mag_staff = Equipment('mages staff', 'weapon', 'magic staff', 0, 0, 5, 0)
mag_hat = Equipment('mages hat', 'helm', 'hat', 0, 0, 0, 2)
mag_robe = Equipment('mages robe', 'armour', 'robe', 0, 1, 0, 4)

kn_helm = Equipment('knights helm', 'helm', 'helmet', 0, 3, 0, 1)
kn_plt = Equipment('knights platemail', 'armour', 'heavy armour', 0, 5, 0, 2)
kite_sh = Equipment('kite shield', 'shield', 'kite shield', 0, 3, 0, 0)
kn_swrd = Equipment('knights sword', 'weapon', 'sword', 3, 0, 0, 0)

pal_hood = Equipment('paladin hood', 'helm', 'hood', 0, 0, 0, 3)
pal_arm = Equipment('paladin armour', 'armour', 'heavy armour', 0, 2, 0, 5)
pal_shld = Equipment('paladin shield', 'shield', 'kite shield', 0, 1, 0, 3)
ench_mace = Equipment('enchanted mace', 'weapon', 'mace', 2, 0, 2, 0)

#%%

class Potion:
    
    ### an item which, when used, will change one of the players stats by a certain amount
    
    def __init__(self, title, stat, effect = 1):
        ### each potion has a name, a stat which it will change, and an amount that it will change it by
        self.title = title
        self.stat = stat
        self.effect = effect
        
    def __str__(self):
        
        print(f'drinking this potion will have some effect on your {self.stat}')

#%%
        
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
                
    
    #print(seed)            
    #print(item.title)
    return item

#%% 
            
class Door:
    
    def __init__(self):
        
        self.open = False
        
    def __str__(self):
        
        if self.open == False:
            print('the door is not open')
        elif self.open == True:
            print('the door is open. maybe you should walk through')    

#%%
class Player_Character:
    
    ### a player character is defined with a set of slots to equip Equipment objects, and a set of stats
    def __init__(self, title = 'hero'):
        self.title = title
        self.type = ''
        self.dam_type = ''
        self.hitpoints = 100
        self.helm = empty_slot
        self.armour = empty_slot
        self.shield = empty_slot
        self.weapon = empty_slot
        self.atk = 5
        self.dfc = 5
        self.matk = 5
        self.mdfc = 5
        self.backpack = []
    
    ### describe the player characters stats and equipment
    def __str__(self):
        print(f'\n{self.title} is a {self.type} with the following attributes: \n')
        print(f'attack: {self.atk}')
        print(f'defense: {self.dfc}')
        print(f'magic attack: {self.matk}')
        print(f'magic defense: {self.mdfc}')
        print(f'total hitpoints: {self.hitpoints}\n')
        print(f'{self.title} is wearing the following equipment:')
        print(f'helm: {self.helm.title}')
        print(f'attack - {self.helm.atk} defence - {self.helm.dfc} magic attack - {self.helm.matk} magic defence - {self.helm.mdfc}\n')
        print(f'armour: {self.armour.title}')
        print(f'attack - {self.armour.atk} defence - {self.armour.dfc} magic attack - {self.armour.matk} magic defence - {self.armour.mdfc}\n')
        print(f'shield: {self.shield.title}')
        print(f'attack - {self.shield.atk} defence - {self.shield.dfc} magic attack - {self.shield.matk} magic defence - {self.shield.mdfc}\n')
        print(f'weapon: {self.weapon.title}')
        print(f'attack - {self.weapon.atk} defence - {self.weapon.dfc} magic attack - {self.weapon.matk} magic defence - {self.weapon.mdfc}\n')
    
    def char_name(self):
        #allows the player to name their character
        naming = 1
        while naming == 1:
            ### ask for a name input
            name = input('what is the name of your character? ')
            query = 1
            while query == 1:
                ### once input has been given, ask to confirm the name
                confirm = input(f'is {name} the name of your character? y/n ')
                if confirm.lower() == 'n':
                    ### if no, break the confirm loop and restart the naming loop
                    query = 0
                elif confirm.lower() == 'y':
                    ### if yes, set the characters name
                    self.title = name
                    ### break both confirm and naming loops
                    naming = 0
                    query = 0
                else:
                    ### if a valid answer is not given, ask again
                    print('please input y or n' )
                    continue
    
    def unequip(self, item):
        
        ### takes a piece of equipment as an argument and unequips that item
        if item == self.helm or item == self.armour or item == self.shield or item == self.weapon:
            ### if item is equipped, subtracts the items stat values from the players, then changes the slot to the empty_slot item
            self.atk -= item.atk
            self.dfc -= item.dfc
            self.matk -= item.matk
            self.mdfc -= item.mdfc
            if item.slot == 'helm':
                self.helm == empty_slot
                print('you unequipped your helm')
            if item.slot == 'armour':
                self.armour == empty_slot
                print('you unequipped your armour')
            if item.slot == 'shield':
                self.shield == empty_slot
                print('you unequipped your shield')
            if item.slot == 'weapon':
                self.weapon == empty_slot
                print('you unequipped your weapon')
        else:
            ### if the item is not equipped, tells the player so
            print('you so not have that item equipped')
            
    def equip(self, item):
        ### allows the player to equip a new item
        
        ### checks if the item is in the players inventory
        if item in self.backpack:
            
            ### checks the item type
            if item.slot == 'helm':
                ### subtracts the current items values from the players stats
                self.atk -= self.helm.atk
                self.dfc -= self.helm.dfc
                self.matk -= self.helm.matk
                self.mdfc -= self.helm.mdfc
                ### changes the slot to the new item
                self.helm = item
            elif item.slot == 'armour':
                self.atk -= self.armour.atk
                self.dfc -= self.armour.dfc
                self.matk -= self.armour.matk
                self.mdfc -= self.armour.mdfc
                self.armour = item
            elif item.slot == 'shield':
                self.atk -= self.shield.atk
                self.dfc -= self.shield.dfc
                self.matk -= self.shield.matk
                self.mdfc -= self.shield.mdfc
                self.shield = item
            elif item.slot == 'weapon':
                self.atk -= self.weapon.atk
                self.dfc -= self.weapon.dfc
                self.matk -= self.weapon.matk
                self.mdfc -= self.weapon.mdfc
                self.weapon = item
            ### adds the newly equipped items stats to the players stats
            self.atk += item.atk
            self.dfc += item.dfc
            self.matk += item.matk
            self.mdfc += item.mdfc
            ### tells the player that the item has been equipped
            print(f'you equipped the {item.title}')
        
        else:
            ### if the item is not in the inventory, tell the player so
            print('this piece of eqiupment is not in your inventory')
    
    def class_select(self):
        ### allows the player to choose their starting class
        ### available classes are defined as dictionaries for easy reference and include a general description as well as general stats to be added to the base stats
        char_types = {
        'warrior' : {'desc' : 'warriors are trained from a young age in the art of close-quarters combat. \nas such, these warriors have a high physical attack, but are vulnerable to magic. \nThey enter the dungeon with a sword of high quality and basic defensive armour', 'dam_type' : 'physical', 'hitpoints' : 20, 'atk' : 7, 'dfc' : 0, 'matk' : -4, 'mdfc' : 0},
        'knight' : {'desc' : 'the knights day (and night) job is as  part of the royal guard. \nnot just for show, knights are equiped with a quality set of armour, and are highly resistant to physical attacks, as well as being able to shrug off their fair share of magical ones', 'dam_type' : 'physical', 'hitpoints' : 50, 'atk' : 0, 'dfc' : 5, 'matk' : -4, 'mdfc' : 2},
        'mage' : {'desc' : 'starts with high magic attack, but not much in the way of defence', 'dam_type' : 'magic', 'hitpoints' : 0, 'atk' : -2, 'dfc' : -3, 'matk' : 8, 'mdfc' : 2},
        'paladin' : {'desc' : 'begins with high magic defence and deals both magic and physical damage', 'dam_type' : 'split', 'hitpoints' : 50, 'atk' : -2, 'dfc' : 2, 'matk' : 2, 'mdfc' : 5}
        }
        
        class_select = 1
        while class_select == 1:
            ### asks the player which class the player would like to start as
            player_class = input('please select your starting class: warrior, knight, mage, paladin ')
            if player_class.lower() in ('warrior', 'knight', 'mage', 'paladin'):
                ### if the player types a valid class, the description of that class is given
                print(char_types[player_class.lower()]['desc'])
                query = 1
                while query == 1:
                   ### ask whether the player is happy to start as this class 
                   confirm = input(f'would you like to start the game as a {player_class.lower()}? y/n ')
                   if confirm.lower() == 'n':
                       ### if no, break the confirm loop and return to the class enclosing class select loop
                       query = 0
                       continue
                   if confirm.lower() == 'y':
                       ### if yes, set the players class and add the class stats to the base stats
                       self.type = player_class.lower()
                       self.dam_type = char_types[player_class.lower()]['dam_type']
                       self.atk += char_types[player_class.lower()]['atk']
                       self.dfc += char_types[player_class.lower()]['dfc']
                       self.matk += char_types[player_class.lower()]['matk']
                       self.mdfc += char_types[player_class.lower()]['mdfc']
                       self.hitpoints += char_types[player_class.lower()]['hitpoints']
                       ### break from both loops
                       class_select = 0
                       query = 0
                   else:
                       ### if an invalid response is given, loop again
                       print('please input y/n')
                       continue
            else:
                ### if an invalid class is selected, or class is misspelt, class select loops again
                print('this is an invalid selection. please check your spelling and try again')
                continue
            
            if self.type == 'warrior':
                self.backpack.append(war_helm)
                self.backpack.append(ch_mail)
                self.backpack.append(w_buck)
                self.backpack.append(ir_axe)
                self.equip(war_helm)
                self.equip(ch_mail)
                self.equip(w_buck)
                self.equip(ir_axe)
            elif self.type == 'knight':
                self.backpack.append(kn_helm)
                self.backpack.append(kn_plt)
                self.backpack.append(kite_sh)
                self.backpack.append(kn_swrd)
                self.equip(kn_helm)
                self.equip(kn_plt)
                self.equip(kite_sh)
                self.equip(kn_swrd)
            elif self.type == 'mage':
                self.backpack.append(mag_orb)
                self.backpack.append(mag_staff)
                self.backpack.append(mag_hat)
                self.backpack.append(mag_robe)
                self.equip(mag_orb)
                self.equip(mag_staff)
                self.equip(mag_hat)
                self.equip(mag_robe)
            elif self.type == 'paladin':
                self.backpack.append(pal_hood)
                self.backpack.append(pal_arm)
                self.backpack.append(pal_shld)
                self.backpack.append(ench_mace)
                self.equip(pal_hood)
                self.equip(pal_arm)
                self.equip(pal_shld)
                self.equip(ench_mace)
#%%
                
class Enemy:
    ###enemy class defines an enemy with a name, statistics, and hitpoints and a score value which will contribute to the players score for the game
    def __init__(self, title, dam_type, atk, dfc, matk, mdfc, hitpoints):
        
        self.title = title
        self.dam_type = dam_type
        self.atk = atk
        self.dfc = dfc
        self.matk = matk
        self.mdfc = mdfc
        self.hitpoints = hitpoints
        
    def __str__(self):
        
        if self.title == 'no enemy':
            print('there is no enemy')
        else:
            print(f'you are faced with a {self.title} which has {self.hitpoints} hitpoints')
            
#%%
            
class Room:
    
    def __init__(self, enemy, chest, door):
        
        self.enemy = enemy
        self.chest = chest
        self.door = door
        
    def __str__(self):
        
        print('the room has an enemy, a chest and a door')
        
#%%
tier1_enemy = {        
'weak1' : {'title' : 'phys1', 'dam_type' : 'physical', 'atk' : 2, 'dfc' : 1, 'matk' : 6, 'mdfc' : 5, 'hitpoints' : 50},
'weak2' : {'title' : 'mag1', 'dam_type' : 'magic', 'atk' : 6, 'dfc' : 5, 'matk' : 2, 'mdfc' : 1, 'hitpoints' : 60},
'weak3' : {'title' : 'spl1', 'dam_type' : 'split', 'atk' : 3, 'dfc' : 4, 'matk' : 2, 'mdfc' : 2, 'hitpoints' : 30},
}

tier2_enemy = {
'mid1' : {'title' : 'phys2', 'dam_type' : 'physical', 'atk' : 10, 'dfc' : 12, 'matk' : 6, 'mdfc' : 5, 'hitpoints' : 100},
'mid2' : {'title' : 'mag2', 'dam_type' : 'magic', 'atk' : 5, 'dfc' : 5, 'matk' : 15, 'mdfc' : 12, 'hitpoints' : 90},
'mid3' : {'title' : 'spl2', 'dam_type' : 'split', 'atk' : 10, 'dfc' : 10, 'matk' : 10, 'mdfc' : 10, 'hitpoints' : 100},
}

tier3_enemy = {
'hi1' : {'title' : 'phys3', 'dam_type' : 'physical', 'atk' : 20, 'dfc' : 25, 'matk' : 10, 'mdfc' : 10, 'hitpoints' : 140},
'hi2' : {'title' : 'mag3', 'dam_type' : 'magic', 'atk' : 10, 'dfc' : 10, 'matk' : 25, 'mdfc' : 18, 'hitpoints' : 160},
'hi3' : {'title' : 'spl3', 'dam_type' : 'split', 'atk' : 20, 'dfc' : 20, 'matk' : 20, 'mdfc' : 20, 'hitpoints' : 150},
}

tier1_enemy_list = ['weak1', 'weak2', 'weak3']
tier2_enemy_list = ['mid1', 'mid2', 'mid3']
tier3_enemy_list = ['hi1', 'hi2', 'hi3']
#%%

def enemy_generator(level):
    
    global tier1_enemy
    global tier2_enemy
    global tier3_enemy
    global tier1_enemy_list
    global tier2_enemy_list
    global tier3_enemy_list
    
    if 0 < level < 20:
        select = random.choice(tier1_enemy_list)
        enemy = Enemy(tier1_enemy[select]['title'], tier1_enemy[select]['dam_type'], tier1_enemy[select]['atk'], tier1_enemy[select]['dfc'], tier1_enemy[select]['matk'], tier1_enemy[select]['mdfc'], tier1_enemy[select]['hitpoints'])
        
    elif 20 <= level < 40:
        select = random.choice(tier2_enemy_list)
        enemy = Enemy(tier2_enemy[select]['title'], tier2_enemy[select]['dam_type'], tier2_enemy[select]['atk'], tier2_enemy[select]['dfc'], tier2_enemy[select]['matk'], tier2_enemy[select]['mdfc'], tier2_enemy[select]['hitpoints'])
    
    elif 40 <= level < 60:
        select = random.choice(tier3_enemy_list)
        enemy = Enemy(tier3_enemy[select]['title'], tier3_enemy[select]['dam_type'], tier3_enemy[select]['atk'], tier3_enemy[select]['dfc'], tier3_enemy[select]['matk'], tier3_enemy[select]['mdfc'], tier3_enemy[select]['hitpoints'])
   
    else:
         print('level out of range')
         enemy = 'ah shit'
    
    return enemy
   
#%%
    
def attack(attacker, defender):
    
    if attacker.dam_type == 'physical':
        dam = int(random.randint(10, 20)*(attacker.atk/defender.dfc))
            
    elif attacker.dam_type == 'magic':
        dam = int(random.randint(10, 20)*(attacker.matk/defender.mdfc))
    
    elif attacker.dam_type == 'split':
        dam = int(random.randint(10, 20)*((attacker.atk+attacker.matk)/(defender.dfc+defender.mdfc)))
    
    if defender.hitpoints > dam:
        defender.hitpoints -= dam
        print(f'{attacker.title} did {dam} points of damage to {defender.title}') 
        print(f'{defender.title} has {defender.hitpoints} hitpoints remaining')
    elif defender.hitpoints <= dam:
        print(f'{attacker.title} did {dam} points of damage to {defender.title}')
        defender.hitpoints = 0
        print(f'{defender.title} was killed')
        
#%%
        
hero = Player_Character()
hero.char_name()
hero.class_select()
hero.__str__()
level = 1

#%%

room = Room(enemy_generator(level), Chest(item_generator(level, random.randint(0, 8000))), Door())
room.enemy.__str__()
while hero.hitpoints > 0 and room.enemy.hitpoints > 0:
    attack(hero, room.enemy)
    if room.enemy.hitpoints == 0:
        break
    attack(room.enemy, hero)
