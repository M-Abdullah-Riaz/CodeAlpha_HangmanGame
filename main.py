import random

print("===== Welcome To Hangman! =====")

words = [
    "computer",
    "intelligence",
    "technology",
    "development",
    "future"
]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

while attempts > 0:

    # Display the word
    word_complete = True

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            word_complete = False

    print()

    # Check if player has won
    if word_complete:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Player input
    entered_letter = input("Enter a letter: ").lower()

    # Input validation
    if len(entered_letter) != 1 or not entered_letter.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Already guessed
    if entered_letter in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(entered_letter)

    # Correct or wrong guess
    if entered_letter in secret_word:
        print("✅ Correct Guess!\n")
    else:
        attempts -= 1
        print(f"❌ Wrong Guess! Attempts Left: {attempts}\n")

# Lose condition
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)