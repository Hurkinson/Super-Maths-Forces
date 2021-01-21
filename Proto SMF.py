import random
import sys


# --------- TODO ----------------
#
# * controles Try/excep
# * integration patchnote entre titre et menu
# * clear l'ecran apres selection dans le menu
# * def soustraction():
# * def multiplication():
# * def division():

title = "SUPER MATHS FORCES !     "
version = "v. 1.1"
        
        
line_1= 84*"-"
line_2= 0
line_3= 90*"-"
spc=round(((len(line_3)-len(title))/2))*" "
spc2=((len(spc)-len(version))-1)*" "

add_score = 0
sous_score = 0
mult_score = 0
div_score = 0

#print(patchnote)



def Additions ():
    
    play = True
    counter = 0
    err = 0
    score = counter - err
    total_counter = 0
    total_score = 0
    while play:
         
        try_b = [1,2,3,4,5,6,7,8,9,10]
        # try_b = list(range(1, 11))
        
        a = int(input("choisi la table d'addition sur laquelle tu veux t'entrainer: "))    
        
        while try_b:                                                           # boucle propositions equations
            
            b = random.choice(try_b)
            target = a + b
            while True:                                                        # boucle des essais utlisateurs
                s = input("\n{0} + {1} = ".format(a,b))
                # s = input("\n{} + {} = ".format(a,b))
                # s = input(f"\n{a} + {b}")
                try:
                    x = int(s)
                    
                except ValueError:     
                    if s == "q":
                        sys.exit()
                    elif s == "m":
                        print("\n\n Tu as eu un score de : {0} !\n Beau travail,\n\nA bientot !".format(total_score))
                        return
                    print("Voulez-vous arreter ?/nm pour menu, q pour quitter")
                    
                else:
                    if x < target:
                        print("trop petit")
                        counter+=1
                        err +=1
                        print("\nEssai numero {0}".format(counter))
                    elif x > target:
                        print("Trop grand")
                        counter+=1
                        err +=1
                        print("\nEssai numero {0}".format(counter))
                                            
                    else:
                        if err == 0:
                            print("\nBINGO ! tu as réussi DU PREMIER COUP ! \nBravo !")
                            counter+=1
                            try_b.pop(try_b.index(b))
                                               
                        else:
                            print("\nBravo ! tu as réussi au bout de {0} tentatives.".format(err))
                            counter+=1
                            try_b.pop(try_b.index(b))
                        break
            
        cont = input("\n\nVeux-tu continuer oui/non ? ")  
        
        if "oui" in cont:
            total_counter+= counter
            total_score+= score
            counter = 0
            err = 0
            continue
        
        elif "non" in cont:
            print("\n\n Tu as eu un score de : {0} !\n Beau travail,\n\nA bientot !".format(total_score))
            play = False
            
            return 


def menu():
    
    entry_1 = " 1. Additions"
    entry_2 = " 2. Soustractions (pas pret encore)"
    entry_3 = " 3. Multiplications (pas pret encore)"
    entry_4 = " 4. Divisions (pas pret encore)"
    entry_5 = " 5. 'q' pour quitter"
    
    menu = [entry_1,entry_2,entry_3,entry_4,entry_5]
      
    while True:
                      
        print("\n\n\n\t\t\t\t+{0}+\n\t\t\t  /{1}{2}{3}{4}\\\n \t\t\t+{5}+\n\n\n".format(line_1,spc,title,version,spc2,line_3))

        print(*menu, sep="\n\n")        
        user_choice = input("\n\nChoisi sur quoi tu veux t'entrainer 1,2,3 ou 4 ? : ")
        try:
            user_choice = int(user_choice)
            
        except ValueError:
            if user_choice == "q":
                sys.exit()
            pass
        if user_choice == 1:
            Additions()    
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        
        
menu()
