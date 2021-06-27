mdp = int(input("entrez votre mot de passe:"))
a = 0
run = True 

while run is True :

    if a == mdp : 
        print("Mot de passe trouvé :", a)
        run = False 

    else : 
        a += 1