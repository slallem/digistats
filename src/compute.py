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

print("num, permutation, resultat, departements, adjacents, adjacent2a2, tripoint")
i = 0
for uperm in ulperms:
    i += 1
    deps = 0
    adj = 0
    adj2a2 = 0
    tripoint = 0
    print("{},{},{},{},{},{},{}".format(i, uperm, int(int(uperm) / 3), deps, adj, adj2a2, tripoint))

# Test
print(departements.departements_adjacents["33"])

