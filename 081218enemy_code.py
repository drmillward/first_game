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
        
