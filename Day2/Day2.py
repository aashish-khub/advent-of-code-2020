#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:02:06 2020


@author: aashishk29
"""
f = open("input.txt")
data = f.read().split("\n")[:-1]
import re

decomp = re.compile(r'(\d+)[-](\d+) (\w): (\w+)')

#print(decomp.search(data[0]).group(0))

def passwordValidOne(l):
    minCount = int(l[0])
    maxCount = int(l[1])
    key = l[2]
    pw = l[3]
    keyCountInPW = pw.count(key)
    if keyCountInPW >= minCount:
        if keyCountInPW <= maxCount:
            return True
    return False

pwChecks = []
validCountOne = 0
# valids = []

for s in data:
    l = []
    for i in [1,2,3,4]:
        l.append(decomp.search(s).group(i))
    pwChecks.append(l)
    # print(pwChecks)
    if passwordValidOne(l):
        validCountOne += 1
        # valids.append(l)

print(validCountOne)

def passwordValidTwo(l):
    indexOne = int(l[0])
    indexTwo = int(l[1])
    key = l[2]
    pw = l[3]
    
    b1 = (pw[indexOne-1] == key)
    b2 = (pw[indexTwo-1] == key)
    
    return b1^b2

pwChecksTwo = []
validCountTwo = 0

for s in data:
    l = []
    for i in [1,2,3,4]:
        l.append(decomp.search(s).group(i))
    pwChecksTwo.append(l)
    # print(pwChecks)
    if passwordValidTwo(l):
        validCountTwo += 1

print(validCountTwo)