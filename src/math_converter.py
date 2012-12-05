#! /usr/bin/python3
'''
Created on Nov 29, 2012

@author: dontommyc
'''
print("Hello math world ")
var = 1
while var == 1:
    mode = input("For hex type 1, for bin type 2, Dec to Hex Bin Oct type 3 Prog-exit type 4, here:")
    mode = int(mode)
    print("  ")
    if mode == 1:
        n = input('Input a Hex nr here:>')
        a = int(n, 16)
        print("Hex to Decimal =:",n, "=",a)
    if mode == 2:
        n = input('Input a Binary nr here:>')
        if n != int(n,2):
            print("lort")
        else:
            b = int(n, 2)
            print("Bin to Decimal =:",n, "=",b)
    if mode == 3:
        y = input('Type a decimal number:')
        y = int(y)
        b = bin(y)
        x = hex(y)
        o = oct(y)
        print("Decimal=",y, "Bin=",b, "Hex=",x, "Octal=",o)
    if mode == 4:
        var = 0
        print("Program Exit")