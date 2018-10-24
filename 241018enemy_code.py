#%%

import random

class Enemy:
    ###enemy class defines an enemy with a name, statistics, and hitpoints and a score value which will contribute to the players score for the game
    def __init__(self, title, atk, dfc, matk, mdfc, hitpoints, score):
        
        self.title = title
        self.atk = atk
        self.dfc = dfc
        self.matk = matk
        self.mdfc = mdfc
        self.hitpoints = hitpoints
        
    def __str__(self):
        
        print(f'you are faced with a {self.title} which has {self.hitpoints} hitpoints')

#%%        
        
def weak_enemy_generator(seed):
    weakmonlist = ['goblin warrior', 'goblin mage', 'rat', 'imp']
    if seed in range(0,50):
        mon = random.choice(weakmonlist)
        if mon == 'goblin warrior':
            enemy = Enemy(mon, random.randint(5,8), random.randint(3,5), 0, random.randint(2,3), random.randint(40,50), 50)
        elif mon == 'goblin mage':
            enemy = Enemy(mon, 0, random.randint(1,2), random.randint(6,9), random.randint(3,5), random.randint(35,45), 50)
        elif mon == 'rat':
            enemy = Enemy(mon, random.randint(3,5), random.randint(2,3), 0, random.randint(1,2), random.randint(20,30), 50)
        elif mon == 'imp':
            enemy = Enemy(mon, random.randint(1,2), random.randint(1,2), random.randint(8,10), random.randint(3,5), random.randint(35,45), 60)            
        #enemy.__str__()
    else:
        print('there was no enemy in this room')
        enemy = Enemy('no enemy', 0, 0, 0, 0, 0, 0)
    
    return enemy

#%%

seed = random.randint(0,40)
a = weak_enemy_generator(seed)

a.__str__()
