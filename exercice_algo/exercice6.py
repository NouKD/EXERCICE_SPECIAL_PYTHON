nombre = ''

while not nombre.isdigit():
    nombre = input("Entrez un nombre: ")

nombre = int(nombre)
resultat = 0

while nombre >= 1:
    resultat += nombre
    nombre -= 1

print("La somme des entiers =", resultat)