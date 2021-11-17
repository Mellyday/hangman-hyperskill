# Write your code here
import random


def mask(word):
    word_in_list = list(word)
    for i, _ in enumerate(word):
        word_in_list[i] = "-"
    word = "".join(word_in_list)
    return word


def unmask(word, keyword, letter):
    word_in_list = list(word)
    if letter in keyword:
        for i, ch in enumerate(keyword):
            if keyword[i] == letter:
                word_in_list[i] = letter
    word = "".join(word_in_list)
    return word


def victory(word, keyword):
    if word == keyword:
        return True

    return False


def play():
    keyword_list = ["python", "java", "kotlin", "javascript"]
    valid_letter = "abcdefghijklmnopqrstuvwxyz"
    previous_guess = []
    keyword = random.choice(keyword_list)
    masked_word = mask(keyword)
    lives = 8

    while lives > 0:
        print()
        print(masked_word)
        print("Input a letter: ", end="")
        guess = input()

        if len(guess) == 0 or len(guess) > 1:
            print("You should input a single letter")
            continue

        if guess not in valid_letter:
            print("Please enter a lowercase English letter")
            continue

        if guess in previous_guess:
            print("You've already guessed this letter")
            continue

        previous_guess.append(guess)

        if guess not in keyword:
            print("That letter doesn't appear in the word")
            lives -= 1
            continue

        masked_word = unmask(masked_word, keyword, guess)

        if victory(masked_word, keyword):
            print(masked_word)
            print("You guessed the word!")
            print("You survived!")
            print()
            break

    if lives == 0:
        print("You lost!")
        print()


print("H A N G M A N")
while True:
    print('Type "play" to play the game, "exit" to quit: ', end='')
    state = input()

    if state == "play":
        play()

    if state == "exit":
        break
