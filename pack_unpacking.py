print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

print(*numbers)

print("abc")

print(*"abc")

def add(x,y):
    return x + y
print(add(10,10))     

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)
print(add(1,2,3,4,5,6,7,8,9))

def about(name ,age ,likes):
    sentence = "Meet {}!They are {} years old and they like {}".format(name,age,likes)
    return sentence
dictionary = {"name":"Vedant","age":23,"likes":"Cricket"}
print(about(**dictionary))

dictionary = {"age":23,"name":"Vedant","likes":"pthyon"}
print(about(**dictionary))




def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
print(foo(sakshi = "female",vedant = "male"))

