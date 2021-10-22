'''
    Author: Riley Anderson
    Date: 21/10/2021
    Description: Game category selection
    version: 2.0
    Changes: instead of needing the name of the category it will take the number.
'''

country_names = ['new zealand', 'australia', 'belize', 'djibouti', 'india',
                 'north korea', 'qatar', 'south africa', 'vietnam', 'zambia',
                 'yemen']
cartoon_characters = ['bugs bunny', 'donald duck', 'popeye', 'scooby-doo',
                      'mickey mouse', 'spider-man', 'pink panther', 'taz',
                      'yosemite sam', 'patrick star', 'shrek', 'puss in boots',
                      'master splinter', 'spongebob squarepants', 'pikachu',
                      'charmander']
tv_shows = ['squid game', 'friends', 'shortland street', 'horders', 'one news', 'three news',
            'treasure island', 'survivor', 'greys anatomy', 'game of thrones', 'lucifer',
            'the office', 'stranger things', 'wellington paranormal']
heros_vs_villians = ['wonder woman', 'batman', 'iron man', 'hulk', 'captain america',
                    'flash', 'black widow', 'catwoman', 'Maleficent', 'yoda', 'optimus prime',
                     'megatron', 'venom', 'thor', 'captain marvel', 'thanos', 'harley quinn', 'batwoman',
                     'powerwoman']
eye_spy = ['tree', 'window', 'chair', 'door', 'light', 'sky', 'table']
vehicle_models = ['mustang', 'civic', 'corvette', 'corolla', 'cherokee', 'beetle', 'highlander', 'cr-v',
                  'ranger', 'land cruiser', 'forester', 'focus', 'hr-v', 'golf', 'outlander', 'santa fe']
food_chains = ['mcdonalds', 'kfc', 'wendy\'s', 'starbucks', 'burgerfuel', 'subway', 'pizza hut', 'domino\'s']
planes = ['wings', 'landing gear', 'engines', 'air new zealand', 'airport', 'terminal', 'flight']

random = country_names + cartoon_characters + tv_shows + heros_vs_villians + eye_spy + vehicle_models + food_chains + planes
while(True):
    category = input('''
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
    if int(category) == 1:
        print(*country_names, sep=', ')
    elif int(category) == 2:
        print(*cartoon_characters, sep=', ')
    elif int(category) == 3:
        print(*tv_shows, sep=', ')
    elif int(category) == 4:
        print(*heros_vs_villians, sep=', ')
    elif int(category) == 5:
        print(*eye_spy, sep=', ')
    elif int(category) == 6:
        print(*vehicle_models, sep=', ')
    elif int(category) == 7:
        print(*food_chains, sep=', ')
    elif int(category) == 8:
        print(*planes, sep=', ')
    elif int(category) == 9:
        print(*random, sep=',')
    else:
        pass
