'''
    Author: Riley Anderson
    Date: 21/10/2021
    Description: start of game
    version: 1.0

'''

player_name = input("Please enter a name:")

print('''

Rules:
Basic rules of Hangman; A word will be selected by the computer at random the length
of the selected word will be shown at the bottom of the screen, '_' will be showing
the unknown letters. You will be able to guess a letter and if it is correct it will
display in its correct location, if it is incorrect you will recieve a strike and the
hanging shall begin, you will have a total of 10 strikes before you lose. All of your
guess will show up on the left hand side of the screen, so you can see what you have
guessed. Warning: You can not guess the whole word in one go.
There will be a selection of categories once you move on, the words that will be
randomly selected will be related in some way. You will get a choice to play 1 or more
games, if you select to play more than 1 game you will not have the chance to change
the category. If you select to play 1 game you will have the opportunity to play
another with a different category. After you have finished playing you will be shown
a statboard of your play.
Have fun!!!!
''')

number_of_games = input("How many goames would you like to play (1-5)?:")

print(player_name, number_of_games)
