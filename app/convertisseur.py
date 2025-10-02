inch_cm = 2.54
cm_inch = 0.394


def fonction_choix():
    choix = ""
    cv_cm = 0 #permet d'initialisé une variable qui sera utilisé dans une condition
    cv_p = 0 #idem

    while choix == "":
        choix = input("Voulez-vous convertir les pouces ou les cm, tapez p ou cm, pour quitter, tappez q : ")
        if choix == "p":
            nb_p = input("Combien de cm souhaitez-vous convertir en pouce : ")
            try:
                cv_p = float(nb_p)
            except:
                print("ce n'est pas un chiffre")
            print (f"ce la fait {cv_p*cm_inch} pouces")
        elif choix == "cm":
            nb_cm = input("Combien de pouce souhaitez-vous convertir en cm : ")
            try:
                cv_cm = float(nb_cm)
            except:
                print("ce n'est pas un chiffre")
            print (f"Cela fait {cv_cm * inch_cm} cm")
        elif choix == "q":
            break
        else:
            print("je n'ai pas compris votre choix")
            choix = ""
        choix = "" #pour relancer la boucle while
        
    return cv_cm, cv_p

fonction_choix()