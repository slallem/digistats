#!/usr/bin/python3

import itertools
import departements


digits = '71721075'
chars = [*digits]
perms = list(itertools.permutations(chars, len(chars)))

print("Traitement de %s" % chars)
print("Il existe {} permutations possibles".format(len(perms)))

uperms = set()
for perm in perms:
    uperms.add("".join(perm))
print("Du fait de chiffres apparaissant plusieurs fois, il n'y a que {} permutations uniques".format(len(uperms)))

ulperms = list(uperms)
ulperms.sort()

f = open("output.csv", "w")
f.write("num, permutation, resultat, departements, valides, creuse, adjacents, tripoint\n")

i = 0
nb_valides = 0
nb_creuse = 0
for uperm in ulperms:
    i += 1
    resdiv3 = int(int(uperm) / 3)
    deps = departements.decode_depts(str(resdiv3))
    valides = True if departements.dep_valides(deps) else False
    if valides:
        nb_valides += 1
    creuse = True if "23" in deps else False
    if creuse:
        nb_creuse += 1
    adj2 = 0
    adj3 = ""
    if valides:
        # Adjacences 2 à 2
        adjpot2 = list(itertools.combinations(deps, 2))
        for item in adjpot2:
            if departements.adjacents2(item[0], item[1]):
                adj2 += 1
        # Conjonction de 3 départements (Tripoint)
        adjpot3 = list(itertools.combinations(deps, 3))
        for item in adjpot3:
            if departements.adjacents3(item[0], item[1], item[2]):
                items = list(item)
                items.sort()
                adj3 += "-".join(items)
    f.write("{},{},{},{},{},{},{},{}\n".format(i, uperm, resdiv3, "-".join(deps), valides, creuse, adj2, adj3))

print("")
print("Valides total: {}".format(nb_valides))
print("Creuse total: {}".format(nb_creuse))

# Test
#print(departements.departements_adjacents["33"])
# Test
#print(departements.decode_depts("112345"))
#print(departements.decode_depts("12345"))

#print(list(itertools.combinations(["11", "22", "33", "44"], 2)))
#print(departements.adjacents("90", "70"))