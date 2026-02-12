import random

words = ["python", "developer", "internship", "programming", "computer"]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("You have 6 incorrect attempts.")
print("_ " * len(secret_word))

# Game loop
while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print(f"Attempts left: {attempts}")

    # Display current word status
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    # Check if user won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

# If attempts finish
if attempts == 0:
    print("😢 Game Over!")
    print("The word was:", secret_word)
