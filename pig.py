#get the sentence from the user

original = input("Get the sentence from the user: ").lower().strip()

#split sentence into words

words = original.split()

#loop through words and convert to pig latin

new_words=[]

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
    
# stick words back together
output =  " ".join(new_words)

print(output)