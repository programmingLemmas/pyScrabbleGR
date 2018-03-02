from mylib21582311 import Dictionary,Player,SakClass
from random import randint
from time import sleep
from itertools import permutations

def createGreek7FromGreek():
    fileGreek = open('greek.txt',encoding='utf-8',mode='r')
    fileGreek7 = open('greek7.txt',encoding='utf-8',mode='w')

    for index in fileGreek:
        if (len(index)<=8):
            fileGreek7.write(index)

    fileGreek.close()
    fileGreek7.close()




def wordIsValid1(givenWord,hand):

    valid1 = False
    for lets in range(0,len(givenWord)):
        if givenWord[lets] not in hand:
            return False

    return True
    


def wordIsValid2(givenWord,dictionary:dict):

    if givenWord not in dictionary:
        return False
    else:
        return True




def giveAWordPassOrQuit(player,diction,sak):
    while(True):

        givenWord = input ("ΓΡΑΨΤΕ ΤΗΝ ΛΕΞΗ ΣΑΣ: ").upper()

        if (givenWord == 'P' or givenWord ==''):
            player.hand = sak.change(player.hand)
            return True

        if (givenWord == 'Q'):
            return False

        if (wordIsValid1(givenWord,player.hand)):
            if (wordIsValid2(givenWord,diction.wordDictionary)):
                player.updatePlayerPoints(givenWord,diction.wordDictionary)
                sak.throw(givenWord,player.hand)
                print("\nΕΓΚΥΡΗ ΛΕΞΗ! ΑΞΙΑ : " + str(diction.findValue(givenWord)))
                return True
            else:
                print("\nΔΕΝ ΥΠΑΡΧΕΙ ΑΥΤΗ Η ΛΕΞΗ ΣΤΟ ΛΕΞΙΚΟ, ΞΑΝΑΠΡΟΣΠΑΘΗΣΤΕ")
        else:
            print("\nΧΡΗΣΙΜΟΠΟΙΗΣΑΤΕ ΜΗ ΕΓΚΥΡΑ ΓΡΑΜΜΑΤΑ, ΞΑΝΑΠΡΟΣΠΑΘΗΣΤΕ")           
    
    



def headsOrTails(choice):
    result = randint(0,1)
    resultString = "ΚΟΡΩΝΑ" if (int(result)==0) else "ΓΡΑΜΜΑΤΑ"

    print('\n'+ 'ΤΟ ΝΟΜΙΣΜΑ ΓΥΡΙΖΕΙ ΣΤΟΝ ΑΕΡΑ')

    for i in range(0,3):
        sleep(0.7)
        print('.', end='', flush=True)
    print("\n")
    
    if (int(choice)==result):
        print("ΤΟ ΑΠΟΤΕΛΕΣΜΑ ΕΙΝΑΙ " + resultString + ". ΚΕΡΔΙΣΕΣ :) ")
        return True

    print("ΤΟ ΑΠΟΤΕΛΕΣΜΑ ΕΙΝΑΙ " + resultString + ". ΕΧΑΣΕΣ :( ")
    return False



def getChoice():
    choice = input("\nΚΟΡΩΝΑ - ΓΡΑΜΜΑΤΑ ,για το ποιός παιζει πρώτος καλή τύχη.\n0 : ΚΟΡΩΝΑ\n1 : ΓΡΑΜΜΑΤΑ\n\ncommand: ")
    while (True):
        if (choice!='0' and choice !='1'):
            choice = input ("ΠΛΗΚΤΡΟΛΟΓΗΣΕ ΞΑΝΑ, ΑΥΤΗ ΤΗ ΦΟΡΑ ΣΩΣΤΑ.. : ")
        else :
            break
    return choice




def showHand(player,diction):
    for letter in range (0,7):
        print(player.hand[letter] + "," + str(diction[player.hand[letter]])+ "  ", end='', flush=True)
    
    print("")  



