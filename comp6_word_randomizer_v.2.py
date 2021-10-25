'''
    Author: Riley Anderson
    Date: 23/10/2021
    Description: Word randomizer
    version: 2.0
    Changes: made a system to check if the item was already in the new list,
             also finish when both lists and the same length
'''
already_picked = []
list_for_random = ['p', 'k', 'l', 'o', 'r', '5']
import random as r
while(True):
    word = r.choice(list_for_random)
    print(word)
    if word not in already_picked:
        already_picked.append(word)
        print(already_picked)
    else:
        print('invalid input, choose again')
        print(already_picked)
    input('')
    if len(already_picked) == len(list_for_random):
        print("complete")
        break
