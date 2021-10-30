'''
    Author: Riley Anderson
    Date: 27/10/2021
    Description: Rewrite of other app
    Version: 2.0
'''

#------------ Libraries --------------
import tkinter as tk
import turtle as t
import random as r

#---------------- Functions ----------
global guess
def comp1():
    '''
    This function will get the basics of the game sorted,
    e.g. player input for their name and how many games
    they want to play. Also letting the player know what
    they need to know.
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
        player_name = input("Please enter a name (Max length = 10, No special characters allowed e.g. !@#$%^&*(), No spaces): ")
        if(((player_name.isalnum() == True) or (player_name.isalpha() == True) or (player_name.isnumeric() == True)) and (len(player_name) <= 10)):
            print(rules)
            while(True):
                number_of_games_chosen = input("How many game would you like to play (1-5)?: ")
                if(number_of_games_chosen.isnumeric() == True) and ((int(number_of_games_chosen) <= 5) and (int(number_of_games_chosen) >=1)):
                    strikes = 10
                    break
                else:
                    print("Invalid Input") #Change invalid input for something more helpful

            return player_name, number_of_games_chosen, strikes
        else:
            print("Invalid Input")
def submit(guess_entry):
    guess = guess_entry.get()
    print(guess)
def comp2():
    '''
    This function will make a gui window
    '''
    def drawing_board_setup():
        draw.penup()
        draw.goto(0, -100)
        draw.left(90)
        hangman(10)
    def hangman(strikes):     
        draw.pendown()
        if strikes == 9:
            draw.forward(300)
        elif strikes == 8:
            draw.right(90)
            draw.forward(150)
        elif strikes == 7:
            draw.right(90)
            draw.forward(50)
        elif strikes == 6:
            draw.right(90)
            draw.circle(20)
        elif strikes == 5:
            draw.left(90)
            draw.penup()
            draw.forward(40)
            draw.pendown()
            draw.forward(70)
        elif strikes == 4:
            draw.left(45)
            draw.forward(50)
        elif strikes == 3:
            draw.left(180)
            draw.penup()
            draw.forward(50)
            draw.left(90)
            draw.pendown()
            draw.forward(50)
        elif strikes == 2:
            draw.penup()
            draw.right(180)
            draw.forward(50)
            draw.left(45)
            draw.forward(40)
            draw.pendown()
            draw.right(135)
            draw.forward(30)
        elif strikes == 1:
            draw.penup()
            draw.right(180)
            draw.forward(30)
            draw.left(90)
            draw.pendown()
            draw.forward(30)
        elif strikes == 0:
            draw.penup()
            draw.right(180)
            draw.forward(30)
            draw.left(45)
            draw.forward(60)
            draw.left(90)
            draw.forward(5)
            draw.pendown()
            draw.dot(5, 'black')
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
        #entry.delete(0)
    window = tk.Tk()
    window.title("Hangman")
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry('%dx%d' % (width, height))
    #----------------------------------------
    top_frame = tk.Frame(window) 
    top_frame.pack(side=tk.TOP)
    canvas = tk.Canvas(top_frame)
    canvas.config(width=700, height=500)
    canvas.pack(side=tk.RIGHT, anchor='ne', padx=10)
    list_frame = tk.Frame(top_frame,bg='blue', width=700,
                          height=500) #For final get rid of bg color
    list_frame.pack_propagate(0)
    list_frame.pack(side=tk.LEFT, padx=10, anchor='nw')
    label = tk.Label(list_frame)
    label.pack()
    #-----------------------------------------------
    screen = t.TurtleScreen(canvas)
    screen.bgcolor('white')
    draw = t.RawTurtle(screen)
    drawing_board_setup()
    #-----------------------------------------------
    bottom_frame = tk.Frame(window, width=1300, height=600, bg='red') #For final get rid of bg color
    bottom_frame.pack_propagate(0)
    bottom_frame.pack(side=tk.BOTTOM, anchor='s')
    bottom_label = tk.Label(bottom_frame) #This will change depending on the word length, will need to pass through a list
    bottom_label.place(x=300, y=100)
    guess_entry = tk.Entry(bottom_frame, width=10)
    guess_entry.pack(ipadx=10, anchor='n')
    entry_btn = tk.Button(bottom_frame, text='submit', command= lambda: submit(guess_entry))
    entry_btn.pack(side=tk.RIGHT)

    window.mainloop()
    return guess
def comp3():
    '''
    This function is for the user to select a category
'''
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
        if category_selection == '1' or category_selection.lower() == 'country names':
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
        return selected_category

def comp4(selected_category):
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
    already_picked = []
    while(True):
        word = r.choice(categories[selected_category])
        if word not in already_picked:
            already_picked.append(word)
            input('')
            print(word, already_picked)
            return word
            break
        else:
            print('Invalid Input, Choose Again')

def comp5(word):
    guesses = []
    word_length = []
    unknown = '_'
    for x in word:
        if '-' == x:
            word_length.append('-')
        elif ' ' == x:
            word_length.append(' ')
        else:
            word_length.append(unknown)
    
    while(True):
        print(*word_length, sep=' ')
        if '_' not in word_length:
            print('You Win')
            break
        

        if(guess.isalpha() == True) and (guess.lower() not in guesses) and (len(guess) == 1):
            index = 0
            guesses.append(guess.lower())
            if guess in word:
                while index < len(word):
                    index = word.find(guess.lower(), index)
                    if index == -1:
                        print("Incorrect")
                        break
                    line[index] = guess.upper()
                    index +=1
        else:
            print("Invalid Input")
            
        
#------- main game -----------
#player_name, number_of_games_chosen, strikes = comp1()
guess = comp2()
print(guess)
selected_category = comp3()
word = comp4(selected_category)
comp5(word)


                    
