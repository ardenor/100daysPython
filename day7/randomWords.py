import random

word_list = ["ardvark", "baboon", "camel"]
tries = 3
#random_word = word_list[random.randint(0, len(word_list) - 1)]
random_word = random.choice(word_list)

display = []
for l in random_word:
    display.append("_")
print(display)

while tries > 0:
    guess = input("Guess a letter: ").lower()

    for pos in range(len(random_word)):
        letter = random_word[pos]
        if letter == guess:
            display[pos] = letter

    print(display)
    tries -= 1