# Eecrire un Programme Python qui permet de calculer la valeur absolue d'un entier saisi par l'utilisateur 

zahl = int(input("Bitte geben Sie eine Zahl ein: "))

if (zahl >= 0):
    print(f"Der Absolutwert der Zahl ist {zahl}")
else:
    zahl = zahl * (-1)
    print(f"Der Absolutwert der Zahl ist {zahl}")