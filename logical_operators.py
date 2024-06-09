x=10
y=20
if not y < x:
    print("it worked")

c=10
d=5
if c>8 and d>1:
    print("It Worked")    #for and operator both the condition should be true

c=10
d=5
if c>=10 and d>1:
    print("It Worked")

c=10
d=5
if c>10 and d>1:
    print("It Worked")
else:
    print("It won't work")

c=10
d=5
if not(c>10 and d>1):
    print("It Worked")

c = 5
d = -1
if c > 1 or d >1:
    print("It Worked")    #if either one or both condition should be true

c=5
d=-1
if not(c>100 or d>100):
    print("It Worked")

c = 6
d = 2
if(c > 5 and d > 5)or(c > 1 and d > 1):
    print("It Worked")