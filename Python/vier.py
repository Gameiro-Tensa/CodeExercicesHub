# Ecrire un programme Python qui permet d'echanger le contenu de deux entiers A et B 
# saisir par l'utilisateur  et afficher ces entiers apres l'echange

zahl1 = int(input("Bitte gibt der erste Zahl ein: "))
zahl2 = int(input("Bitte gibt der zweite Zahl ein: "))


zahl3 = zahl2
zahl2 = zahl1
zahl1 = zahl3

print(f"Die eingegebene und ausgetauschte Zahl sind Zahl: {zahl1} und zahl2: {zahl2}")