def permisSup(p, c, v, a) :
    pointsPerdus = p + 3*c + 5*v + 10*a
    nbrePermis = pointsPerdus/100.0
    return 200*nbrePermis

poule = int(input("Combien de poules ?"))
chien = int(input("Combien de chiens ?"))
vache = int(input("Combien de vaches ?"))
amis = int(input("Combien d'amis ?"))

payer = permisSup(poule, chien, vache, amis)

print("\nA payer :", end=' ')
if payer == 0:
    print("rien à payer")
else :
    print(payer, "euros")