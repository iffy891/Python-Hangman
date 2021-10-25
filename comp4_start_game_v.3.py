'''
    Author: Riley Anderson
    Date: 21/10/2021
    Description: start of game
    version: 3.0
    Changes: Added validation

'''
rules = ('''

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
while(True):
    player_name = input("Please enter a name (Max length=10, No special characters allowed e.g. #@$!%^&*(), No spaces):")
    if(((player_name.isalnum() == True) or (player_name.isalpha() == True) or (player_name.isnumeric() == True)) and (len(player_name) <= 10)):
        print(rules)
        while(True):
            number_of_games = input("How many games would you like to play (1-5)?:")
            if(number_of_games.isnumeric() == True) and ((int(number_of_games) <= 5) and (int(number_of_games) >=1)):
                print(player_name, number_of_games)
                break
            else:
                print("invalid Input")
    



