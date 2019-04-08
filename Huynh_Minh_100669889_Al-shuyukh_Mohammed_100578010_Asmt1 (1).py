"""
THE ASSIGNMENT 1 CSCI 1030U
NOTE: doing in pairs

@author: Mohammed Al-shuyukh (SID: 100578010)
@author: Minh Quang Huynh (SID: 100669889)
"""

"""
PART 1
"""
def intersect(s1,s2):
    """
    intersect(s1,s2)
    This function takes two lists as input, and returns the intersection of those twosets (as a list)
    
    @arg s1 The first list
    @arg s2 The second list
    
    @return The intersections of the two lists as a list
    """
    s3=[]
    for x in range(len(s1)):
        for y in range(len(s2)):
            if(s1[x]==s2[y]):
               s3.append(s1[x])
    return s3

s1 = [1,3,5,7,9,11,13,15,17,19,21,23,25]
s2 = [1,4,9,16,25]

print('PART 1')
print(intersect(s1,s2))
print('--------------------------------------------------------------------------------------------')
print('')



"""
PART 2
"""
def gregoryLieBniz(numIterations): 
    """
    gregoryLieBniz(numIterations)
    This funtion will estimate the pi value using the Gregory-Liebniz series.
    
    @arg numIterations The amount of terms to sum up
    
    @return The approximation for pi value given the iteration
    """
    sum = 0.0 #Current sum value with no iteration 
    n = 0.0 #n starts at 0
    for n in range(numIterations):
       sum += (4.0*(pow(-1,n)))/(2.0*n + 1.0) #Calculate the estimation using the given formula  
    return round(sum, 11) #return the estimationround the answer up to 11 decimal places
  
print('PART 2')
print(gregoryLieBniz(10000000)) #Print out the estimation of pi with given iteration as 10000000
print('--------------------------------------------------------------------------------------------')
print('')
    


"""
PART 3
This part of the assigment simulates a RPG battle (with the xp and level system) between 2 groups (parties)
"""
class Character:
    """
    Character

    This class represents all of the data and behaviour of a character in our game.
    """
    def __init__(self, name, hp, xpGained, attack, defense, magic=0):
        """
        __init__(self, name, hp, xpGained, attack, defense, magic)

        This constructor initializes all of the instance variables of our class

        @arg self The character object being initialized
        @arg name The name of the character
        @arg hp The remaining hitpoints of the character
        @arg xpGained The amount of xp gained from killing enemy
        @arg attack The attack power of the character
        @arg defense The defense power of the character
        @arg magic The magic power of the character (optional, default: 0)
        """
        self.name = name
        self.xp = 0 # The xp that the character currently have
        self.xpGained = xpGained
        self.hp = hp 
        self.maxhp = hp #The max HP of character
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.level = 1 #The level of character

    def isDead(self):
        """
        isDead(self)

        This function returns True if this character is dead

        @arg self The character we want to check
        """
        if self.hp <= 0:
            return True
        return False

    def attacks(self, otherCharacter):
        """
        attacks(self, otherCharacter)

        This function simulates an attack from this character ('self') to 'otherCharacter'.
        The other character's HP is updated with the damage taken.

        @arg self The character that is attacking
        @arg otherCharacter The target of the attack
        """
        if self.isDead(): #Check if the attacker is still alive or not
            print(self.name, 'cannot attack because he/she is dead.')
        elif otherCharacter.isDead(): #Check if the target is still alive or not
            print(otherCharacter.name, ' is already dead.')
        else:
            damage = self.attack - otherCharacter.defense
            if (damage <= 0):
                damage  = 0
            otherCharacter.hp -= damage
            if otherCharacter.hp < 0:
                otherCharacter.hp = 0
            print(self.name, 'does', damage, 'points of damage to', otherCharacter.name)

    def heal(self, party):
        """
        heal(self, party)

        This function simulates a healing spell.  The HP of the entire party is updated.

        @arg self The character that is healing
        @arg party The list of party members being healed
        """
        if self.isDead(): #Check if Glinda is still alive or not
            print(self.name, 'cannot heal because he/she is dead.')
        else:
            for partyMember in party:
                if not partyMember.isDead(): #Check if the healing target is still alive or not
                    partyMember.hp += self.magic
                    if partyMember.hp > partyMember.maxhp:
                        partyMember.hp = partyMember.maxhp
                    print(self.name, 'heals', self.magic, 'hp for', partyMember.name)
                else:
                    print(partyMember.name, 'is already dead.')

    def __str__(self):
        """
        __str__(self)
        This function returns a string representation of our character

        @arg self The character that is being represented

        @return The string representation of the character
        """
        #return self.name + ' ( ' + str(self.hp) + '/' + st
        if self.isDead():
          return  '{} [DEAD]'.format(self.name)
        else:
          return '{} (HP: {}/{}, XP: {}, Level: {}, Attack: {}, Defense: {})'.format(self.name,self.hp,self.maxhp,self.xp,self.level,self.attack,self.defense)

    def gainXP(self, enemy):
        """
        gainXP(self, enemy)
        This function  will add some amount of experience to the character, possibly leveling them up as well.
        NOTE: this function will also reset the total xp the character has everytime after they level up
        
        @arg self The character that is being represented
        @arg enemy The enemy that being killed by the represented character
        """
        #lv and stat bonuses for each level
        levels=[2, 3, 4, 5, 6]
        levelsMinXP = [100, 200, 300, 400, 500]
        levelAttackGain = [5, 7.5, 10, 12.5, 15]
        levelDefenseGain = [2.5, 5, 7.5, 10, 15]
        levelMagicGain = [2, 3, 5, 8, 10]

        #add xp to the character
        self.xpGained = enemy.xpGained
        self.xp += self.xpGained

        #Party status after leveling up
        if (self.level < 6 and self.xp >= levelsMinXP[self.level-1]):
          self.attack += levelAttackGain[self.level - 1]
          self.defense += levelDefenseGain[self.level - 1]
          self.magic += levelMagicGain[self.level - 1]
          self.level  = levels[self.level - 1]
          self.xp = 0

          print('LEVEL UP !!!!! {} level is now : {} '.format(self.name , self.level))

