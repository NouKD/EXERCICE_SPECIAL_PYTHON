nombre = 1
somme = 0
montant_verse = ''

while 1:
    nombre = input("Entrez le montant : ")
    if nombre.isdigit():
        if int(nombre) == 0:
            break
        somme += int(nombre)

print("\nVous devez:", somme, "euros\n")

while not montant_verse.isdigit():
    montant_verse = input("Montant verse: ")

reste = int(montant_verse) - somme

nb_10_euros = reste // 10
nb_5_euros = (reste % 10) // 5
nb_1_euros = (reste % 10) % 5

print("\nMonnaie a rendre: ")
print("Billets de 10 €:", nb_10_euros)
print("Billets de 5  €:", nb_5_euros)
print("Pieces  de 1  €:", nb_1_euros)