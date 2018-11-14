'''
Created on Nov 5, 2018

@author: Eirik
'''

from hangmand import hangmand
from getwords import getwords
import getpass
import random

gametypes = ["1: Guess a word that the computer picks", "2: Pick a word for the computer to guess"
             , "3: Pick a word for your friend to guess"]
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

def runit(word, player_type):
    getw = getwords("")
    words = getw.fetch_words(len(word))    
    hangman = hangmand("")
    if player_type == 1 or player_type == 3:
        return hangman.start_game_player(word, words, player_type)
    if player_type == 2:
        return hangman.start_game_ai(word, words, player_type)
    
    
# Pick a random word from a random length of words            
def computer_pick_random():
    wordlist = random.randrange(3,18)
    getw = getwords("")
    words = getw.fetch_words(wordlist)
    word = words[random.randrange(0, len(words))]
    return word

def computer_pick_length():
    print()

# Have user select a word to be guessed, check if word is valid, ask again if invalid
# Note that this input will be echoed in eclipse, but not if run from terminal
def player_pick(*err):
    if err:
        print(*err)
    word = getpass.getpass("Type word to guess: ").lower()
    if len(word) < 3 or len(word) > 18:
        return player_pick("The word has to be between 3 and 18 letters long")
    for x in range(len(word)):
        if not ALPHABET.__contains__(word[x]):
            return player_pick("The word can only contain letters a-z, try again")
    return word
    
    
def get_word(game_type):
    if game_type == 1:
        return computer_pick_random()
    elif game_type == 2:
        return player_pick()
    elif game_type == 3:
        return player_pick()
    
# Keep asking what game type to be played, until a valid response is given
def get_game_type(*err):
    if err:
        print(*err)
    print(*gametypes, sep = "\n")
    player_type = input("Select game type: ")
    if player_type == "1" or player_type == "2" or player_type == "3":
        return int(player_type)
    else:
        return get_game_type("You have to select a number between 1 and 3, try again.")

# Keep asking player if another game should be started until a valid response is given
def play_again(*err):
    if err:
        print(*err)
    accept = ["y", "yes", "ye", "yeah", "aye"]
    decline = ["no", "n", "nah", "nope"]
    response = input("Do you want to play again? y/n ").lower()
    if accept.__contains__(response):
        return True
    elif decline.__contains__(response):
        return False
    else:
        return play_again()

# Select a word to play, print out result and ask player if another game should be started
def game_loop(game_type):
    word = get_word(game_type)
    errors = runit(word, game_type)
    if errors == 0:
        print("Well done! The word {} was solved without any errors!".format(word))
    elif errors == 1:
        print("Well done. The word {} was solved with {} error!".format(word, errors))
    elif (errors > 5):
        print("The word {} was not solved".format(word))
    else:
        print("Well done. The word {} was solved with {} errors!".format(word, errors))
    return play_again()

# Have player select what gametype to be played (computer or human player)
# Continue loop until player selects to quit.
if __name__ == '__main__':
    playing = True
    game_type = get_game_type()
    
    while playing:
        playing = game_loop(game_type)
    
    pass

