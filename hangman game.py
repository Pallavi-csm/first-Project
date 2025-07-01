import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'algorithm']
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def hangman():
    print("🎮 Welcome to Hangman Game!")
    secret_word = choose_word()
    guessed_letters = set()
    attempts = 6  

    while attempts > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess.")
            attempts -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You guessed the word:", secret_word)
            break
    else:
        print("\n💀 Game Over! The word was:", secret_word)

hangman()
