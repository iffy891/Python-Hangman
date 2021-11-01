#-------------- Libraries ------------
import random as r
import tkinter as tk
import turtle as t

category = []
already_picked = []
word_length = []
guesses = []
outcomes = []
categories = {
        'country names':
        ['new zealand', 'australia', 'belize', 'djibouti', 'india',
        'north korea', 'qatar', 'south africa', 'vietnam', 'zambia',
        'yemen'],
        'cartoon characters':
        ['bugs bunny', 'donald duck', 'popeye', 'scooby-doo',
        'mickey mouse', 'spider-man', 'pink panther', 'taz',
        'yosemite sam', 'patrick star', 'shrek', 'puss in boots',
        'master splinter', 'spongebob squarepants', 'pikachu',
        'charmander'],
        'tv shows' :
        ['squid game', 'friends', 'shortland street', 'horders', 'one news', 'three news',
        'treasure island', 'survivor', 'greys anatomy', 'game of thrones', 'lucifer',
        'the office', 'stranger things', 'wellington paranormal'],
        'heros vs villians': ['wonder woman', 'batman', 'iron man', 'hulk', 'captain america',
        'flash', 'black widow', 'catwoman', 'Maleficent', 'yoda', 'optimus prime',
        'megatron', 'venom', 'thor', 'captain marvel', 'thanos', 'harley quinn', 'batwoman',
        'powerwoman'],
        'eye spy':
        ['tree', 'window', 'chair', 'door', 'light', 'sky', 'table'],
        'vehicle models':
        ['mustang', 'civic', 'corvette', 'corolla', 'cherokee', 'beetle', 'highlander', 'cr-v',
        'ranger', 'land cruiser', 'forester', 'focus', 'hr-v', 'golf', 'outlander', 'santa fe'],
        'food chains':
        ['mcdonalds', 'kfc', 'wendy\'s', 'starbucks', 'burgerfuel', 'subway', 'pizza hut', 'domino\'s'],
        'planes':
        ['wings', 'landing gear', 'engines', 'air new zealand', 'airport', 'terminal', 'flight'],
        'random':
        ['new zealand', 'australia', 'belize', 'djibouti', 'india',
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
#------------ Functions -----------------

def setup_once():
    '''
    This function will only need to be called once to get the 
    players name and the number of games the player intends on 
    playing.
    '''
    while(True):
        player_name = input('Please enter a name (Max length=10, No special characters allowed e.g. #@$!%^&*(), No spaces): ')
        if(((player_name.isalnum() == True) or (player_name.isalpha() == True) or
            (player_name.isnumeric() == True)) and (len(player_name) <= 10 )):
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
            while(True):
                num_games_chosen = int(input("How many games would you like to play (1-5)?: "))
                if ((num_games_chosen <= 5) and (num_games_chosen >=1)):
                    strikes = 10
                    break
                else:
                    print("invalid Input")
            break
        else:
            print("Invalid Input")
    player_info = [player_name, num_games_chosen]
    #return player_info, num_games_chosen
    categoryselection(player_info, num_games_chosen, strikes)
def categoryselection(player_info, num_games_chosen, strikes):
    
    
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
    category.append(selected_category)
    main_game(player_info, num_games_chosen, selected_category, strikes)

def main_game(player_info, num_games_chosen, selected_category, strikes): #main_game(selected_category)
    while(True):
        word = r.choice(categories[selected_category])
        if word not in already_picked:
            already_picked.append(word)
            break
    for x in word:
        if '-' == x:
            word_length.append('-')
        elif ' ' == x:
            word_length.append(' ')
        elif '\'' == x:
            word_length.append('\'')
        else:
            word_length.append('_')
    hidden_word = ' '.join(word_length)
    window(hidden_word, word, player_info, num_games_chosen, selected_category, strikes)


def window(hidden_word, word, player_info, num_games_chosen, selected_category, strikes):
    root = tk.Tk()
    root.title('Hangman')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width, height))

    #tp == top
    tp_frame = tk.Frame(root)
    tp_frame.pack(side = tk.TOP)

    canvas = tk.Canvas(tp_frame, width=700, height=500)
    canvas.pack(side=tk.RIGHT, anchor='ne', padx=10)

    screen = t.TurtleScreen(canvas)
    screen.bgcolor('white')
    draw = t.RawTurtle(screen)
    draw_board_setup(draw)

    #lt == list
    lt_frame = tk.Frame(tp_frame, bg='blue', width=700, height=500)
    lt_frame.pack_propagate(0)
    lt_frame.pack(side=tk.LEFT, padx=10, anchor='nw')

    #lbl == label
    lbl_1 = tk.Label(lt_frame, text=guesses, font=('comic Sans Ms','20', 'normal'))
    lbl_1.pack()

    #btm == bottom
    btm_frame = tk.Frame(root, width=1300, height=600, bg='red')
    btm_frame.pack_propagate(0)
    btm_frame.pack(side=tk.BOTTOM, anchor='s')
    btm_lbl = tk.Label(btm_frame, font=('comic Sans Ms', '30', 'bold'), text=hidden_word)
    btm_lbl.place(x=20, y=100)

    #ent == entry
    guess_ent = tk.Entry(btm_frame, width=10)
    guess_ent.pack(ipadx=10, anchor='n')
    ent_btn = tk.Button(btm_frame, text='submit', command = lambda: strikes == submit(hidden_word, word, player_info, num_games_chosen, selected_category, strikes, btm_lbl, guess_ent, lbl_1, root, draw)) #submit(strikes, word, btm_lbl,guess_ent, lbl_1, root)
    ent_btn.pack(anchor='n')
    print(strikes)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()

