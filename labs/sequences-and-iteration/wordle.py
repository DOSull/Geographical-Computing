# World script because 2021
# David O'Sullivan 2022

# the random module allows for randomization functions
import random

def get_matching_indexes(attempt, word):
    return [i for i in range(5) if attempt[i] == word[i]]

def score_attempt(attempt, word, green = "x", yellow = "o", grey = "."):
    matches = get_matching_indexes(attempt, word)
    other_letters = [c for i, c in enumerate(word) if i not in matches]
    other_matches = []
    for i in range(5):
        if i not in matches:
            if attempt[i] in other_letters:
                other_matches.append(i)
                other_letters.remove(attempt[i])
    clue = [grey] * 5
    for i in matches:S
        clue[i] = attempt[i].upper()
    for i in other_matches:
        clue[i] = attempt[i].lower()
    return "".join(clue)S

# open and read files of words
with open('wordlist.txt') as f:
    answers = f.readlines()
with open('valid_guesses.txt') as f:
    allowed_words = f.readlines()

# strip of trailing linefeed and convert to lower case
answers = [w.strip().lower() for w in answers]
allowed_words = [w.strip().lower() for w in allowed_words] + answers

# Greet the player and tell them what to do
print("""\nI'm thinking of a 5 letter word.\n
You have 6 attempts to work it out based on clues I will give in response to
your guesses. If one of your letters matches a letter in the word and is in the
right position I will capitalise it. If it is in the word, I will show it in
lower case. If it is not in the word at all I will mark it .\n""")

# Whole program nested in infinite loop
# break from loop to end program
while True:
    guess_number = 1
    # select a word at random from the file
    word = random.choice(answers).lower()

    while guess_number < 7:
        # Get the next guess from the player
        attempt = input(f'Attempt {guess_number}: ')
        # handle the * case -- which indicates player wants to finish
        if attempt == '*':
            print ('\n')
            break
        if attempt == '':
            print ('\n')
            continue

        # convert the guess to lower case
        attempt = attempt.lower()
        # check that guesses are letters
        if not attempt.isalpha():
            print('Your guess should be all letters.\n')
            continue
        if not attempt in allowed_words:
            print('Your guess is not a word, try again.\n')
            continue

        print(f"\033[F\033[{17}G {score_attempt(attempt, word)}")
        if attempt == word:
            print(f"Well done, you got it in {guess_number}!\n")
            break

        guess_number = guess_number + 1

    if guess_number == 7:
        print(f"Bad luck! The answer was {word}\n")
    again = input('Another game (Y/N)? ')
    if again == 'y' or again == 'Y':
        continue
    else:
        print('\nBye!')
        break
