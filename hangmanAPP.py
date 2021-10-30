'''
    Author: Riley Anderson
    Date: 25/10/21
    Description: App of hangman
    Version: 1.0
'''

#-------------- Libraries --------------
import tkinter as tk
import turtle as t
import random as r
#-------------- Variables ---------------


display_list = []
word_len = []
categories = {'country names': ['new zealand', 'australia', 'belize', 'djibouti', 'india',
                 'north korea', 'qatar', 'south africa', 'vietnam', 'zambia',
                 'yemen'],
              'cartoon characters': ['bugs bunny', 'donald duck', 'popeye', 'scooby-doo',
                      'mickey mouse', 'spider-man', 'pink panther', 'taz',
                      'yosemite sam', 'patrick star', 'shrek', 'puss in boots',
                      'master splinter', 'spongebob squarepants', 'pikachu',
                      'charmander'],
              'tv shows' : ['squid game', 'friends', 'shortland street', 'horders', 'one news', 'three news',
            'treasure island', 'survivor', 'greys anatomy', 'game of thrones', 'lucifer',
            'the office', 'stranger things', 'wellington paranormal'],
              'heros vs villians': ['wonder woman', 'batman', 'iron man', 'hulk', 'captain america',
                    'flash', 'black widow', 'catwoman', 'Maleficent', 'yoda', 'optimus prime',
                     'megatron', 'venom', 'thor', 'captain marvel', 'thanos', 'harley quinn', 'batwoman',
                     'powerwoman'],
              'eye spy': ['tree', 'window', 'chair', 'door', 'light', 'sky', 'table'],
              'vehicle models': ['mustang', 'civic', 'corvette', 'corolla', 'cherokee', 'beetle', 'highlander', 'cr-v',
                  'ranger', 'land cruiser', 'forester', 'focus', 'hr-v', 'golf', 'outlander', 'santa fe'],
              'food chains': ['mcdonalds', 'kfc', 'wendy\'s', 'starbucks', 'burgerfuel', 'subway', 'pizza hut', 'domino\'s'],
              'planes':['wings', 'landing gear', 'engines', 'air new zealand', 'airport', 'terminal', 'flight'],
              'random': ['new zealand', 'australia', 'belize', 'djibouti', 'india',
                 'north korea', 'qatar', 'south africa', 'vietnam', 'zambia',
                 'yemen', 'bugs bunny', 'donald duck', 'popeye', 'scooby-doo',
                      'mickey mouse', 'spider-man', 'pink panther', 'taz',
                      'yosemite sam', 'patrick star', 'shrek', 'puss in boots',
                      'master splinter', 'spongebob squarepants', 'pikachu',
                      'charmander', 'squid game', 'friends', 'shortland street', 'horders', 'one news', 'three news',
            'treasure island', 'survivor', 'greys anatomy', 'game of thrones', 'lucifer',
            'the office', 'stranger things', 'wellington paranormal', 'wonder woman', 'batman', 'iron man', 'hulk', 'captain america',
                    'flash', 'black widow', 'catwoman', 'Maleficent', 'yoda', 'optimus prime',
                     'megatron', 'venom', 'thor', 'captain marvel', 'thanos', 'harley quinn', 'batwoman',
                     'powerwoman', 'tree', 'window', 'chair', 'door', 'light', 'sky', 'table', 'mustang', 'civic', 'corvette', 'corolla', 'cherokee', 'beetle', 'highlander', 'cr-v',
                  'ranger', 'land cruiser', 'forester', 'focus', 'hr-v', 'golf', 'outlander', 'santa fe', 'mcdonalds', 'kfc', 'wendy\'s', 'starbucks', 'burgerfuel', 'subway',
                         'pizza hut', 'domino\'s', 'wings', 'landing gear', 'engines', 'air new zealand', 'airport', 'terminal', 'flight']}  
