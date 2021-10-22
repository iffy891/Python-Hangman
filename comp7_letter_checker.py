'''
    Author: Riley Anderson
    Date: 22/10/2021
    Description: test of letter checker
    version: 1.0
    
'''
word = 'winner'
line = ['_', '_', '_', '_', '_', '_']
   
index = 0
while(True):
    print(line, sep=' ')
    guess = input("What is your guess?:")
    index = 0
    while index < len(word):
        index = word.find(guess, index)
        if index == -1:
            break
        line[index] = guess
        index += 1
    
        
