def about(name,age,likes):
    sentence = "Meet{}! They are{}years old and they like  {}".format(name,age,likes)
    return sentence
print(about("Jack","23","Python"))


def about(name,age,likes = "Python"):
    sentence = "Meet{}! They are{}years old and they like {}".format(name,age,likes)
    return sentence
print(about("Jack","23","Football"))