selected_category = None
already_picked = {}
guesses = []
index = 0
word = 'winner'
words = {'game 1':'Mickey Mouse', 'game 2':'Daffy Duck', 'game 3':'Road Runner','game 4':'Scooby-Doo','game 5':'Spider-Man'}
errors = {'game 1':'2', 'game 2':'6', 'game 3':'1','game 4':'10','game 5':'10'}
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
                                '''

player_info = []
#-------------- Functions ---------------
def gamesetup():
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
    setup = True
    while(setup == True):
        player_name = input("Please enter a name (Max length = 10, No special characters allowed e.g. !@#$%^&*(), No spaces): ")
        if(((player_name.isalnum() == True) or (player_name.isalpha() == True) or (player_name.isnumeric() == True)) and (len(player_name) <= 10)):
            print(rules)
            while(setup == True):
                number_of_games_chosen = input("How many games would you like to play (1-5)?:")
                if(number_of_games_chosen.isnumeric() == True) and ((int(number_of_games_chosen) <= 5) and (int(number_of_games_chosen) >=1)):
                    #print(player_name, number_of_games)
                    setup = False
                    strikes = 10
                    break
                else:
                    print("invalid Input")
            return player_name, number_of_games_chosen, strikes
        else:
            print("invalid Input")
        
def window():
    def main_setup():
        draw.penup()
        draw.goto(0,-100)
        draw.left(90)
        draw_me()
    def draw_me():
        global entry
        #number = entry.get()
        draw.pendown()
        '''
        if int(number) == 1:
            draw.forward(300)
        elif int(number) == 2:
            draw.right(90)
            draw.forward(150)
        elif int(number) == 3:
            draw.right(90)
            draw.forward(50)
        elif int(number) == 4:
            draw.right(90)
            draw.circle(20)
        elif int(number) == 5:
            draw.left(90)
            draw.penup()
            draw.forward(40)
            draw.pendown()
            draw.forward(70)
        elif int(number) == 6:
            draw.left(45)
            draw.forward(50)
        elif int(number) == 7:
            draw.left(180)
            draw.penup()
            draw.forward(50)
            draw.left(90)
            draw.pendown()
            draw.forward(50)
        elif int(number) == 8:
            draw.penup()
            draw.right(180)
            draw.forward(50)
            draw.left(45)
            draw.forward(40)
            draw.pendown()
            draw.right(135)
            draw.forward(30)
        elif int(number) == 9:
            draw.penup()
            draw.right(180)
            draw.forward(30)
            draw.left(90)
            draw.pendown()
            draw.forward(30)
        elif int(number) == 10:
            draw.penup()
            draw.right(180)
            draw.forward(30)
            draw.left(45)
            draw.forward(60)
            draw.left(90)
            draw.forward(5)
            draw.pendown()
            draw.dot(5, 'black')           <----- Fix to read strikes
            draw.penup()
            draw.left(180)
            draw.forward(10)
            draw.pendown()
            draw.dot(5, 'black')
            draw.penup()
            draw.backward(10)
            draw.right(90)
            draw.forward(20)
            draw.right(90)
            draw.forward(5)
            draw.pendown()
            draw.left(225)
            for x in range(1,15):
                draw.forward(2)
                draw.right(7)
            draw.penup()
            draw.forward(100)
        entry.delete(0)
        '''
    def list_change():
        global label, display_list
        additive = entry1.get()
        print(display_list, additive)
        display_list.append(additive)
        print(display_list)
        print(*display_list, sep=', ')
        label['text'] = display_list
    window = tk.Tk()
    window.title('Hangman')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry('%dx%d' % (width, height))
    #---------- Top Frame -----------
    top_frame = tk.Frame(window)
    top_frame.pack(side=tk.TOP)
    #-------- Canvas frame ---------
    canvas = tk.Canvas(top_frame)
    canvas.config(width=700, height=500)
    canvas.pack(side=tk.RIGHT, anchor='ne', padx=10)
    screen = t.TurtleScreen(canvas)
    screen.bgcolor('white')
    #entry = tk.Entry(frame)
    #entry.pack()
    #button = tk.Button(frame, text='hit me', command=draw_me)
    #button.pack()
    draw = t.RawTurtle(screen)
    main_setup()
    #----------- Guesses list frame ------
    list_frame = tk.Frame(top_frame, bg='blue', width=700, height=500)
    list_frame.pack_propagate(0)
    list_frame.pack(side=tk.LEFT, padx=10, anchor='nw')
    #entry1 = tk.Entry(list_frame)
    #entry1.pack()
    #button = tk.Button(list_frame, text='hit me', command=list_change)
    #button.pack()
    label = tk.Label(list_frame)
    label.pack()
    #------------ Bottom Frame -----------
    bot_frame = tk.Frame(window, width=1300, height=600, bg='red')
    bot_frame.pack_propagate(0)
    bot_frame.pack(side=tk.BOTTOM, anchor='s')
    bot_label = tk.Label(bot_frame, text=word_len)
    bot_label.place(x=300, y=100)
    guess_entry = tk.Entry(bot_frame, width=10)
    guess_entry.pack(ipadx=10, anchor='n')

    window.mainloop()

def category_select():
    global categories, selected_category
    while(True):
        category_selection = input('''
