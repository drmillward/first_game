#%%
import random

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
        
### some potions are defined
s_str_pot = Potion('small strength potion', 'strength', 2)
l_str_pot = Potion('large strength potion', 'strength', 4)
b_str_pot = Potion('small strength potion', 'strength', -2)

### a list of the potions will be used to generate the contents of a chest
potion_list = [s_str_pot, l_str_pot, b_str_pot]

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
            
new_chest = Chest(random.choice(potion_list))
new_chest.__str__()
print(new_chest.item.effect)
