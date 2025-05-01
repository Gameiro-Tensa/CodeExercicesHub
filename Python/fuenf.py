# Ecrire un Programme Python qui permet a l'utilisateur d'afficher si un nombre entier saisi au clavier est pair ou impair 

number = int(input("Bitte eine Zahl eingeben: "))

if (number % 2 == 0 ):
    print(f"Der eingegbene Zahl {number} ist gerade")
else:
    print(f"Der eingegebene Zahl  {number} ist ungerade")