def showStuf(player,sak,diction):

    print("ΠΑΙΖΕΙ : " + player.name)
    print("ΣΚΟΡ : " + str(player.points))
    print("ΤΟ ΣΑΚΟΥΛΙ ΕΜΠΕΡΙΕΧΕΙ : " + str(len(sak.letters)) + " ΓΡΑΜΜΑΤΑ")
    print("ΓΑΜΜΑΤΑ ΣΤΟ ΧΕΡΙ : " , end='', flush=True)
    
    showHand(player,diction)

    print('\nΜΠΟΡΕΙΣ ΑΚΟΜΑ ΝΑ ΠΑΤΗΣΕΙΣ p ΓΙΑ ΝΑ ΑΛΛΑΞΕΙΣ ΓΡΑΜΜΑΤΑ ΚΑΙ q ΓΙΑ ΝΑ ΒΓΕΙΣ\n')



def showRound(roundCount):
    print("\n------------------------------ ROUND:" + str(roundCount) + " ------------------------------\n")




def scoreToTxt(player):
    text_file = open("scores.txt", "a")
    text_file.write(player.name+"'s"+" score " + str(player.points) + "\n")
    text_file.close()





def botPlay(difficulty,player,diction,sak):
    lets=''.join(player.hand)
    isThereAnyWord=False
    if difficulty=='0':
        for i in range(3,7):
            for w in permutations(lets, i):
                word1=''.join(w)
                if (wordIsValid2(word1,diction.wordDictionary)):
                    isThereAnyWord=True                                
                    player.updatePlayerPoints(word1,diction.wordDictionary)
                    sak.throw(word1,player.hand)
                    print('Θα παίξω τη λέξη: ', word1)
                    print("ΕΓΚΥΡΗ ΛΕΞΗ! ΑΞΙΑ : " + str(diction.findValue(word1)))
                    return
        print('ΝΑ ΠΑΡΕΙ, ΔΕΝ ΒΡΗΚΑ ΟΥΤΕ ΜΙΑ ΛΕΞΗ!')
        player.hand = sak.change(player.hand)           
        return               
                    
                        
    elif difficulty=='1':
        maxP=0
        isThereAnyWord=False
        for i in range(2,7):
            for w in permutations(lets, i):
                word1=''.join(w)
                if (wordIsValid2(word1,diction.wordDictionary)):
                    if diction.findValue(word1)>maxP:
                        maxP=diction.findValue(word1)
                        bestWord=word1
                        isThereAnyWord=True
        if isThereAnyWord==True:                
            player.updatePlayerPoints(bestWord,diction.wordDictionary)
            sak.throw(bestWord,player.hand)
            print('ΘΑ ΠΑΙΞΩ ΤΗ ΛΕΞΗ: ', bestWord)
            print("ΕΓΚΥΡΗ ΛΕΞΗ! ΑΞΙΑ : " + str(diction.findValue(bestWord)))
        else:
            print('ΝΑ ΠΑΡΕΙ, ΔΕΝ ΒΡΗΚΑ ΟΥΤΕ ΜΙΑ ΛΕΞΗ!')
            player.hand = sak.change(player.hand)                     
        return             
                   
        
                
            


########################### MAIN GAME FUNCTIONS, AND OBJECT CREATION #########################################         


def play(difficulty):
    givenName = input("\nΚΑΛΩΣΗΛΘΕΣ ΣΤΟ SCRABLE, ΔΩΣΕ ΟΝΟΜΑ: ")
    dict1 = Dictionary()
    p1 = Player(givenName)
    p2 = Player('MARIA')
    sak1 = SakClass()

    yourTurn = headsOrTails(getChoice())
    dontWantToQuit = True
    canGiveMore = True
    roundCounter = 1

    showRound(roundCounter)
    sak1.shuffleSak()
    p1.fullHandWithLetters(sak1)
    p2.fullHandWithLetters(sak1)


    while(True):

        if (roundCounter>1): sak1.shuffleSak()

        if(yourTurn):

            
            showStuf(p1,sak1,dict1.letterValue)
            dontWantToQuit = giveAWordPassOrQuit(p1,dict1,sak1)
            canGiveMore = p1.fullHandWithLetters(sak1)
            yourTurn = False

        else:

            
            showStuf(p2,sak1,dict1.letterValue)
            #dontWantToQuit = giveAWordPassOrQuit(p2,dict1,sak1)
            botPlay(difficulty,p2,dict1,sak1)
            canGiveMore = p2.fullHandWithLetters(sak1)
            yourTurn = True

        if (dontWantToQuit==False):
            scoreToTxt(p1)
            break
        if (canGiveMore== False):
            scoreToTxt(p1)
            print("ΤΕΛΕΙΩΣΑΝ ΤΑ ΓΡΑΜΜΑΤΑ ΣΤΟ ΣΑΚΟΥΛΙ, ΤΟ ΠΑΙΧΝΙΔΙ ΤΕΛΕΙΩΣΕ")
            break
                
        roundCounter = roundCounter +1
        showRound(roundCounter)


