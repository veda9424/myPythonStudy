for i in range(1,10):
    print(i)

vowels = 0
consonants = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter==" ":
        pass
    else:
        consonants = consonants + 1
print("there are {} vowels".format(vowels))
print("There are{} cnsonants".format(consonants))

students = {
    "male":["Tom","Charlie","Harry","Frank"],
    "female":["Sarah","Sakshi","Emily","Sonal"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)