'''
Created on Dec 5, 2012

@author: dontommy
'''
# floating point (decimal int)
xfloat = 5.32
print(xfloat)

# integer variable
xint = 5
print(xint)

# string variable
xstring = "a string"
print(xstring)

# tuple (array that cant be changed
xtuple = ('January','February','Marts','April')
print(xtuple)

# list [normal array]
xlist = ['Fuck','Tis','And','Lort']
print(xlist)

# dictionary {array with values and keys}
xdic = {'Test 1': 'Shitty','Test 2': 'Pissy'}
print(xdic)

# for loop for going trough a list
for item in xlist:
    print(item)
    
# for loop for going trough a dictionary
for item in xdic:
    print(item+" : "+xdic[item])

# add to list
xlist.append("python")
print(xlist)

# remove item from list
xlist.remove("python")
print(xlist)

# add to dictionary
xdic['newkey'] = "newvalue"
print(xdic)

# remove item from dictionary
del xdic['newkey']
print(xdic)

# defining a function and calling it
def xmoms(thevar):
    moms = thevar * 1.25
    return moms
x_moms = xmoms(100)
print(x_moms)

# while loop for counting to 10
xtest = 1
while xtest <= 10:
    print(xtest)
    xtest = xtest+1
