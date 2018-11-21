Welcome to Hangman.
It's a classic Hangman game, where you have the options of picking a word and have a friend guess it, pick a word and have the computer guess it, or have the computer pick a word for you to guess. Run the game with python hangman.py. A normal run uses the files hangman.py, hangmand.py, getwords.py and asciiart.py plus the .txt files based on the length of the word to guess.

The dictionary used is user/share/dict/word which is freely available online and is based on the SCOWL (Spell Checker Oriented Word Lists) project for Debian.

All words with length 1 or 2 as well as words containing special characters (apostrophe and hyphen) were removed from the dictionary. After all unwanted words were removed the dictionary contains 62784 unique words. These words were then split into seperate files based on their length so that the computer can load only words or correct length. Number of words for each length is as follows:

![words by length](graphs_and_data/NumberOfWords.png?raw=true "Words By Length")

|Length| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|words| 585 | 2339|4567|7215|9816|10374|9217|7329|5012|3176|1778|788|369|136|61|22|

The average number of guesses for each length (AI was set up to continue guessing until all 26 letters were used unless it solved the word earlier):

|Length| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|avg.guess| 6.42 | 5.67|4.36|3.35|2.58|1.76|1.19|0.82|0.56|0.42|0.28|0.18|0.12|0.06|0.05|0.09|

Running PlayAllWords.py makes the computer try to guess every word in the dictionary and provides a frequency map of how many guesses are needed. (caution: 0.013 seconds average per word means about 13 minutes runtime on a i5 3.1ghz 4core cpu) 

About the AI:
At the start of a word it loads all words of that length into memory. After guessing a letter it eliminates words based on where that letter is in the word. The AI then makes a frequency map of the remaining letters/words to see which letter to guess next. If two or more letters are tied for highest frequency it will guess alphabetically (can easily be changed to random, but for analytics purposes alphabetically was chosen) 

The Hangman AI guesses the word "Hangman" with 3 errors (e,i,d). The order of the guesses will be e,i,a,n,m,d,g,h. The first guess will depend on how long the word is. Among three letter words the most common letter is a, four letter words have e as the most common letter. 
 3:a, 4:e, 5:s, 6:e, 7:e, 8:e, 9:e, 10:e, 11:e, 12:i, 13:i, 14:i, 15:i, 16:i, 17:i, 18:i. The prevalence of -ing and -tion ending is the reason words with 12 or more letters have i as the most common character. The AI will try to delay mistakes as long as possible. If for example it the word is s_o_er and the options are narrowed down to "slower" and "shower" it will guess the "w" before checking if the second letter is "l" or "h"

| errors | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | 8    | 19   | 36   | 46   | 56   | 66 | 73 | 64 | 60 | 51 | 51 | 31 | 18 | 5 | 1 | 0 | 0 |
| 4 | 30   | 88   | 153  | 239  | 286  | 337 | 347 | 289 | 232 | 150 | 100 | 57 | 20 | 7 | 4 | 0 | 0 |
| 5 | 94   | 292  | 546  | 762  | 829  | 755 | 560 | 358 | 178 | 104 | 54 | 22 | 12 | 1 | 0 | 0 | 0 |
| 6 | 332  | 884  | 1355 | 1544 | 1306 | 897 | 459 | 227 | 106 | 54 | 29 | 14 | 7 | 1 | 0 | 0 | 0 |
| 7 | 849  | 1929 | 2418 | 2093 | 1310 | 658 | 328 | 138 | 51 | 25 | 13 | 4 | 0 | 0 | 0 | 0 | 0 |
| 8 | 1743 | 3048 | 2880 | 1726 | 699  | 200 | 59  | 16 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 9 | 2553 | 3506 | 2195 | 801  | 148  | 14  | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10| 3008 | 2906 | 1167 | 225  | 23   | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11| 2693 | 1855 | 429  | 35   | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12| 1985 | 1047 | 137  | 7    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 13| 1318 | 427  | 33   | 0    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 14| 657  | 123  | 8    | 0    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 15| 327  | 39   | 3    | 0    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 16| 128  | 8    | 0    | 0    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 17| 58   | 3    | 0    | 0    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 18| 20   | 2    | 0    | 0    | 0    | 0   | 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The computer was able to guess 15,803 of the 62,784 (25.17%) words without any mistakes.
The computer was unable to guess 2,276 of the 62,784 (3.62%) words before getting the 6 errors.
The computer was able to guess any word of 9 characters or more.

