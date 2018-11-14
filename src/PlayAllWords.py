'''
Created on Nov 5, 2018

@author: Eirik
'''

''' Program that runs all words, and generates a frequency list of how many attempts
    the computer needs to solve the words
    Do not run unless you really want to,
    on an i5 3.1ghz processor with 4 cores it takes about 13 minutes
'''
from getwords import getwords
import time

from multiprocessing import Pool
import multiprocessing
from playAllSolver import playAllSolver
    
    
def runit(length):
    getw = getwords("")
    print("loading words with length " + (str(length)))
    words = getw.fetch_words(length)
    print("Number of words to play: " + str(len(words)))
    errors = [0] * 29
    hangman = playAllSolver("")
    for word in words:
            errors[hangman.start_game_ai(word, words, 26, False)] += 1
    print(errors)
            
if __name__ == '__main__':
    processors = multiprocessing.cpu_count()
    print("Playing all words in the dictionary. Using {} cores. This may take several minutes".format(processors))
    pool = Pool(processes=processors)
    start = time.time()
    with Pool(processors) as p:
        print(p.map(runit, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
    print("Time taken = {0:.5f}".format(time.time() - start))
    
    pass