def draw_board_setup(draw):
    draw.penup()
    draw.goto(0,-100)
    draw.left(90)
def hangman(draw, strikes):
    draw.pendown()
    print(strikes)
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
        
def submit(hidden_word, word, player_info, num_games_chosen, selected_category, strikes, btm_lbl, guess_ent, lbl_1, root, draw): #submit(strikes, word, btm_lbl,guess_ent, lbl_1, root)
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
    if(guess.isalpha() == True) and (guess.upper() not in guesses) and (len(guess) == 1):
        index = 0
        guesses.append(guess.upper())
        lbl_1['text'] = guesses
        if guess in word:
            while index < len(word):
                index = word.find(guess.lower(), index)
                if index == -1:
                    break
                word_length[index] = guess.upper()
                hidden_word = ' '.join(word_length)
                index += 1
            btm_lbl['text'] = hidden_word
            if '_' not in word_length:
                btm_lbl['text'] = 'WINNER'
                outcome = 'won'
                end_game(outcome, player_info, num_games_chosen, selected_category, root, strikes)
            
        else:
            strikes -= 1
            hangman(draw, strikes)
            if strikes == 0:
                btm_lbl['text'] = 'LOSER'
                outcome = 'lost'
                end_game(outcome, player_info, num_games_chosen, selected_category, root, strikes)
        
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
    return strikes

def end_game(outcome, player_info, num_games_chosen, selected_category, root, strikes):
    #global games_played, word_length, hidden_word, guesses, num_games_chosen
    games_played = 0
    games_played += 1
    
    if outcome == 'won':
        outcomes.append(outcome)
        
        if num_games_chosen > 1:
            winning_msg = tk.messagebox.askyesno(title= 'WINNER', message='''
    You have won, Would you like to Play the next game or Exit the game?
    [If you would like to continue click \'yes\', if not click \'no\' to
    end the game and continue to statboard]''')
            num_games_chosen -= 1
            if winning_msg == True:
                #print('True')
                word_length = []
                hidden_word = ''
                word = ''
                guesses = []
                root.destroy()
                main_game(hidden_word, word_length, guesses, word, strikes)
            elif winning_msg == False:
                #print('False')
                root.destroy()
                statboard(player_info, games_played)
            
        elif num_games_chosen == 1:
            winning_msg = tk.messagebox.askyesno(title= 'WINNER', message='''
You have won, Would you like to set up another or exit the game?
[If you would like to set up another game click \'yes\', if not click \'no\' to
end the game and continue to statboard]''')
            if winning_msg == True:
                #print('True')
                word_length = []
                hidden_word = ''
                word = ''
                guesses = []
                root.destroy()
                categoryselection()
            elif winning_msg == False:
                root.destroy()
                statboard(player_info, games_played)
    if outcome == 'lost':
        outcomes.append(outcome)
        if num_games_chosen > 1:
            losing_msg = tk.messagebox.askyesno(title='LOSER', message='''
    You have lost, Would you like to Play the next game or Exit the game?
    [If you would like to continue click \'yes\', if not click \'no\' to
    end the game and continue to statboard]''')
            if losing_msg == True:
                #print('True')
                word_length = []
                hidden_word = ''
                word = ''
                guesses = []
                root.destroy()
                main_game()
            elif losing_msg == False:
                root.destroy()
                statboard(player_info, games_played)
            num_games_chosen -= 1
        elif num_games_chosen == 1:
            losing_msg = tk.messagebox.askyesno(title='LOSER', message='''
You have lost, Would you like to set up another or exit the game?
[If you would like to set up another game click \'yes\', if not click \'no\' to
end the game and continue to statboard]''')
            if losing_msg == True:
                #print('True')
                word_length = []
                hidden_word = ''
                word = ''
                guesses = []
                root.destroy()
                categoryselection()
            elif losing_msg == False:
                root.destroy()
                statboard(player_info, games_played)

                
def statboard(player_info, games_played):
    num_wins = outcomes.count('won')
    games_categories = ', '.join(category)
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
'''.format(player_info[0], player_info[1], games_played, num_wins, games_categories))
    input('Press enter to fully exit the came:')
    exit()       
        
    
    
setup_once()
