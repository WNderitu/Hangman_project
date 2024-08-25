import random
import re

print('Welcome to the Hangman Game')
print('The game involves guessing a hidden word')
print('The Player attempts at guessing a word represented in a row of dashes')
print('If a player guesses a letter which exists in the word, the program writes it in all correct positions')
print('The rules of the games are as follows:')
print('1. You have a maximum of 6 attempts')
print('2. The number of attempts are reduced for every wrong character guess the player makes')
print('3. Once all attempts are exhausted, without a matching word having been guessed, the player is hang (loses)')

# list of the hangman words for randomization
hgmn_rdm_wrds = ['azure', 'banjo', 'lucky', 'topaz', 'vixen', 'waltz']

# choosing a random word from the list of hangman words
guess_wrd = random.choice(hgmn_rdm_wrds)

# conversting a string to a list
guess_wrd_list = list(guess_wrd)

# replace values from index 0 to 4
guess_wrd_list[0:5] = ['_', '_', '_', '_', '_']
print(guess_wrd_list)
# # request for player to enter one letter

def reveal_word(guess_wrd_list, guess_wrd, letter_guess):
    guess_wrd_list = list(guess_wrd)
    for i in range(len(guess_wrd)):
        if guess_wrd[i] == letter_guess:
            guess_wrd_list[i] = letter_guess
    return ''.join(guess_wrd_list)

valid = False
while not valid:
    letter_guess = input('Guess one letter in the hiddden word? \n')
    if (len(letter_guess) == 1):
        valid = True
    else:
        print('The number of letters is more than 1, type 1 letter only')
        
# num_of_guesses = 0
# while num_of_guesses < 6:
#     failed_attempt = 0
#     while failed_attempt <6:
#         if letter_guess == guess_wrd[0]:
#             guess_wrd_list[0] = letter_guess
#             print(guess_wrd_list)
#             num_of_guesses +=1
#         elif letter_guess == guess_wrd[1]:
#             guess_wrd_list[1] = letter_guess
#             print(guess_wrd_list)
#             num_of_guesses +=1
#         elif letter_guess == guess_wrd[2]:
#             guess_wrd_list[2] = letter_guess
#             print(guess_wrd_list)
#             num_of_guesses +=1
#         elif letter_guess == guess_wrd[3]:
#             guess_wrd_list[3] = letter_guess
#             print(guess_wrd_list)
#             num_of_guesses +=1
#         elif letter_guess == guess_wrd[4]:
#             guess_wrd_list[4] = letter_guess
#             print(guess_wrd_list)
#             num_of_guesses +=1
#         else:
#             print('You failed, Try Again')
#             failed_attempt +=1
        
#     if failed_attempt == 6:
#         print(guess_wrd, 'You Lost!')
#         break
#     if num_of_guesses == 6:
#         print('You Won!')
    
failed_attempt = 0

for letter in guess_wrd:
    if letter != letter_guess:
        print('You failed, Try Again')
        failed_attempt +=1
    else:
        if letter_guess == guess_wrd[0]:
            guess_wrd_list[0] = letter_guess
            print(guess_wrd_list)
        elif letter_guess == guess_wrd[1]:
            guess_wrd_list[1] = letter_guess
            print(guess_wrd_list)
        elif letter_guess == guess_wrd[2]:
            guess_wrd_list[2] = letter_guess
            print(guess_wrd_list)
        elif letter_guess == guess_wrd[3]:
            guess_wrd_list[3] = letter_guess
            print(guess_wrd_list)
        elif letter_guess == guess_wrd[4]:
            guess_wrd_list[4] = letter_guess
            print(guess_wrd_list)

if reveal_word(guess_wrd_list,guess_wrd,letter_guess) == guess_wrd:
    print('You Win')
else:
    failed_attempt == 6
    print('You Lost')

