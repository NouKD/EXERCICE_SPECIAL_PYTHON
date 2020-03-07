nombre = ''

nombres = []
i = 0
while i < 20:
    nombre = input("Entrez le nombre numero {0} : ".format(i+1))
    if nombre.isdigit():
        nombres.append(int(nombre))
        i += 1

plus_grand = nombres[0]

for i in nombres:
    if i > plus_grand:
        plus_grand = i

print("Le plus grand etait", plus_grand)