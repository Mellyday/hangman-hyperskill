# Write your code here
import random

print("H A N G M A N")
keyword_list = ["python", "java", "kotlin", "javascript"]
keyword = random.choice(keyword_list)
hint = list(keyword)
for i, ch in enumerate(hint):
    if i >= 3:
        hint[i] = "-"
hint = ''.join(hint)

print("Guess the word ", hint, ": ", sep="")
guess = input()

if guess == keyword:
    print("You survived!")
if guess != keyword:
    print("You lost!")
