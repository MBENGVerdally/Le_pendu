## Le pendu


import random
def randomaccesword():

    wordlist = ["banana", "strawberry", "kiwi"]
    wordchose = random.choice(wordlist)
    return wordchose
word = randomaccesword()
print(word)

guessword =  random.choice(wordlist)
maskedword = ["_" for _ in guessword]
len (guessword)
print(" ".join(maskedword))

