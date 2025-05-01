# Ecrire un Programm Python qui demande deux m und n a l'utilisateur et l'informe ensuite si le produit de ces deux nombres
# est positif ou negatif. on inclut dans le Programme le cas ou le produit est nul


m = int(input("Bitte geben Sie eine Zahl ein: "))
n = int(input("Bitte geben Sie eine Zahl ein: "))

product = m * n

if (product > 0):
    print(f"Das Product ist positif {product}")
elif (product < 0):
    print(f"Das Product ist negatif {product}")
else:
    print(f"Das Product ist null {0}")