import random

words = ["python", "laptop", "doctor", "garden", "planet"]

secret_word = random.choice(words)

print("Welcome to Hangman!")
print("The secret word has", len(secret_word), "letters.")


guessed_letters = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    # Build the display, e.g. _ _ r _ _ n
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # Check for a win
    if "_" not in display:
        print("You won! The word was", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type just one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed", guess, "- try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("Sorry,", guess, "is not in the word.")

if wrong_guesses == max_wrong:
    print("Game over! The word was", secret_word)