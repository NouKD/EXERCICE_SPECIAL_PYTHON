heures = int(input(" le nombre d heures"))
prix = float(input("le prix unitaire d une heure"))
montant = 0
if heures <= 39:
    montant = 0
elif heures < 45:
    montant = (heures-39)*(prix*1.5)
elif heures < 50:
    montant = (5*prix*1.5)+(heures-44)*(prix*1.75)
else:
    montant = (5*prix*1.5)+(5*prix*1.75)+(heures-49)*(prix*2)
print("le montant des heures supplementaires est : ", montant)