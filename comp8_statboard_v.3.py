'''
    Author: Riley Anderson
    Date: 23/10/2021
    Description: Statboard
    Version: 3.0
    Changes: More universal variables, e.g. input for name
    Notes: the dictionaries will get their values inputted at the time of the game and after,
            not directly in the code to give more changable options.
'''
words = {'game 1':'Mickey Mouse', 'game 2':'Daffy Duck', 'game 3':'Road Runner','game 4':'Scooby-Doo','game 5':'Spider-Man'}
errors = {'game 1':'2', 'game 2':'6', 'game 3':'1','game 4':'10','game 5':'10'}
while(True):
    name = input("Please enter a name (Max length=10, No special characters allowed e.g. #@$!%^&*(), No spaces): ")
    if(((name.isalnum() == True) or (name.isalpha() == True) or (name.isnumeric() == True)) and (len(name) <= 10)):
        while(True):
            num_of_games_choosen = input("How many games would you like to play: ")
            if ((num_of_games_choosen.isnumeric() == True) and ((int(num_of_games_choosen) <= 5) and (int(num_of_games_choosen) >=  1))): 
                while(True):
                    num_of_games_played = input("How many games have you played: ")
                    if((num_of_games_played.isnumeric() == True) and ((int(num_of_games_played) <= int(num_of_games_choosen)))):
                        while(True):
                            num_of_games_won = input("How many games did you win: ")
                            if((num_of_games_won.isnumeric() == True) and ((int(num_of_games_won) <= int(num_of_games_played)))):
                                print(name, num_of_games_choosen)
                                statboard = '''
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
                            words['game 1'], words['game 2'], words['game 3'], words['game 4'],words['game 5'],
                            errors['game 1'], errors['game 2'], errors['game 3'], errors['game 4'],errors['game 5'])
                            print(statboard)
                            input("Next game:")
                            break
                        else:
                            print("invalid input")
                        break
                    else:
                        print("invalid input")
                    break
            else:
                print("invalid input")
            break
    else:
        print("invalid input")

            
                
    

    


    

                
