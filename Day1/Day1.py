#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:20:57 2020

@author: aashishk29
"""
f = open("input.txt")
data = f.read().split("\n")[:-1]
data = [int(i) for i in data]
data.sort()


def productSearch(arr,start,end,key):
    if start == end: #then there is no solution!
        return 0
    startVal = arr[start]
    endVal = arr[end]
    sumVals = startVal+endVal
    if sumVals == key:
        print(startVal)
        print(endVal)
        return startVal*endVal
    elif sumVals > key:
        return productSearch(arr,start,end-1,key)
    else:
        return productSearch(arr,start+1,end,key)
        
def biProductSearch(arr,key):
    return productSearch(arr,0,len(arr)-1,key)

print("Product of Two Numbers is:",biProductSearch(data,2020))

def triProductSearch(arr,key):
    for i in range(len(arr)):
        val = arr[i]
        newArr = arr[:]
        newArr.pop(i)
        remainingProduct = biProductSearch(newArr,key-val)
        if remainingProduct:
            print(val)
            return remainingProduct*val
        else:
            continue

print("Product of Three Numbers is:",triProductSearch(data,2020))
