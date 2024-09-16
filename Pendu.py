import random

def randomaccesword():
    wordlist = 0
    wordlist = ["banana", "strawberry", "kiwi", "orange", "apple"]
    wordchose = random.choice(wordlist)
    return wordchose

word = randomaccesword()
maskedword = ["_" for _ in word]
tentatives = 5
letters_guessed = []

print("Mot masqué :", " ".join(maskedword))

while tentatives > 0 and "_" in maskedword:
    guess = input("Devinez une lettre : ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Veuillez entrer une seule lettre.")
        continue

    if guess in letters_guessed:
        print("Vous avez déjà deviné cette lettre.")
        continue

    letters_guessed.append(guess)
    
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                maskedword[index] = guess
        print("Bonne réponse !")
    else:
        tentatives -= 1
        print(f"Lettre incorrecte. Il vous reste {tentatives} tentatives.")
    
    print("Mot masqué :", " ".join(maskedword))

if "_" not in maskedword:
    print("Félicitations ! Vous avez gagné !")
else:
    print(f"Désolé, vous avez perdu. Le mot était '{word}'.")