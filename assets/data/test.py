#! /usr/bin/env python2

import json
import random

keys = [u'bv', u'preterit', u'pp', u'trad']

def shuffle (n):
    r = {}
    for i in xrange(n):
        id = int(random.random()*n)
        while id in r.keys():
            id = int(random.random()*n)
        r[id] = i
    return [ii for i,ii in r.items()]

def dumpLine (l):
    return "       {:25s}{:25s}{:25s}{:25s}".format(*tuple([' / '.join (l[ii]) for ii in keys]))

with open('verbs.json') as f:
    content = f.read ()
    verbs = json.loads(content)

    l = len(verbs)
    r = shuffle(l)

    n = raw_input("Combien de verbes ? (max: %d, defaut: 20)  " % l)
    if len(n.strip()) == 0:
        n = 20
    else:
        print n
        n = int(n)
    if n > l:
        n = l
    r = r[:n]
    l = n


    miss = []
    num = 0

    for id in r:
        num += 1
        guess = int(random.random()*len(keys))

        print "{:2d}/{:2d}  base verbale             preterit                 present perfect          francais".format(num, l)
        print "       " + " "*(25*guess) + "{:25s}".format(", ".join(verbs[id][keys[guess]]))

        guess = keys[guess]

        missed = False
        indent = -1
        for i in keys:
            indent += 1
            if i == guess:
                continue
            rep = raw_input ("     " + " "*(25*indent) + "> ")
            if not missed and rep not in verbs[id][i]:
                missed = True
                miss.append(id)

        if missed:
            print "\x1B[31m" + dumpLine (verbs[id]) + "\x1B[0m"

        print "\n"


    print "\x1B[31mFini !        %d/%d\x1B[0m" % (l-len(miss), l)
    for m in miss:
        print dumpLine (verbs[m])
