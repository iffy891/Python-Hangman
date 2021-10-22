'''
    Author: Riley Anderson
    Date: 22/10/2021
    Description: Statboard
    Version: 2.0
    Changes: used .format() to input the data rather than have it written directly in the statment. Aswell as saving the values of the games in a dictionary
'''
name = 'bob'
num_of_games_choosen = '5'
num_of_games_played = '5'
num_of_games_won = '3'
words = {'game 1':'Mickey Mouse', 'game 2':'Daffy Duck', 'game 3':'Road Runner','game 4':'Scooby-Doo','game 5':'Spider-Man'}
errors = {'game 1':'2', 'game 2':'6', 'game 3':'1','game 4':'10','game 5':'10'}

while(True):
    print('''
=============================================================================================================================================================
                                                        ||                 YOUR PLAY                 ||
=============================================================================================================================================================


        Player Name: {}

        Number of Games Choosen to play: {}

        Number of Games Played: {}

        Number of Game Won: {}

        Category:

        Games Words:
            Game 1. {}
            Game 2. {}
            Game 3. {}
            Game 4. {}
            Game 5. {}

        How many errors in each game:
            Game 1. {}
            Game 2. {}
            Game 3. {}
            Game 4. {}
            Game 5. {}

=============================================================================================================================================================

=============================================================================================================================================================
    '''.format(name, num_of_games_choosen, num_of_games_played, num_of_games_won,
               words['game 1'], words['game 2'], words['game 3'], words['game 4'],words['5'],
               errors['game 1'], errors['game 2'], errors['game 3'], errors['game 4'],errors['5']))

    input("Next game:")
