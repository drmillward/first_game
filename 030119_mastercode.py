# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:03:44 2018

@author: daniel
"""

import random
import csv
import datetime
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
       self.open = False
       
    def __str__(self):
        
        #prints the status of the chest dependent on whether it is open or closed or contains an item
        
        if self.open == False:
            print('the chest is unopened')
        
        if self.open == True and self.item == 'no_item':#placeholder string
            
            print('the chest is empty')
            
        elif self.open == True and self.item != 'no_item':#placeholder string
            
            print(f'the chest is open. it contains {self.item.title}')        
        
#%%
        
sthelm = Equipment('steel helm', 'helm', 'helmet', 0, 5, 0, 0)       
stplate = Equipment('steel platemail', 'armour', 'heavy armour', 0, 10, 0, 0)
stkite = Equipment('steel kite shield', 'shield', 'kite shield', 0, 10, 0, 0)
enhood = Equipment('enchanted hood', 'helm', 'hood', 0, 1, 1, 4)
enrobe = Equipment('enchanted robe', 'armour', 'robe', 0, 2, 1, 12)
enshield = Equipment('enchanted shield', 'shield', 'small shield', 0, 2, 0, 8)
wanhelm = Equipment('wanderer helm', 'helm', 'helmet', 0, 4, 0, 4)
wanmail = Equipment('wanderer chainmail', 'armour', 'chainmail', 0, 8, 0, 8) 
wanshield = Equipment('wanderer shield', 'shield', 'small shield', 0, 5, 0, 5)
herosw = Equipment('hero sword', 'weapon', 'sword', 100, 0, 0, 0)
herosh = Equipment('heroshield', 'shield', 'kite shield', 0, 100, 0, 0)
stsword = Equipment('steel sword', 'weapon', 'sword', 10, 0, 0, 0)
faxe = Equipment('fire axe', 'weapon', 'axe', 6, 0, 6, 0)
oakwand = Equipment('oak wand', 'weapon', 'wand', 0, 0, 12, 0)
mauclub = Equipment('maurauders club', 'weapon', 'club', 15, 0, 0, 0) 

elknhelm = Equipment('elite knight helm', 'helm', 'helmet', 0, 10, 0, 2)
elknarm = Equipment('elite knight armour', 'armour', 'heavy armour', 0, 18, 0, 5)
elknshd = Equipment('elite knight shield', 'shield', 'kite shield', 0, 20, 0, 5)
smlhat = Equipment('small hat', 'helm', 'wizard hat', 0, 2, 0, 12)
sorcrobe = Equipment('sorcerer robe', 'armour', 'robe', 0, 3, 0, 20)
sorcorb = Equipment('sorcerer robe', 'shield', 'magic orb', 0, 5, 0, 16)
thfhood = Equipment('thief hood', 'helm', 'hood', 0, 8, 0, 8)
thfarmr = Equipment('black leather armour', 'armour', 'leather armour', 0, 15, 0, 15)
parknf = Equipment('parry knife', 'shield', 'sidearm', 0, 10, 0, 10)
prstsw = Equipment('priest sword', 'weapon', 'sword', 12, 0, 12, 0)
lcrn = Equipment('lucerne', 'weapon', 'polearm', 22, 0, 0, 0)
sagestf = Equipment('sage staff', 'weapon', 'staff', 0, 0, 25, 0)
chsswrd = Equipment('chaos sword', 'weapon', 'sword', 35, 0, 0, 0)
chsstf = Equipment('chaos staff', 'weapon', 'staff', 0, 0, 35, 4)
blkirarm = Equipment('black iron armour', 'armour', 'platemail', 0, 30, 0, 10)
gldcrwn = Equipment('gold crown', 'helm', 'crown', 0, 8, 0, 20)
lhdsh = Equipment('lord hand shield', 'shield', 'tower shield', 0, 15, 0, 15)


hieq1 = Equipment('hieq1', 'helm', 'helmet', 0, 3, 0, 1)
hieq2 = Equipment('hieq2', 'armour', 'heavy armour', 0, 5, 0, 2)
hieq3 = Equipment('hieq3', 'shield', 'kite shield', 0, 3, 0, 0)
hieq4 = Equipment('hieq4', 'weapon', 'sword', 20, 0, 0, 0)

#%%

no_item = Potion('no item', 'na', 0)

lowstr = Potion('weak strength potion', 'attack', 2)
lowdef = Potion('weak defence potion', 'defence', 2)
lowmag = Potion('weak magic potion', 'magic attack', 2)
lowmd = Potion('weak magic defence potion', 'magic defence', 2)
lowhlt = Potion('weak health potion', 'health', 25)
lowvit = Potion('weak vitality potion', 'vitality', 25)
#badstr1 = Potion('weak magic potion', 'magic attack', 2)

midstr = Potion('strength potion', 'attack', 4)
middef = Potion('defence potion', 'defence', 4)
midmag = Potion('magic potion', 'magic attack', 4)
midmd = Potion('magic defence potion', 'magic defence', 4)
midhlt = Potion('health potion', 'health', 50)
midvit = Potion('vitality potion', 'viatlity', 40)

hipot1 = Potion('hipot1', 'magic attack', 3)
hipot2 = Potion('hipot2', 'magic attack', 3)
hipot3 = Potion('hipot3', 'magic attack', 3)

#%%

lowitem = {lowstr : range(0, 199), lowdef : range(200, 399), lowmag : range(400, 599), lowmd : range(600, 799), lowhlt : range(800, 2889), lowvit : range(2890, 3089), sthelm : range(3090, 3489), stplate : range(3490, 3889), stkite : range(3890, 4289), enhood : range(4290, 4689), enrobe : range(4690, 5089), enshield : range(5090, 5489), wanhelm : range(5490, 5789), wanmail : range(5790, 6089), wanshield : range(6090, 6389), herosw : [6390], herosh : [6391], stsword : range(6392, 6841), faxe : range(6842, 7241), oakwand : range(7242, 7691), mauclub : range(7692, 8000)}
miditem = {midstr : range(0, 100), middef : range(101, 200), midmag : range(201, 300), midmd : range(301, 400), midhlt : range(401, 2900), midvit : range(2901, 3000), elknhelm : range(3001, 3400), elknarm : range(3401, 3800), elknshd : range(3801, 4200), smlhat : range(4201, 4600), sorcrobe : range(4601, 5000), sorcorb : range(5001, 5400), thfhood : range(5401, 5800), thfarmr : range(5801, 6200), parknf : range(6201, 6600), prstsw : range(6601, 6900), lcrn : range(6901, 7200), sagestf : range(7201, 7500), chsswrd : range(7501, 7600), chsstf : range(7601, 7700), blkirarm : range(7701, 7800), gldcrwn : range(7801, 7900), lhdsh: range(7901, 8000)}
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
        self.total_hitpoints = 100
        self.helm = empty_slot
        self.armour = empty_slot
        self.shield = empty_slot
        self.weapon = empty_slot
        self.atk = 5
        self.dfc = 5
        self.matk = 5
        self.mdfc = 5
        self.backpack = []
        self.defend = False
    
    ### describe the player characters stats and equipment
    def __str__(self):
        print(f'\n{self.title} is a {self.type} with the following attributes: \n')
        print(f'attack: {self.atk}')
        print(f'defense: {self.dfc}')
        print(f'magic attack: {self.matk}')
        print(f'magic defense: {self.mdfc}')
        print(f'hitpoints: {self.hitpoints}/{self.total_hitpoints}\n')
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
        
        if item == empty_slot:
            print('you have no item equipped in that slot')
            pass
        ### takes a piece of equipment as an argument and unequips that item
        elif item == self.helm or item == self.armour or item == self.shield or item == self.weapon:
            ### if item is equipped, subtracts the items stat values from the players, then changes the slot to the empty_slot item
            self.atk -= item.atk
            self.dfc -= item.dfc
            self.matk -= item.matk
            self.mdfc -= item.mdfc
            if item.slot == 'helm':
                self.helm = empty_slot
                print('you unequipped your helm')
            if item.slot == 'armour':
                self.armour = empty_slot
                print('you unequipped your armour')
            if item.slot == 'shield':
                self.shield = empty_slot
                print('you unequipped your shield')
            if item.slot == 'weapon':
                self.weapon = empty_slot
                print('you unequipped your weapon')
            self.backpack.append(item)
        else:
            ### if the item is not equipped, tells the player so
            print('you do not have that item equipped')
            
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
                if self.helm.title != 'no item equipped':
                    self.backpack.append(self.helm)
                ### changes the slot to the new item
                self.helm = item
            elif item.slot == 'armour':
                self.atk -= self.armour.atk
                self.dfc -= self.armour.dfc
                self.matk -= self.armour.matk
                self.mdfc -= self.armour.mdfc
                if self.armour.title != 'no item equipped':
                    self.backpack.append(self.armour)
                self.armour = item
            elif item.slot == 'shield':
                self.atk -= self.shield.atk
                self.dfc -= self.shield.dfc
                self.matk -= self.shield.matk
                self.mdfc -= self.shield.mdfc
                if self.shield.title != 'no item equipped':
                    self.backpack.append(self.shield)
                self.shield = item
            elif item.slot == 'weapon':
                self.atk -= self.weapon.atk
                self.dfc -= self.weapon.dfc
                self.matk -= self.weapon.matk
                self.mdfc -= self.weapon.mdfc
                if self.weapon.title != 'no item equipped':
                    self.backpack.append(self.weapon)
                self.weapon = item
            ### adds the newly equipped items stats to the players stats
            self.atk += item.atk
            self.dfc += item.dfc
            self.matk += item.matk
            self.mdfc += item.mdfc
            ### tells the player that the item has been equipped
            print(f'you equipped the {item.title}')
            self.backpack.remove(item)
        else:
            ### if the item is not in the inventory, tell the player so
            print('this piece of eqiupment is not in your inventory')
    
    def class_select(self):
        ### allows the player to choose their starting class
        ### available classes are defined as dictionaries for easy reference and include a general description as well as general stats to be added to the base stats
        char_types = {
        'warrior' : {'desc' : 'warriors begin the game with the highest physical attack but this is offset by low defences', 'dam_type' : 'physical', 'hitpoints' : 20, 'atk' : 7, 'dfc' : 0, 'matk' : -4, 'mdfc' : 0},
        'knight' : {'desc' : 'the knight starts the game with fairly good defences, and does a moderate amount of physical attack', 'dam_type' : 'physical', 'hitpoints' : 50, 'atk' : 0, 'dfc' : 5, 'matk' : -4, 'mdfc' : 2},
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
                       self.total_hitpoints += char_types[player_class.lower()]['hitpoints']
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
                
    def drink(self, potion):
        
        if isinstance(potion, Potion):
            drink_check = 0
            if potion.stat == 'attack':
                if self.atk + potion.effect <= 0:
                    print('you may not want to drink this')
                else:
                    self.atk += potion.effect
                    drink_check = 1
            elif potion.stat == 'defence':
                if self.dfc + potion.effect <= 0:
                    print('you may not want to drink this')
                else:
                    self.dfc += potion.effect
                    drink_check = 1
            elif potion.stat == 'magic attack':
                if self.matk + potion.effect <= 0:
                    print('you may not want to drink this')
                else:
                    self.matk += potion.effect
                    drink_check = 1
            elif potion.stat == 'magic defence':
                if self.mdfc + potion.effect <= 0:
                    print('you may not want to drink this')
                else:
                    self.mdfc += potion.effect
                    drink_check = 1
            elif potion.stat == 'health':
                if self.total_hitpoints - self.hitpoints <= potion.effect:
                    self.hitpoints = self.total_hitpoints
                    drink_check = 1
                else:
                    self.hitpoints += potion.effect
                    drink_check = 1
            elif potion.stat == 'vitality':
                self.total_hitpoints += potion.effect
                self.hitpoints += potion.effect
                drink_check = 1
            
            if drink_check == 1:
                print(f'the potion changed your {potion.stat} by {potion.effect} points')
                self.backpack.remove(potion)
            
        else:
            print('i dont think you can drink that')
    
    def defend_action(self):
        
        if self.defend == False:
            if room.enemy.hitpoints == 0:
                print('you raise your shield, but given that the enemy is aleady dead, you just look silly')
            elif room.enemy.hitpoints > 0:
                print(f'you raise your shield, desperatley trying to ward of the {room.enemy.title}s incoming blow')
                self.defend = True
        elif self.defend:
            print('there is nothing more you can do to protect yourself')
            
    def player_turn(self, room):
    
        action_query = True
        while action_query == True:
            
            action = input('what would you like to do? ')
            
            if action[0:5].lower() == 'equip':
                check = 0
                for i in self.backpack:
                    if action[6::].lower() == i.title:
                        self.equip(i)
                        check = 1
                        action_query = False
                        break
                if check == 0:
                    print('that item is unavailable to equip')
            
            elif action[0:7].lower() == 'unequip':
                
                check = 0
                if action[8::].lower() == self.helm.title:
                    self.unequip(self.helm)
                    check = 1
                    action_query = False
                    break
                elif action[8::].lower() == self.armour.title:
                    self.unequip(self.armour)
                    check = 1
                    action_query = False
                    break
                elif action[8::].lower() == self.shield.title:
                    self.unequip(self.shield)
                    check = 1
                    action_query = False
                    break
                elif action[8::].lower() == self.weapon.title:
                    self.unequip(self.weapon)
                    check = 1
                    action_query = False
                    break
                if check == 0:
                    print('that item is unavailable to equip')
            
            elif action[0:6].lower() == 'attack':
                
                if action[7::].lower() == 'door':
                    print('i dont think force will work, maybe try the handle')
                    
                elif action[7::].lower() == 'chest':
                    print('i really dont think that level of force is necessary')
                    
                elif action[7::].lower() == 'self' or action[7::].lower() == 'myself':
                    print('theres enough already trying to kill you in this dungeon without you trying to do yourself in')
                    
                elif action[7::].lower() == 'enemy' or action[7::].lower() == room.enemy.title.lower():
                    if room.enemy.hitpoints > 0:
                        attack(self, room.enemy)
                        action_query = False
                        break
                    
                    elif room.enemy.hitpoints == 0:
                        print('stop it, its already dead')
                        
                else:
                    print('please input a valid target to attack')                    
            
            elif action[0:7].lower() in ['examine', 'look at']:
                
                check = 0
                for i in self.backpack:
                    if action[8::].lower() == i.title:
                        check = 1
                        i.__str__()
                
                if action[8::].lower() in ['self', 'myself', 'player', self.title.lower()]:
                    self.__str__()
                
                elif action[8::].lower() in ['pack', 'backpack', 'bag', 'inventory']:
                    print('your backpack contains:')
                    for i in self.backpack:
                        print(i.title)
                
                elif action[8::].lower() == 'enemy' or action[8::].lower() == room.enemy.title.lower():
                    room.enemy.__str__()
                        
                
                elif action[8::].lower() == 'chest':
                    room.chest.__str__()
                    
                elif action[8::].lower() == 'door':
                    room.door.__str__()
                
                elif action[8::].lower() in ['helm', 'helmet', 'hat']:
                    self.helm.__str__()
                    
                elif action[8::].lower() in ['armour', 'armor', 'robe', 'chest']:
                    self.armour.__str__()
                
                elif action[8::].lower() in ['shield']:
                    self.shield.__str__()
                
                elif action[8::].lower() in ['weapon', 'sword', 'axe', 'staff']:
                    self.weapon.__str__()
                
                else:
                    if check == 1:
                        pass
                    else:
                        print('you should be more clear about what you want to examine')
                    
            elif action[0:5].lower() == 'info':
                print('available commands include: \n')
                print('equip\nunequip\nexamine\nuse\nattack\nopen\ntake item')
                
            elif action[0:4].lower() == 'open':
                if action[5::] == 'chest':
                    if room.chest.open == False:
                        print('you opened the chest')
                        room.chest.open = True
                        room.chest.__str__()
                        action_query = False
                        break
                    elif room.chest.open == True:
                        print('the chest is already open')
                if action[5::] == 'door':
                    if room.enemy.hitpoints > 0:
                        print(f'you look towards the door, but the {room.enemy.title} blocks your path')
                    elif room.enemy.hitpoints == 0:
                        print('you walk across the room, open the door and proceed down the stairs to the next level of the dungeon')
                        room.door.open = True
                        action_query = False
                        break
            
            elif action[0:4].lower() == 'take':
                if room.chest.open == True:
                    if action[5::] in ['item', room.chest.item.title]:
                        if room.chest.item.title == 'no item':
                            print('you have already taken the item from this room')
                        else:
                            print(f'you pick up the {room.chest.item.title} and place it in your backpack, ready for later use')
                            self.backpack.append(room.chest.item)
                            room.chest.item = no_item
                            action_query = False
                            break
                    else:
                        print('what is it you want to take?')
                    
                else:
                    print('you may want to open the chest first')
                            
            
            elif action[0:5].lower() == 'drink':
                check = 0
                for i in self.backpack:
                    if action[6::].lower() == i.title:
                        check += 1
                        self.drink(i)
                        action_query = False
                        break
                if check == 0:
                    print('that is not available to drink')
            
            elif action[0:7].lower() == 'discard':
                bagcheck = 0
                for i in self.backpack:
                    if action[8::].lower() == i.title:
                        discard_item = i
                        bagcheck = 1
                        break
                if bagcheck == 1:
                    dconfirm = 0
                    while dconfirm == 0:
                        dcheck = input(f'would you like to throw away {discard_item.title}? y/n ')
                        if dcheck.lower() == 'y':
                            self.backpack.remove(discard_item)
                            print(f'you throw away {discard_item.title}')
                            action_query = False
                            dconfirm = 1
                            break
                        elif dcheck.lower() == 'n':
                            print('you decided not to throw it away')
                            dconfirm = 1
                            break
                        else:
                            print('please input y or n ')
                elif bagcheck == 0:
                    print('that does not seem to be an item which can be discarded')
                            
            elif action.lower() == 'defend':
                if self.shield == empty_slot:
                    print('it crosses your mind that defending yourself in this situation would be useful, however you find yourself without any means of defence')
                else:
                    self.defend_action()
                    action_query = False
                    break
            
            elif action.lower() == 'end':
                self.hitpoints = 0
                room.door.open = True
                action_query = False
                break
            
            else:
                print('please input a valid action')
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
        self.defend = False
        
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
'imp' : {'title' : 'imp', 'dam_type' : 'split', 'atk' : 10, 'dfc' : 7, 'matk' : 3, 'mdfc' : 7, 'hitpoints' : 50},
'pixie' : {'title' : 'pixie', 'dam_type' : 'magic', 'atk' : 2, 'dfc' : 5, 'matk' : 12, 'mdfc' : 10, 'hitpoints' : 45},
'gobscout' : {'title' : 'goblin scout', 'dam_type' : 'physical', 'atk' : 10, 'dfc' : 10, 'matk' : 0, 'mdfc' : 6, 'hitpoints' : 60},
'zambo' : {'title' : 'decomposed zombie', 'dam_type' : 'physical', 'atk' : 8, 'dfc' : 8, 'matk' : 0, 'mdfc' : 5, 'hitpoints' : 25},
'skeleton' : {'title' : 'skeleton', 'dam_type' : 'split', 'atk' : 10, 'dfc' : 12, 'matk' : 8, 'mdfc' : 8, 'hitpoints' : 50},
'necro' : {'title' : 'necromancer', 'dam_type' : 'magic', 'atk' : 0, 'dfc' : 7, 'matk' : 15, 'mdfc' : 12, 'hitpoints' : 40},
'ferdog' : {'title' : 'feral dog', 'dam_type' : 'physical', 'atk' : 10, 'dfc' : 6, 'matk' : 0, 'mdfc' : 4, 'hitpoints' : 30},
'smuggler' : {'title' : 'smuggler', 'dam_type' : 'split', 'atk' : 7, 'dfc' : 8, 'matk' : 8, 'mdfc' : 7, 'hitpoints' : 55},
'lrgrat' : {'title' : 'large rat', 'dam_type' : 'physical', 'atk' : 6, 'dfc' : 5, 'matk' : 0, 'mdfc' : 4, 'hitpoints' : 35},
'evslime' : {'title' : 'evil slime', 'dam_type' : 'magic', 'atk' : 0, 'dfc' : 10, 'matk': 13, 'mdfc' : 12, 'hitpoints' : 50}
}

tier2_enemy = {
'centaur' : {'title' : 'centaur', 'dam_type' : 'split', 'atk' : 15, 'dfc' : 25, 'matk' : 15, 'mdfc' : 10, 'hitpoints' : 75},
'crptelf' : {'title' : 'corrupted elf', 'dam_type' : 'magic', 'atk' : 10, 'dfc' : 15, 'matk' : 35, 'mdfc' : 30, 'hitpoints' : 70},
'gobsold' : {'title' : 'goblin sol', 'dam_type' : 'physical', 'atk' : 30, 'dfc' : 30, 'matk' : 10, 'mdfc' : 15, 'hitpoints' : 70},
'orc' : {'title' : 'orc', 'dam_type' : 'physical', 'atk' : 40, 'dfc' : 20, 'matk' : 10, 'mdfc' : 10, 'hitpoints' : 100},
'gspider' : {'title' : 'giant spider', 'dam_type' : 'split', 'atk' : 20, 'dfc' : 15, 'matk' : 20, 'mdfc' : 15, 'hitpoints' : 75},
'cavebear' : {'title' : 'cave bear', 'dam_type' : 'physical', 'atk' : 25, 'dfc' : 40, 'matk' : 10, 'mdfc' : 20, 'hitpoints' : 80},
'cavelurk' : {'title' : 'cave lurker', 'dam_type' : 'split', 'atk' : 20, 'dfc' : 25, 'matk' : 20, 'mdfc' : 25, 'hitpoints' : 90},
'succ' : {'title' : 'succubus', 'dam_type' : 'magic', 'atk' : 10, 'dfc' : 15, 'matk' : 40, 'mdfc' : 20, 'hitpoints' : 75},
'inc' : {'title' : 'incubus', 'dam_type' : 'magic', 'atk' : 10, 'dfc' : 30, 'matk' : 25, 'mdfc' : 40, 'hitpoints' : 95},
'mntr' : {'title' : 'minotaur', 'dam_type' : 'physical', 'atk' : 40, 'dfc' : 30, 'matk' : 10, 'mdfc' : 25, 'hitpoints' : 100},
}

tier3_enemy = {
'hi1' : {'title' : 'phys3', 'dam_type' : 'physical', 'atk' : 20, 'dfc' : 25, 'matk' : 10, 'mdfc' : 10, 'hitpoints' : 140},
'hi2' : {'title' : 'mag3', 'dam_type' : 'magic', 'atk' : 10, 'dfc' : 10, 'matk' : 25, 'mdfc' : 18, 'hitpoints' : 160},
'hi3' : {'title' : 'spl3', 'dam_type' : 'split', 'atk' : 20, 'dfc' : 20, 'matk' : 20, 'mdfc' : 20, 'hitpoints' : 150},
}

tier1_enemy_list = ['imp', 'pixie', 'gobscout', 'zambo', 'skeleton', 'necro', 'ferdog', 'smuggler', 'lrgrat', 'evslime']
tier2_enemy_list = ['centaur', 'crptelf', 'gobsold', 'orc', 'gspider', 'cavebear', 'cavelurk', 'succ', 'inc', 'mntr']
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
        dam = int(random.randint(8, 12)*(attacker.atk/defender.dfc))
            
    elif attacker.dam_type == 'magic':
        dam = int(random.randint(8, 12)*(attacker.matk/defender.mdfc))
    
    elif attacker.dam_type == 'split':
        dam = int(random.randint(8, 12)*((attacker.atk+attacker.matk)/(defender.dfc+defender.mdfc)))
    
    if defender.defend == True:
        dam = int(dam*random.uniform(0.25, 0.75))
    
    if defender.hitpoints > dam:
        defender.hitpoints -= dam
        print(f'{attacker.title} did {dam} points of damage to {defender.title}') 
        print(f'{defender.title} has {defender.hitpoints} hitpoints remaining\n')
    elif defender.hitpoints <= dam:
        print(f'{attacker.title} did {dam} points of damage to {defender.title}')
        defender.hitpoints = 0
        print(f'{defender.title} was killed')
        
#%%
def hiscore_report():
    with open('score_record.csv', 'r') as highscore:
        hiscore = 0
        hitpoints = 0
        info = {}
        
        reader = csv.DictReader(highscore)
        for row in reader:
            if int(row['dungeon level']) > int(hiscore):
                hiscore = row['dungeon level']
                info = row
            elif int(row['dungeon level']) == int(hiscore) and int(row['hitpoints remaining']) > hitpoints:
                hiscore = row['dungeon level']
                hitpoints
                info = row
        print(f"the best run was made by a {info['class']} called {info['character name']}: ")
        print('')
        print(f"dungeon level : {info['dungeon level']}")
        print(f"remaining hitpoints : {info['hitpoints remaining']}")
        print(f"attack : {info['attack']}")
        print(f"defence : {info['defence']}")
        print(f"magic attack : {info['magic attack']}")
        print(f"magic defence : {info['magic defence']}")
        print('')
        print(f" the run was made on {info['date']}")
#%%
        
if __name__ == '__main__':
    
    hiscore_report()
    hero = Player_Character()
    hero.char_name()
    hero.class_select()
    hero.__str__()
    level = 0
               
    while level <= 60 and hero.hitpoints > 0:
        level += 1
        defend_count = 0
        print(f'you enter floor number {level} of the dungeon')
        seed = random.randint(0, 8000)
        print(seed)
        room = Room(enemy_generator(level), Chest(item_generator(level, seed)), Door())
        room.__str__()
        room.enemy.__str__()
        while room.door.open == False:
            hero.player_turn(room)
            if hero.hitpoints <= 0:
                print('you died')
                break
            if room.enemy.hitpoints > 0:
                attack(room.enemy, hero)
            if hero.hitpoints <= 0:
                print('you died')
                break
            if hero.defend == True and defend_count == 0:
                defend_count = 1
                print('you continue to ward off the enemy with your shield')
            elif hero.defend == True and defend_count == 1:
                hero.defend = False
                defend_count = 0
                print('you lower your shield')
        
        
    with open('score_record.csv', 'a', newline = '') as scorelog:
        now = datetime.datetime.now()
        fieldnames = ['character name', 'class', 'dungeon level', 'hitpoints remaining', 'attack', 'defence', 'magic attack', 'magic defence', 'date']
        scorewriter = csv.DictWriter(scorelog, fieldnames = fieldnames)
        scorewriter.writerow({'character name' : hero.title, 'class' : hero.type, 'dungeon level' : level, 'hitpoints remaining' : hero.hitpoints, 'attack' : hero.atk, 'defence' : hero.dfc, 'magic attack' : hero.matk, 'magic defence' : hero.mdfc, 'date' : now.strftime('%Y-%m-%d')})
