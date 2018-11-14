'''
Created on Nov 9, 2018

@author: Eirik
'''
from asciiart import asciiart
class hangmand(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.reset()
        self.current_length = 0
        self.LETTERS = list('abcdefghijklmnopqrstuvwxyz')
        
    # reset is called between every game, clear the dictionary
    # , and reset the alphabet (alphabet is being emptied during play
    def reset(self):
        self.words = []
        self.ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
        self.player = 0
       
    
    def start_game_player(self, word, words, player_type):
        self.reset()
        self.words = words
        errors = 0
        wrong_letters = []
        correct_letters = ["_"] * len(word)
        self.player = player_type
        print(*correct_letters)
        while errors < 6 and correct_letters.__contains__("_"):
            letter = self.select_letter()
            if self.error(word, wrong_letters, correct_letters, letter):
                errors += 1
            self.mark_word(word, correct_letters, letter)
            if self.ALPHABET.__contains__(letter):
                self.ALPHABET.remove(letter)
            self.output(correct_letters, wrong_letters, errors)
        return (errors)
    
    # word = word to guess, words = all possible words of given length
    # player_type set to computer for the select_letter function
    # wrong_letters keep track of incorrect guesses, correct_word keeps track of correct ones
    # While loop runs until word is correctly guessed, or 6 incorrect guesses has been made    
    def start_game_ai(self, word, words, player_type):
        self.reset()
        self.words = words
        errors = 0
        wrong_letters = []
        correct_letters = ["_"] * len(word)
        self.player = player_type
                
        while errors < 6 and correct_letters.__contains__("_"):
            letter = self.select_letter_ai()    
            if self.error(word, wrong_letters, correct_letters, letter):
                errors += 1
                
            self.mark_word(word, correct_letters, letter)
            temp_words = []
            occurances = [j for j, ltr in enumerate(word) if ltr == letter]
            for word_to_test in self.words:
                if self.match_word(word, word_to_test,occurances,  letter):
                    temp_words.append(word_to_test)
            self.words = temp_words
            if self.ALPHABET.__contains__(letter):
                self.ALPHABET.remove(letter)
                self.output(correct_letters, wrong_letters, errors)
        return (errors)
        #self.result(word, errors, err)
                
    # Print status of game
    def output(self, correct_letters, wrong_letters, errors):
        print("Word to guess: ", end = "")
        print(*correct_letters)
        print("Wrong letters: ", end = "")
        print(*wrong_letters)
        if errors < 6:
            print(asciiart.HANGMANART[errors])
        else: 
            print(asciiart.HANGMANART[6])
    
    # If letter is not in the word to be guessed, or if it has been guessed already, error is incremented
    def error(self, word, wrong_letters, correct_letters, letter):
        if not word.__contains__(letter) or wrong_letters.__contains__(letter) or correct_letters.__contains__(letter):
            wrong_letters.append(letter)
            return True
        return False
    
    # See if a given word matches with the word to guess given the letters
    def match_word(self, word1, word2, occurances, letter):
        if not word2.__contains__(letter) and word1.__contains__(letter):
            return False
        if [i for i, ltr in enumerate(word2) if ltr == letter] != occurances:
            return False
        #for x in range(len(word1)):
        #    if (word2[x] == letter and word1[x] != letter) or (word1[x] == letter and word2[x] != letter):
        #        return False 
        return True
    
    # Insert the letter that was just guessed into guessed_word list. (replacing "_")    
    def mark_word(self, word_to_guess, guessed_word, letter):
        for x in range(len(word_to_guess)):
            if word_to_guess[x] == letter:
                guessed_word[x] = letter
           
    # player = 0 => player is computer
    def select_letter(self):
        if self.player == 0:
            return self.select_letter_ai()
        else:
            return self.select_letter_player()
                
    # select a letter from input, and check if it's a letter between a - z, recursion if needed
    def select_letter_player(self, *err):
        if err:
            print(*err)        
        letter = input("Select a letter to guess: ").lower()
        if len(letter) == 1 and self.LETTERS.__contains__(letter):
                return letter
        else:
            return self.select_letter_player("Must be a letter between a -z")
    
    # Check how many of the remaining words contain the remaining letters.
    # Build frequency table, then return the most frequently used letter
    # if several letters have same frequency, return based on alphabetical order.       
    def select_letter_ai(self):
        frequency = [0] * len(self.ALPHABET)    
        for x in range(len(self.ALPHABET)):
            for word in self.words:
                if word.__contains__(self.ALPHABET[x]):
                    frequency[x] += 1
                    
        highestl = str(self.ALPHABET[0])
        highestv = 0
        for x in range(len(frequency)):
            if frequency[x] > highestv:
                highestv = frequency[x]
                highestl = self.ALPHABET[x]
        return highestl