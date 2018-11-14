'''
Created on Nov 6, 2018
Just a helper class that analyzes frequency of letters.
Not used in the program itself
@author: Eirik
'''



if __name__ == '__main__':
    ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
    frequency = [0] * 26
    
    with open('wordsfiltered9.txt', 'r') as f:
        WORDS = f.read().split('\n')
    
    for word in WORDS:
        for x in range(len(ALPHABET)):
            if word.__contains__(ALPHABET[x]):
                frequency[x] += 1
        
    print(len(WORDS))
    print(frequency)
    
    highestf = 0
    highestl = "a"
    for x in range(len(ALPHABET)):
        if frequency[x] > highestf:
            highestf = frequency[x]
            highestl = ALPHABET[x]
    print(highestl)
    print(highestf)
    f.close()
    pass

# a, e, s, e, e, e, e, e, e, i, i, i, i, i, i, i, l, a, a, a