#%%
class Player_Character:
    
    ### a player character is defined with a set of slots to equip Equipment objects, and a set of stats
    def __init__(self, name = 'hero'):
        self.name = name
        self.type = ''
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
        print(f'\n{self.name} is a {self.type} with the following attributes: \n')
        print(f'attack: {self.atk}')
        print(f'defense: {self.dfc}')
        print(f'magic attack: {self.matk}')
        print(f'magic defense: {self.mdfc}')
        print(f'total hitpoints: {self.hitpoints}\n')
        print(f'{self.name} is wearing the following equipment:')
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
                    self.name = name
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
        'warrior' : {'desc' : 'warriors are trained from a young age in the art of close-quarters combat. \nas such, these warriors have a high physical attack, but are vulnerable to magic. \nThey enter the dungeon with a sword of high quality and basic defensive armour', 'hitpoints' : 20, 'atk' : 7, 'dfc' : 0, 'matk' : -4, 'mdfc' : 0},
        'knight' : {'desc' : 'the knights day (and night) job is as  part of the royal guard. \nnot just for show, knights are equiped with a quality set of armour, and are highly resistant to physical attacks, as well as being able to shrug off their fair share of magical ones', 'hitpoints' : 50, 'atk' : 0, 'dfc' : 5, 'matk' : -4, 'mdfc' : 2},
        'mage' : {'desc' : 'starts with high magic attack, but not much in the way of defence', 'hitpoints' : 0, 'atk' : -2, 'dfc' : -3, 'matk' : 8, 'mdfc' : 2},
        'paladin' : {'desc' : 'begins with high magic defence and deals both magic and physical damage', 'hitpoints' : 50, 'atk' : -2, 'dfc' : 2, 'matk' : 2, 'mdfc' : 5}
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
