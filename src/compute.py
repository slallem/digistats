#!/usr/bin/python3

import itertools


digits = '71721075'
chars = [*digits]
perms = list(itertools.permutations(chars, len(chars)))

print("Traitement de %s" % chars)
print("Il existe {} permutations possibles".format(len(perms)))

uperms = set()
for perm in perms:
    uperms.add("".join(perm))
print("Du fait de chiffres apparaissant plusieurs fois, il n'y a que {} combinaisons uniques possibles".format(len(uperms)))

ulperms = list(uperms)
ulperms.sort()

print("num, permutation, resultat, departements, adjacents, adjacent2a2, tripoint")
iter = 0
for uperm in ulperms:
    iter += 1
    print("{},{},{},?,?,?,?".format(iter, uperm, int(int(uperm)/3)))

