'''
Created on Nov 5, 2018

@author: Eirik
'''

''' Helper tool to split dictionary file into files based on length of words.
    Not used during runtime 
'''

if __name__ == '__main__':
    #from multiprocessing import Pool
    
    with open('words', 'r') as f:
        WORDS = f.read().split('\n')
 
    ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
    
    new3 = set()
    new4 = set()
    new5 = set()
    new6 = set()
    new7 = set()
    new8 = set()
    new9 = set()
    new10 = set()
    new11 = set()
    new12 = set()
    new13 = set()
    new14 = set()
    new15 = set()
    new16 = set()
    new17 = set()
    new18 = set()
    newwords = set()
    for word in WORDS:
        if all([letter in ALPHABET for letter in word]):
            if len(word) == 3:
                new3.append(word)
            if len(word) == 4:
                new4.append(word)
            if len(word) == 5:
                new5.append(word)    
            if len(word) == 6:
                new6.append(word)
            if len(word) == 7:
                new7.append(word)
            if len(word) == 8:
                new8.append(word)
            if len(word) == 9:
                new9.append(word)
            if len(word) == 10:
                new10.append(word)
            if len(word) == 11:
                new11.append(word)
            if len(word) == 12:
                new12.append(word)
            if len(word) == 13:
                new13.append(word)
            if len(word) == 14:
                new14.append(word)
            if len(word) == 15:
                new15.append(word)
            if len(word) == 16:
                new16.append(word)
            if len(word) == 17:
                new17.append(word)
            if len(word) == 18:
                new18.append(word)
            
            
            #newwords.append(word)
    #WORDS = set(newwords)
    
    f= open("wordsfiltered3.txt","w+")
    for i in range(len(new3)):
        f.write(new3[i] + "\n")
    f= open("wordsfiltered4.txt","w+")
    for i in range(len(new4)):
        f.write(new4[i] + "\n")
    f= open("wordsfiltered5.txt","w+")
    for i in range(len(new5)):
        f.write(new5[i] + "\n")
    f= open("wordsfiltered6.txt","w+")
    for i in range(len(new6)):
        f.write(new6[i] + "\n")
    f= open("wordsfiltered7.txt","w+")
    for i in range(len(new7)):
        f.write(new7[i] + "\n")
    f= open("wordsfiltered8.txt","w+")
    for i in range(len(new8)):
        f.write(new8[i] + "\n")
    f= open("wordsfiltered9.txt","w+")
    for i in range(len(new9)):
        f.write(new9[i] + "\n")
    f= open("wordsfiltered10.txt","w+")
    for i in range(len(new10)):
        f.write(new10[i] + "\n")
    f= open("wordsfiltered11.txt","w+")
    for i in range(len(new11)):
        f.write(new11[i] + "\n")
    f= open("wordsfiltered12.txt","w+")
    for i in range(len(new12)):
        f.write(new12[i] + "\n")
    f= open("wordsfiltered13.txt","w+")
    for i in range(len(new13)):
        f.write(new13[i] + "\n")
    f= open("wordsfiltered14.txt","w+")
    for i in range(len(new14)):
        f.write(new14[i] + "\n")
    f= open("wordsfiltered15.txt","w+")
    for i in range(len(new15)):
        f.write(new15[i] + "\n")
    f= open("wordsfiltered16.txt","w+")
    for i in range(len(new16)):
        f.write(new16[i] + "\n")
    f= open("wordsfiltered17.txt","w+")
    for i in range(len(new17)):
        f.write(new17[i] + "\n")
    f= open("wordsfiltered18.txt","w+")
    for i in range(len(new18)):
        f.write(new18[i] + "\n")
    
    f.close()
    print(len(WORDS))