#Create the party members
krogg = Character('Krogg',180,0,20,20)
glinda = Character('Glinda',120,0,5,20,5)
geoffrey = Character('Geoffrey',150,0,15,15)

#create the party
party = [krogg, glinda, geoffrey]

#create the enemies
enemy1 = Character('Spider 1', 50, 100, 10, 1)
enemy2 = Character('Spider 2', 50, 100, 10, 1)
enemy3 = Character('Wolf 1', 100, 250, 15, 5)
enemy4 = Character('Wolf 2', 100, 250, 15, 5)
enemy5 = Character('Bear 1', 200, 350, 20, 10)
enemy6 = Character('Bear 2', 200, 350, 20, 10)
enemy7 = Character('Red Dragon', 300, 800, 30, 20)
enemy8 = Character('Blue Dragon', 400, 1000, 35, 20)

#create a group contains the enemies above
enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]

def allDead(list):
    """
    allDead(list)
    This function will check whether all the character inside the group are all dead or not
    
    @arg list The list which represent either the party or the enemies group
    
    @return The boolean indicated whether all the character inside the group are all dead or not
    """
    count = 0
    for char in list:
        if (char.isDead() == True):
            count += 1
    if (count >= len(list)):
        return True
    else:
        return False

def printStats():
    """
    printStats()
    This function will print out the status of every character in the game
    """
    print('')
    print('CHARACTER STATUS: ')
    for partyMember in party:
      print(partyMember)
    for char in enemies:
      print(char)
    print('')
      
def printResult():
    """
    printResult()
    This function will print out the result of the game
    """
    if (allDead(enemies) == True):
        print("All enemies are dead.  You are victorious!") #it ends when all enemies are dead as a victory for the party
    elif (allDead(party) == True): #otherwise, when all party members are dead, it ends with a loss for the party
        print ("Your whole party is dead.  You lose. ")

print('PART 3')
print('')
round = 1 #Game start from round 1
i = 0 #index uses for indicating specific enemy within the list
while (allDead(enemies) == False and allDead(party) == False):
      print('ROUND ', round)
      print('ACTIONS: ')
      #party members attack the enemies
      krogg.attacks(enemies[i])
      if (enemies[i].isDead() == True):
        print('{} deals the final blows to {}.'.format(krogg.name, enemies[i].name))
        krogg.gainXP(enemies[i])
        if (i != 7):
          i += 1
        else:
          if (enemies[i].isDead() == True):
            printStats()
            printResult()
            break
      geoffrey.attacks(enemies[i])
      if (enemies[i].isDead() == True):
        print('{} deals the final blows to {}.'.format(geoffrey.name, enemies[i].name))
        geoffrey.gainXP(enemies[i])
        if (i != 7):
          i += 1
        else:
          if (enemies[i].isDead() == True):
            printStats()
            printResult()
            break
      glinda.heal(party)
      
      #enemies attack party member  
      for member in party:
        enemies[i].attacks(member)
      
      #print out the stat (and the result for the end game)
      printStats()
      printResult()
      
      round += 1 #move to next round
      