CATEGORIES:
1. Country Names
2. Cartoon Characters
3. TV Shows
4. Heros VS Villians
5. Eye Spy
6. Vehicle Models
7. Food Chains
8. Planes
9. Random
Please select a category: ''')
        if category_selection == "1" or category_selection.lower() == 'country names':
            selected_category = 'country names'
        elif category_selection == "2" or category_selection.lower() == 'cartoon characters':
            selected_category = 'cartoon characters'
        elif category_selection == '3' or category_selection.lower() == 'tv shows':
            selected_category = 'tv shows'
        elif category_selection == '4' or category_selection.lower() == 'heros vs villians':
            selected_category = 'heros vs villians'
        elif category_selection == '5' or category_selection.lower() == 'eye spy':
            selected_category = 'eye spy'
        elif category_selection == '6' or category_selection.lower() == 'vehicle models':
            selected_category = 'vehicle models'
        elif category_selection == '7' or category_selection.lower() == 'food chains':
            selected_category = 'food chains'
        elif category_selection == '8' or category_selection.lower() == 'planes':
            selected_category = 'planes'
        elif category_selection == '9' or category_selection.lower() == 'random':
            selected_category = 'random'
        else:
            print("invalid input")

def word_randomiser():
    while(True):
        #selected_category = 'random'
        if selected_category != None:
            category_choice = categories[selected_category]
            word = r.choice(category_choice)
            #print(word)
            if word not in already_picked:
                already_picked.append(word)
                print(*already_picked, sep=', ')
            else:
                print('invalid input, choose again')
                print(already_picked)
            input('')
            '''
            if len(already_picked) == int(number_of_games):
                break

            '''

def checker():
    global display_list, word, index, word_len
    '''
    while(play == True):
        print(*line, sep=' ')
        if '_' not in line:
            play = False
            print('You Win')
            break
        guess = input("What is your guess?: ")

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
'''
    while(True):
        print(*word_len, sep=' ')
        if '_' not in word_len:
            print('You Win')
            break
        guess = input("What is your guess?: ")

        if(guess.isalpha() == True) and (guess.lower() not in display_list) and (len(guess) == 1):
            index = 0
            display_list.append(guess.lower())
            while index < len(word):
                index = word.find(guess.lower(), index)
                if index == -1:
                    print("Incorrect")
                    break
                line[index] = guess.upper()
                index += 1
                print(guess)
        else:
            print('invalid input')
        print(display_list)

def statboard():
    global words, errors, statboard
    
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
                                    print(statboard.format(name, num_of_games_choosen, num_of_games_played, num_of_games_won,
                                    words['game 1'], words['game 2'], words['game 3'], words['game 4'],words['game 5'],
                                    errors['game 1'], errors['game 2'], errors['game 3'], errors['game 4'],errors['game 5']))
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

def appendinfo(name, games, plays, wins):
    player_info.append(name)
    player_info.append(games)
    player_info.append(plays)
    player_info.append(wins)
    return player_info
#-------------- Main Code ---------------
player_name, number_of_games_chosen, strikes = gamesetup()
#category_select()
#window()
#word_randomiser()
#checker()
player_info = appendinfo(player_name, number_of_games_chosen, '2', '1')  #number_of_games_played, number_of_games_won
#statboard()
print(player_info)

