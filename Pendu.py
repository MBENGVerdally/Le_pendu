## Le pendu


import random
def randomaccesword():

    wordlist = ["banana", "strawberry", "kiwi"]
    wordchose = random.choice(wordlist)
    return wordchose
word = randomaccesword()
print(word)

guessword =  random.choice(wordlist)
maskedword = " _ " *
len (guessword)
print(guessword)