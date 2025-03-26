import random

words = ["python", "hangman", "computer","codealpha", "programming"]
word = random.choice(words)
guessed = set()
attempts = 6

print("Hint: The word has", len(word), "letters.")

while attempts > 0:
    display = "".join([letter if letter in guessed else "_" for letter in word])
    print("\nWord:", display)
    
    if "_" not in display:
        print("You win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.add(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" in display:
    print("Game over! The word was:", word)