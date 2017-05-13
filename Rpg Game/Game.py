'''
Want to add a pet module, and a main program where attacking is 
controlled by time, and i want to add a random damage fluctuation. 
'''
import random
import math   
import ast
'''
for converting string dict into literal dict
string_dict = '{\'Hello\':\'Goodbye\'}'
dict_lit = ast.literal_eval(string_dict)
'''
class Warrior:
    def __init__(self,name):
        self.name = name.title()
        self.strength = 0
        self.stam = 0
        #self.hp = 100 # + self.stam * 10
        self.hp_max = 100
        self.crit = 0
        self.hit = 75 #Out of 100%. Over 100% increases damage by the remainder. 
        self.damage = 5 #Out of 100 Max
        self.armor = {'Helmet'  : [],
                      'Shoulder': [],
                      'Chest'   : [],
                      'Gloves'  : [],
                      'Bracers' : [],
                      'Belt'    : [],
                      'Pants'   : [],
                      'Boots'   : [],
                      'Cloak'   : [],
                      'Weapon'  : []}
        self.equip(10)              
        self.equip(11)
        self.equip(12) 
        self.equip(4)
        self.equip(5)
        self.equip(6)
        self.equip(7)
        self.equip(14)
        self.equip(15)
        self.equip(16)
        '''
        self.dodge
        
        
        '''
        self.total_stats()
        self.hp = self.hp_max
    
    def __repr__(self):
        '''
        Prints the Name,total Hp, Str,Stam,Crit chance,Hit chance and Dmg. 
        '''
        line = ''
        line += 'Player Stats'.center(40,'=')+('\n'*2)
        line += justify('Name',self.name)+'\n'
        line += justify('Health Points',str(self.hp)+'/'+str(self.hp_max))+'\n'
        line += justify('Stamina',str(self.stam))+'\n'
        line += justify('Strength',str(self.strength))+'\n'
        line += justify('Hit Chance',str(self.hit)+'%')+'\n'
        line += justify('Crit Chance',str(self.crit)+'%')+'\n'
        line += justify('Damage',str(self.damage))+'\n'
        return line
        
    def equip(self,id):
        '''
        Will search armor_db.csv for item matchig the item ID, and equip said item
        to the warrior's given armor slot. 
        Name           ,      Type      ,Str , Stam , Crit,  Hit, Damage
        str title case , str title case ,int , int  , int ,int  , int
        '''
        file = open('armor_db.csv')
        for line in file:
            if line.startswith('#') or line.strip() == '':
                continue
            stats = line.strip().split(',')
            if int(stats[0]) == id:
                name = stats[1]
                type = stats[2]
                strength = int(stats[3])
                stam = int(stats[4])
                crit = int(stats[5])
                hit = int(stats[6])
                dmg = int(stats[7])
                self.armor[type] = [name,
                                    type,
                                    strength,
                                    stam,
                                    crit,
                                    hit,
                                    dmg]
                print('Equipped: '+name+' in '+type+' slot')

    def total_stats(self):
        '''
        totals the stats of the given warrior instance, taking into consideration
        all of the stats from the equipped armor. 
        '''
        stam = 0
        strength = 0
        crit = 0
        hit = 75
        damage = 5 
        keys = list(self.armor.keys())
        for key in keys:
            stam += self.armor[key][3]
            strength += self.armor[key][2]
            crit += self.armor[key][4]
            hit += self.armor[key][5]
            damage += self.armor[key][6] + strength
        self.stam = stam
        self.hp_max = 100 + stam*10 
        self.strength = strength
        self.crit = crit
        self.hit = hit
        self.damage = damage + self.strength*2
    
    def attack(self,other):
        '''
        Attacks the other warrior instance
        Takes into consideration chance to hit and chance to crit
        Critical strike is twice normal damage, 
        '''
        if len(self.armor['Weapon']) == 0:
            print(self.name+' does not have weapon equipped')
            return None  
        if not other.isalive():
            print(other.name+' is Dead')
            return None
        roll = random.randint(0,100)
        crit = random.randint(0,100)
        fluctuation = int(round(self.damage/10))
        damage_change = random.randint(-fluctuation,fluctuation)
        damage = self.damage+damage_change
        if roll <= self.hit: 
            if crit <= self.crit:
                other.hp -= 2*damage
                print('CRITICAL STRIKE!',2*damage)
            elif crit > self.crit:
                other.hp -= damage
                print(damage)
        else:
            print('Miss')    
     
    def isalive(self):
        '''
        if self is alive, returns True, Otherwise False.
        
        Returns: True
        '''
        return self.hp > 0
        
    def save(self):    
        '''
        saves the character Items and current hp are stored.
        writes said parameters out to file
        [Name,armor,]
        
        '''
        file = open(self.name+'_characterfile.csv','w')
        line = ''
        line += self.name+'|'
        line += str(self.hp)+'|'
        line += str(self.armor)
        
        file.write(line)
        file.close()
        
        
    def load(self,name):
        '''
        searches for a file in the directory, will be 
        name_characterfile.csv
        
        
        
        for converting string dict into literal dict
        string_dict = '{\'Hello\':\'Goodbye\'}'
        dict_lit = ast.literal_eval(string_dict)
        
        
        '''
        file = open(name+'_characterfile.csv')
        for line in file:
            data = line.split('|')
            self.name = data[0]
            self.hp = int(data[1])
            armor = ast.literal_eval(data[2])
            self.armor = armor
            self.total_stats()
            
    def show_character():
        '''
        stock images of a propeller cap
        4 or 5 images of funny looking skins
        layout corrdinates of armor peices, generalize
        overlay pictures of character with armor. 
        
        '''
        pass
        
        
def search_db(keyword):
    '''
    searches armor_db.csv for items containing the keyword
    then, prints out the found items along with the associated
    ID#, Name, and Type
    '''
    file = open('armor_db.csv')
    line = ''
    for line in file:
        if line.startswith('#') or line.strip() == '':
            continue
        data = line.strip().split(',')
        id = data[0]
        name = data[1]
        type = data[2]
        if keyword.lower() in name.lower():
            print('ID#: '+id+'\t|NAME: '+name+'\t|TYPE: '+type)
    
def justify(s1,s2):
    '''
    takes two strings and justifies them in a field of 35
    '''
    return s1.ljust(20)+s2.rjust(15)        
        
        
        
        
        
        
            
