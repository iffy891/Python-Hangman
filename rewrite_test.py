import tkinter as tk
import turtle as t
import random as r

strikes = 10
guesses = []
word_length = []
word = ''
selected_category = ''
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
player_info = []

games_played = 0
outcomes = []
already_picked = []
def end_game_win():
    global games_played, word_length, selected_category
    outcomes.append('Won')
    games_played += 1
    if int(num_games_chosen) > 1:
        winning_msg = tk.messagebox.askyesno(title='WINNER', message='''
    You have won, Would you like to Play the next game or Exit the game?
    [If you would like to continue click \'yes\', if not click \'no\' to
    end the game and continue to statboard]''')
        #if yes, it will clear the board and reset things
        if winning_msg == True:
            strikes = 10
            print(winning_msg)
            guesses, word_length, word, selected_category = word_random(selected_category, already_picked, word_length)
            guesses = []
            lbl_1['text'] = guesses
            btm_lbl['text'] = word_length
            testing_msg = tk.messagebox.showinfo(title='TESTING',
                                                 message=('''
word: {}
word length: {}
strikes : {}
'''.format(word, word_length, strikes)))
            
            
        #if no then it will kill the window and print out the statboard
        elif winning_msg == False:
            print(winning_msg)
            window.tk.destroy()
            statboard()
    elif int(num_games_chosen) == 1:
        winning_msg = tk.messagebox.askyesno(title='WINNER', message='''
You have won, Would you like to set up another or exit the game?
[If you would like to set up another game click \'yes\', if not click \'no\' to
end the game and continue to statboard]''')
        #if yes, it will kill the window and go to the category selection area
        if winning_msg == True:
            window.tk.destroy()
            strikes = 10
            lbl_1['text'] = ''
            btm_lbl['text'] = ''
            make_game(selected_category, already_picked)
        #if no, it will kill the window and print out the statboard
        elif winning_msg == False:
            window.tk.destroy()
            statboard()
def end_game_lose():
    outcomes.append('Lost')
    games_played += 1
    if int(num_games_chosen) > 1:
        losing_msg = tk.messagebox.askyesno(title='LOSER', message='''
    You have lost, Would you like to Play the next game or Exit the game?
    [If you would like to continue click \'yes\', if not click \'no\' to
    end the game and continue to statboard]''')
        #if yes, it will clear the board and reset things
        if losing_msg == True:
            strikes = 10
            lbl_1['text'] = ''
            btm_lbl['text'] = ''
            word_random()
        #if no then it will kill the window and print out the statboard
        elif winning_msg == False:
            window.tk.destroy()
            statboard()
    elif int(num_games_chosen) == 1:
        losing_msg = tk.messagebox.askyesno(title='LOSER', message='''
You have lost, Would you like to set up another or exit the game?
[If you would like to set up another game click \'yes\', if not click \'no\' to
end the game and continue to statboard]''')
        #if yes, it will kill the window and go to the category selection area
        if losing_msg == True:
            strikes = 10
            lbl_1['text'] = ''
            btm_lbl['text'] = ''
            make_game()
        #if no, it will kill the window and print out the statboard
        elif winning_msg == False:
            window.tk.destroy()
            statboard()
    
def draw_board_setup():
    draw.penup()
    draw.goto(0, -100)
    draw.left(90)

def hangman():
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
def submit(word):
    global strikes, word_length
    guess_ent.config(state='disabled')
    guess = guess_ent.get()
    warning = ''
    special_chars = ['!','@','#','$','%',
                     '^','&','*','(',')',
                     '-','_','+','=','\\',
                     '|', '`','~','{','}',
                     '[',']',';',':','\'',
                     '"', ',', '<', '.','>',
                     '/','?']
    
    print(word)
    if(guess.isalpha() == True) and (guess.upper() not in guesses) and (len(guess) == 1):
        print(word)
        index = 0
        guesses.append(guess.upper())
        if guess in word:
            print('True')
            while index < len(word):
                index = word.find(guess.lower(), index)
                if index == -1:
                    break
                word_length[index] = guess.upper()
                index += 1
            btm_lbl['text'] = word_length
            if '_' not in word_length:
                btm_lbl['text'] = 'WINNER'
                end_game_win()
            if strikes == 0:
                print(strikes)
                btm_lbl['text'] = 'LOSER'
                end_game_lose()
        else:
            strikes -= 1
            hangman()
            
        lbl_1['text'] = guesses
        guess_ent.config(state='normal')
        guess_ent.delete(0)
    else:
        if guess == '':
            guess = '<blank>'
        
        if guess.isalpha() == False and guess.isspace() == False and guess != '<blank>':
            if guess.isnumeric() == False or guess.isalnum() == False:
                for x in guess:
                    if x in special_chars:
                        guess_ent.config(state='normal')
                        guess_ent.delete(0, tk.END)
                msg = tk.messagebox.showwarning(title='Invalid Input', message = "Please enter a letter from the english alphabet, not symbols and punctuation.")
            else:
                msg = tk.messagebox.showwarning(title='Invalid Input', message = "Please input letters from the alphabet only.")
                guess_ent.config(state='normal')
                guess_ent.delete(0)
        elif guess.upper() in guesses:
            msg = tk.messagebox.showwarning(title='Invalid Input', message = "You have already made this guess, Please enter one you have not tried")
            guess_ent.config(state='normal')
            guess_ent.delete(0)
        elif len(guess) > 1 and guess.isspace() == False and guess != '<blank>':
            msg = tk.messagebox.showwarning(title='Invalid Input', message = "Please enter only 1 character")
            guess_ent.config(state='normal')
            guess_ent.delete(0, tk.END)
        elif guess.isspace() == True or guess == '<blank>':
            msg = tk.messagebox.showwarning(title='Invalid Input', message = "You have not entered a guess, please enter a guess.")
            guess_ent.config(state='normal')
            if guess == ' ':
                guess_ent.delete(0)

    
        
            
        
