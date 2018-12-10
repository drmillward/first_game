def player_turn(player, room):
    
    action_query = True
    while action_query == True:
        
        action = input('what would you like to do? ')
        
        if action[0:5].lower() == 'equip':
            check = 0
            for i in player.backpack:
                if action[6::].lower() == i.title:
                    player.equip(i)
                    check = 1
                    action_query = False
                    break
            if check == 0:
                print('that item is unavailable to equip')
        
        elif action[0:7].lower() == 'unequip':
            
            check = 0
            for i in player.backpack:
                if action[8::].lower() == i.title:
                    player.unequip(i)
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
                    attack(player, room.enemy)
                    action_query = False
                    break
                
                elif room.enemy.hitpoints == 0:
                    print('stop it, its already dead')
                    
            else:
                print('please input a valid target to attack')                    
        
        elif action[0:7].lower() == 'examine':
            
            pass
        
        else:
            print('please input a valid action')
