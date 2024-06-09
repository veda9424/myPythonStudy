a = 250

def f1():
    global a 
    a = 100   #global
    print(a)

def f2():
    a = 50   #local
    print(a)

print(f1())
print(f2())
print(a)

a = [1,2,3]

def f1(): 
    a[0] = 5   #global
    print(a)

def f2():
    a = 50   #local
    print(a)

print(f1())
print(f2())
print(a)

