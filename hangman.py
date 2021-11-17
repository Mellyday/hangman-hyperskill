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


print("H A N G M A N")
keyword_list = ["python", "java", "kotlin", "javascript"]
keyword = random.choice(keyword_list)
masked_word = mask(keyword)
lives = 8

while lives > 0:
    print()
    print(masked_word)
    print("Input a letter: ", end="")
    guess = input()

    if guess not in keyword:
        print("That letter doesn't appear in the word")
        lives -= 1
        continue

    if guess in masked_word:
        print("No improvements")
        lives -= 1
        continue

    masked_word = unmask(masked_word, keyword, guess)

    if victory(masked_word, keyword):
        print(masked_word)
        print("You guessed the word!")
        print("You survived!")
        break

if lives == 0:
    print("You lost!")
