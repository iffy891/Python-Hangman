'''
    Author: Riley Anderson
    Date: 23/10/2021
    Description: Game category selection
    version: 4.0
    Changes: Made the validation wider so the user has more of a choice, to input the number or the name of the category choosen.
'''
import random as r
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



while(True):
    category = None
    cat = input('''
CATEGORIES:
1. country names
2. cartoon characters
3. tv shows
4. heros vs villians
5. eye spy
6. vehicle models
7. food chains
8. planes
9. random
please select a category:''')
    if int(cat) == 1 or cat.lower() == 'country names':
        category = 'country names'
    elif int(cat) == 2 or cat.lower() == 'cartoon characters':
        category = 'cartoon characters'
    elif int(cat) == 3 or cat.lower() == 'tv shows':
        category = 'tv shows'
    elif int(cat) == 4 or cat.lower() == 'heros vs villians':
        category = 'heros vs villians'
    elif int(cat) == 5 or cat.lower() == 'eye spy':
        category = 'eye spy'
    elif int(cat) == 6 or cat.lower() == 'vehicle models':
        category = 'vehicle models'
    elif int(cat) == 7 or cat.lower() == 'food chains':
        category = 'food chains'
    elif int(cat) == 8 or cat.lower() == 'planes':
        category = 'planes'
    elif int(cat) == 9 or cat.lower() == 'random':
        category = 'random'
    else:
        print("invalid input")

    if category != None:
        cat_choice = categories[category]
        word = r.choice(cat_choice)
        print(word)
    else:
        print("Invalid input")

    
