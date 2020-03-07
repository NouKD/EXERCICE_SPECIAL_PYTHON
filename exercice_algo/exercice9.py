nombre = ''

nombres = []
i = 1
while 1:
    nombre = input("Entrez le nombre numero {0} : ".format(i))
    if nombre.isdigit():
        if int(nombre) == 0:
            break
        nombres.append(int(nombre))
        i += 1

plus_grand = nombres[0]

for i in nombres:
    if i > plus_grand:
        plus_grand = i

print("Le plus grand etait", plus_grand)