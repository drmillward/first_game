class Equipment:
    
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

#%%%        

empty_slot = Equipment('no item equipped', '', '', 0, 0, 0, 0)
war_helm = Equipment('warriors helm', 'helm', 'helmet', 0, 2, 0, 0)
ch_mail = Equipment('chainmail', 'armour', 'light armour', 0, 4, 0, 0)
w_buck = Equipment('wooden buckler', 'shield', 'round shield', 0, 2, 0, 0)
ir_axe = Equipment('iron axe', 'weapon', 'axe', 5, 0, 0, 0)
mag_orb = Equipment('magicians orb', 'shield', 'magic orb', 0, 1, 0, 5)

#%%
mag_orb.__str__()

