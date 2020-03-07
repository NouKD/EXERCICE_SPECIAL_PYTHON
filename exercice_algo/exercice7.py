nombre = ''
nombres = []

while not nombre.isdigit():
    nombre = input("Entrez un nombre: ")

nombre = int(nombre)
resultat = 1

for i in range(1, nombre+1):
    resultat *= i
    nombres.append(str(i))

print(" x ".join(nombres), end=" = ")
print(resultat)