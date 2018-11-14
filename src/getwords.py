'''
Created on Nov 5, 2018

@author: Eirik
'''

class getwords(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        # List of files that can be loaded
        self.files = ["wordsfiltered3.txt", "wordsfiltered4.txt", "wordsfiltered5.txt", "wordsfiltered6.txt", 
             "wordsfiltered7.txt", "wordsfiltered8.txt", "wordsfiltered9.txt", "wordsfiltered10.txt", 
             "wordsfiltered11.txt", "wordsfiltered12.txt", "wordsfiltered13.txt", "wordsfiltered14.txt", 
             "wordsfiltered15.txt", "wordsfiltered16.txt", "wordsfiltered17.txt", "wordsfiltered18.txt"]

    
    # opens the file containing the words with correct length. Since words of 1 and 2 letters
    # have been eliminated fetch_words(3) will open files[0] ("wordsfiltered3.txt")
    def fetch_words(self, length):
        with open(self.files[length-3], "r") as f:
            words = f.read().split('\n')
            f.close()
            return words
            