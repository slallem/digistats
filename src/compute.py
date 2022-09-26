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


for uperm in uperms:
    print("{}, {}".format(uperm, int(int(uperm)/3)))