def showGuide():
    print("\n                                  ΤΙ ΕΙΝΑΙ ΤΟ SCRABLE\n")
    
    print("Στόχος του παιχνιδιού είναι να συγκεντρώσει ο παίκτης τη μεγαλύτερη δυνατή βαθμολογία")
    print("σχηματίζοντας λέξεις τις οποίες τοποθετεί σε ένα πίνακα σύμφωνα με προκαθορισμένους κανόνες.")
    print("Οι λέξεις σχηματίζονται με γράμματα που ο παίκτης τραβάει από μία κληρωτίδα")
    print("και η αξία της κάθε λέξης καθορίζεται:")
    print("α) από τα γράμματα που περιέχει")
    print("β) από τη θέση στην οποία θα τοποθετηθεί.")
    print("Αυτό σημαίνει ότι οι λέξεις δεν έχουν πάντα την ίδια αξία,")
    print("εφόσον η επιλογή ορισμένων σπάνιων γραμμάτων μπορεί να αυξήσει τη βαθμολογία τους.")
    
    print("\n                               ΠΩΣ ΠΑΙΖΕΤΑΙ ΤΟ SCRABLE ΜΑΣ\n")

    print("Το πρόγραμμα κληρώνει 7 γράμματα στον παίκτη από το «σακουλάκι» και 7 για τον Η/Υ. ")
    print("Στη συνέχεια περιμένει τον παίκτη να πληκτρολογήσει μια λέξη με τα γράμματα που διαθέτει")
    print("Ο παίκτης σε κάθε ενεργό γύρο, έχει τις εξής επιλογές:")
    print("α) Να πληκτρολογήσει την λέξη που επιθυμεί βάσει των γραμμάτων στο χέρι του.")
    print("β) Να πληκτρολογήσει 'p'(pass) ,σε περίπτωση που θέλει να αντικαταστήσει το χέρι του")
    print("με καινούρια γράμματα και να κάνει pass τον γύρο του")
    print("γ) Να πληκτρολογίσει 'q'(quit), σε περίπτωση που θέλει να σταματήσει το παιχνίδι")
    print("και να επιστρέψει στο αρχικό Menu")

    input("\n\nπληκτρολογήστε οτιδήποτε για να γυρίσετε στο Menu...")

def showScores():

    with open("scores.txt",encoding='utf-8',mode='r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    print(" ")
    for score in content: print(score)
    
    input("\n\nπληκτρολογήστε οτιδήποτε για να γυρίσετε στο Menu...")


def selectDifficulty():
    while(True):
        
        gameMode= input('ΠΛΗΚΤΡΟΛΟΓΙΣΕ 0 ΓΙΑ ΕΥΚΟΛΟ ΠΑΙΧΝΙΔΙ ΚΑΙ 1 ΓΙΑ ΔΥΣΚΟΛΟ: ')
        if gameMode=='0':
            print('\n******TΟ ΠΑΙΧΝΙΔΙ ΘΑ ΕΙΝΑΙ ΕΥΚΟΛΟ!*******')
            return gameMode
        elif gameMode=='1':
            print('\n******TΟ ΠΑΙΧΝΙΔΙ ΘΑ ΕΙΝΑΙ ΔΥΣΚΟΛΟ!*******')
            return gameMode
        else: print('ΛΑΘΟΣ ΣΤΟΙΧΕΙΟ!')     
        
            





    
    



    
