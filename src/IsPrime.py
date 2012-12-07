#!/usr/bin/env python3
'''
Created on Dec 6, 2012

@author: dontommy
'''
import time

def isprime(n):
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

print(isprime(6))
tidnu = time.time()
xlist = []
for prim in range(3,10000,2):
    thisprime = True
    for prim2 in range(2,prim-1):
        if prim%prim2==0:
            thisprime = False
    if thisprime:
        xlist.append(str(prim))

thelist = '\n'.join(xlist)

tidefter = time.time()
sluttid = tidefter-tidnu
OutFile = open('/home/dontommy/prim.txt','w')
OutFile.write("The program took: "+str(sluttid)+" secounds to run\n")
OutFile.write(thelist)

print("DONE!")