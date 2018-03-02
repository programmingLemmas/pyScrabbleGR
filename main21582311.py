
'''
Αυτή είναι η βασική μας συνάρτηση. Οι συναρτήσεις που καλούνται από εδώ
βρίσκονται στο αρχείο myFunctions21582311.py, κάτω απο την κόκκινη γραμμή.

!ΠΡΟΣΟΧΗ!
Το πρόγραμμά μας δημιουργεί κάθε φορα που εκκινεί μόνο του το αρχείο
Greek7.txt, αφού του έχει δοθεί το Greek.txt(το οποιο επισυναπτεται).

Πάνω από την κόκκινη γραμμή βρίσκονται όλες οι υπόλοιπες συναρτήσεις που
καλούνται εκει.

Για το παιχνίδι με τον υπολογιστή υλοποιήθηκε ο αλγόριθμος MIN Letters
και ο SMART και μπήκαν αντίστοιχα στις κατηγορίες εύκολο και δύσκολο.

Η default δυσκολία είναι το εύκολο παιχνίδι.

Αφού ο παίκτης επιλέξει κάτι από το αρχικό μενού καλούνται οι συναρτήσεις
που αναφερθηκαν, κατω απο την κοκκινη γραμμή.

Αυτές καλούν τις συναρτήσεις πάνω απο την κόκκινη γραμμή και δημιουργούν
αντικείμενα.

Χρησιμοποιούνται οι κλάσεις:

SakClass που υλοποιεί το σακούλι του φυσικού
παιχνιδιού και μπορει να ανακατέβεται, να παίρνει, να πετάει και να
αλλάζει γράμματα.

Player που υλοποιεί τον παίκτη του φυσικού παιχνιδιού, ο οποίος
έχει το όνομα του, τα γράμματα στο χέρι του, του πόντους του και μπορεί
να αλλάζει τους πόντους του και τα γράμματά του.

Dictionary που υλοποιεί το φυσικό λεξικό αλλά και περιέχει
τους κανόνες σε σχέση με την αξία των γραμμάτων. Μπορεί να βρίσκει ακόμα,
τις αξίες των λέξεων.

'''







from  myFunctions21582311 import play,showGuide,showScores,selectDifficulty,createGreek7FromGreek

createGreek7FromGreek()
difficulty='0'

while(True):

    print("\n*********************** SCRABLE ***********************")
    print("-------------------------------------------------------")
    print("\n                      1 : ΠΑΙΧΝΙΔΙ")
    print("                      2 : ΟΔΗΓΙΕΣ")
    print("                      3 : ΣΚΟΡ")
    print("                      4 : ΔΥΣΚΟΛΙΑ")
    print("                      q : ΕΞΟΔΟΣ")
    print("\n-------------------------------------------------------\n")

    choice = input ("command: ").upper()

    if(choice=='1'):
        play(difficulty)

    elif(choice=='2'):
        showGuide()
        

    elif(choice=='3'):
        showScores()

    elif(choice=='4'):
        difficulty = selectDifficulty()
                

    elif(choice=='Q'):
        print( "\nΕΥΧΑΡΙΣΤΟΥΜΕ ΠΟΥ ΔΟΚΙΜΑΣΕΣ ΤΟ SCRABLE ΜΑΣ")
        break

    else:
        print("\nΞΑΝΑΠΡΟΣΠΑΘΗΣΕ.. ΣΩΣΤΑ ΑΥΤΗ ΤΗ ΦΟΡΑ")
        
    





    
        