def begin_game_setup():
    while(True):
        player_name = input("Please enter a name (Max length 10 charactersn No special Characters allowed e.g. !@#$%^&*(), No spaces): ")
        if(((player_name.isalnum() == True) or (player_name.isalpha() == True) or (player_name.isnumeric() == True)) and (len(player_name) <= 10)):
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
            Have fun!!!!''')
            while(True):
                num_games_chosen = input("How many games would you like to play (1-5)?: ")
                if(num_games_chosen.isnumeric() == True) and ((int(num_games_chosen) <= 5) and (int(num_games_chosen) >=1)):
                    break
                else:
                    print("Invalid Input")
            break
        else:
            print("Invalid Input")
    return player_name, num_games_chosen
def make_game():
    global word_length
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
            break
        elif category_selection == "2" or category_selection.lower() == 'cartoon characters':
            selected_category = 'cartoon characters'
            break
        elif category_selection == '3' or category_selection.lower() == 'tv shows':
            selected_category = 'tv shows'
            break
        elif category_selection == '4' or category_selection.lower() == 'heros vs villians':
            selected_category = 'heros vs villians'
            break
        elif category_selection == '5' or category_selection.lower() == 'eye spy':
            selected_category = 'eye spy'
            break
        elif category_selection == '6' or category_selection.lower() == 'vehicle models':
            selected_category = 'vehicle models'
            break
        elif category_selection == '7' or category_selection.lower() == 'food chains':
            selected_category = 'food chains'
            break
        elif category_selection == '8' or category_selection.lower() == 'planes':
            selected_category = 'planes'
            break
        elif category_selection == '9' or category_selection.lower() == 'random':
            selected_category = 'random'
            break
        else:
            print("invalid input")
    guesses, word_length, word, selected_category = word_random(selected_category, already_picked, word_length, word)
    
    return guesses, word_length, word, selected_category   
    
def word_random(selected_category, already_picked, word_length, word):
    print(selected_category)
    print(word)
    while(True):
        word = r.choice(categories[selected_category])
        if word not in already_picked:
            already_picked.append(word)
            break
    guesses = []
    word_length.clear()
    unknown= '_'
    print(word)
    for x in word:
        if '-' == x:
            word_length.append('-')
        elif ' ' == x:
            word_length.append(' ')
        elif "'" == x:
            word_length.append("'")
        else:
            word_length.append(unknown)
    print(word_length)
    return guesses, word_length, word, selected_category
    
def statboard():
    num_wins = outcomes.count('Won')
    print('''
=============================================================================================================================================================
                                                        ||                 YOUR PLAY                 ||
=============================================================================================================================================================


        Player Name: {}

        Number of Games Choosen to play: {}

        Number of Games Played: {}

        Number of Games Won: {}

        Category: {}

=============================================================================================================================================================

=============================================================================================================================================================
'''.format(player_name, num_games_chosen, num_wins, selected_category))

    
player_name, num_games_chosen = begin_game_setup()
guesses, word_length, word, selected_category = make_game()
window = tk.Tk()
window.title("Hangman")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d' % (width, height))
'''
The top frame will include the hangman timer
and the "already guessed list"

- The Hangman timer:
    This will draw certain parts
    with different strikes left
    using the strike variable

- the "already guesses list":
    This will update through out
    the game adding every guess
'''

#tp == top

tp_frame = tk.Frame(window)
'''
This is the main frame of which each
one will be located together
'''
tp_frame.pack(side=tk.TOP)
canvas = tk.Canvas(tp_frame)
canvas.config(width=700, height=500)
canvas.pack(side=tk.RIGHT, anchor='ne', padx=10)
'''
This is the canvas which will graphically
show the player how many incorrect guesses
they have left
'''
screen = t.TurtleScreen(canvas)
screen.bgcolor('white')
draw = t.RawTurtle(screen)
draw_board_setup()
#lt == list

lt_frame = tk.Frame(tp_frame, bg='blue', width=700,
                    height=500) #The colour will most likely be changed or invalid
lt_frame.pack_propagate(0)
lt_frame.pack(side=tk.LEFT, padx=10, anchor='nw')

#lbl == label
lbl_1 = tk.Label(lt_frame, text=guesses, font=('comic Sans Ms', '20', 'normal'))
lbl_1.pack()

#btm == bottom

btm_frame = tk.Frame(window, width=1300,
                     height=600, bg='red')#The colour will most likely be changed or invalid
btm_frame.pack_propagate(0)
btm_frame.pack(side=tk.BOTTOM, anchor='s')
btm_lbl = tk.Label(btm_frame,font=('comic Sans Ms', '30', 'bold'), text=word_length)#text will equal the length of the chosen word
btm_lbl.place(x=20, y=100)

#ent == entry, btn == button

guess_ent = tk.Entry(btm_frame, width=10)
guess_ent.pack(ipadx=10, anchor='n')
ent_btn = tk.Button(btm_frame, text='submit', command= lambda: strikes == submit(word)) #This will submit the users guess
ent_btn.pack(anchor='n')
#guess_ent.bind('<Return>',lambda: strikes == submit())
window.lift()
window.attributes('-topmost',True)
window.after_idle(window.attributes,'-topmost',False)
window.mainloop()

    


        
