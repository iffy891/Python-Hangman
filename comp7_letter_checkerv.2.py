'''
    Author: Riley Anderson
    Date: 22/10/2021
    Description: Word checker, This will check for the letter in the word, basic made
    Version: 2.0
    changes: Added validation for if it has been guessed before and
             if it is only letters
'''
word = 'win-ner'
line = ['_', '_', '_', '_', '_', '_', '_']
play = True  
index = 0

guesses = []
while(play == True):
    print(*line, sep=' ')
    if '_' not in line:
        play = False
        print('You Win')
        break
    guess = input("What is your guess?:")
    
    if (guess.isalpha() == True) and (guess not in guesses) and (len(guess) == 1):
        index = 0
        while index < len(word):
            index = word.find(guess.lower(), index)
            if index == -1:
                break
            line[index] = guess.upper()
            index += 1
            print(guess)
    
    else:
        print('invalid input')
    guesses.append(guess)
