from random import choice

question =["why is the sky blue?","why is there face on the moon?","Where are all the dinasours?"]

question = choice(question)
answer = input(question).strip().lower()

while answer!="just because":
    answer = input("why?: ").strip().lower()

print("Oh Okay....")