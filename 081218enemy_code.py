# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:20:44 2018

@author: danie
"""
import random

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
            
            
weak1 = Enemy('weak1', 'physical', 2, 1, 6, 5, 50)
weak2 = Enemy('weak2', 'magic', 6, 5, 2, 1, 60)
weak3 = Enemy('weak3', 'split', 3, 4, 2, 2, 30)

mid1 = Enemy('mid1', 'physical', 10, 12, 6, 5, 100)
mid2 = Enemy('mid2', 'magic', 5, 5, 15, 12, 90)
mid3 = Enemy('mid3', 'split', 10, 10, 10, 10, 100)

hi1 = Enemy('hi1', 'physical', 20, 25, 10, 10, 140)
hi2 = Enemy('hi2', 'magic', 10, 10, 25, 18, 160)
hi3 = Enemy('hi3', 'split', 20, 20, 20, 20, 150)

tier1_enemy = [weak1, weak2, weak3]
tier2_enemy = [mid1, mid2, mid3]
tier3_enemy = [hi1, hi2, hi3]

def enemy_generator(level):
    
    global tier1_enemy
    global tier2_enemy
    global tier3_enemy
    
    if 0 < level < 20:
        enemy = random.choice(tier1_enemy)
    elif 20 <= level < 40:
        enemy = random.choice(tier2_enemy)
    elif 40 <= level < 60:
        enemy = random.choice(tier3_enemy)
    else:
         print('level out of range')
         enemy = tier1_enemy[0]
    
    return enemy
     
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
        
a = enemy_generator(50)
a.__str__()
print(a.dam_type)
b = enemy_generator(50)
b.__str__()
print(b.dam_type)

while a.hitpoints > 0 and b.hitpoints > 0:
    attack(a,b)
    if b.hitpoints == 0:
        break
    attack(b,a)
