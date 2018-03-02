from random import shuffle
from time import sleep

class SakClass:

    
    def __init__(self): 
        
        self.letters=  ['Α','Α','Α','Α','Α','Α','Α','Α','Α','Α','Α','Α',
                       'Β',
                       'Γ','Γ',
                       'Δ','Δ',
                       'Ε','Ε','Ε','Ε','Ε','Ε','Ε','Ε',
                       'Ζ',
                       'Η','Η','Η','Η','Η','Η','Η',
                       'Θ',
                       'Ι','Ι','Ι','Ι','Ι','Ι','Ι','Ι',
                       'Κ','Κ','Κ','Κ',
                       'Λ','Λ','Λ',
                       'Μ','Μ','Μ',
                       'Ν','Ν','Ν','Ν','Ν','Ν',
                       'Ξ',
                       'Ο','Ο','Ο','Ο','Ο','Ο','Ο','Ο','Ο',
                       'Π','Π','Π','Π',
                       'Ρ','Ρ','Ρ','Ρ','Ρ',
                       'Σ','Σ','Σ','Σ','Σ','Σ','Σ',
                       'Τ','Τ','Τ','Τ','Τ','Τ','Τ','Τ',
                       'Υ','Υ','Υ','Υ',
                       'Φ',
                       'Χ',
                       'Ψ',
                       'Ω','Ω','Ω']
       


    def shuffleSak(self):
        shuffle(self.letters)
        print('ΑΝΑΚΑΤΕΥΕΤΑΙ ΤΟ ΣΑΚΟΥΛΙ')
        for i in range(0,4):
            sleep(0.7)
            print('.', end='', flush=True)
        print("\n")
        

    def get(self,numb):
        lootedList = []
        for number in range(0,numb):
            lootedList.append(self.letters.pop(0))
        return lootedList

    def throw(self,word,hand):
        for letter in range(0,len(word)):
            for letter2 in range(0,7):
                if(word[letter]==hand[letter2]):
                    del(hand[letter2])
                    break
                
            
            
               

    def change(self,hand):
        newHand= self.get(7)
        for number in range(0,7):
            self.letters.append(hand.pop(0))
        return newHand

    


    
class Player:

    def __init__(self,name):

        self.name = name
        self.hand = []
        self.points = 0

    def updatePlayerPoints(self,word,wordDict):
        self.points = wordDict[word]+ self.points

    def fullHandWithLetters(self,sak):
        if (len(self.hand)==7):
            return True

        if (len(sak.letters) >= (7-len(self.hand))):
            self.hand = self.hand + sak.get(7-len(self.hand))
            return True

        return False
            



    
        

        
class Dictionary:
    def __init__(self):

        self.wordDictionary={}

        self.letterValue =   {'Α':1,'Ε':1,'Η':1,'Ι':1,'Ν':1,'Ο':1,'Σ':1,'Τ':1,
                               'Κ':2,'Π':2,'Ρ':2,'Υ':2,
                               'Λ':3,'Μ':3,'Ω':3,
                               'Γ':4,'Δ':4,
                               'Β':8,'Φ':8,'Χ':8,
                               'Ζ':10,'Θ':10,'Ξ':10,'Ψ':10}

        def findWordValue(word):
            value=0
            for i in range(0,len(word)):
                value = self.letterValue[word[i]] + value
            return value
            
        fileGreek7 = open('greek7.txt',encoding='utf-8-sig',mode='r')

        for index in fileGreek7:
            currentWord = index.rstrip("\n")
            self.wordDictionary[currentWord]= findWordValue(currentWord)

        fileGreek7.close()

    def findValue(self,word):
            value=0
            for i in range(0,len(word)):
                value = self.letterValue[word[i]] + value
            return value


        







    




    






















        
