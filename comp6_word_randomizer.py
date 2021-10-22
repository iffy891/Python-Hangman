'''
    Author: Riley Anderson
    Date: 22/10/2021
    Description: Word randomizer, basic made
    version: 1.0
'''
already_picked = []
list_for_random = ['p', 'k', 'l', 'o', 'r', '5']
import random as r
while(True):
    word = r.choice(list_for_random)
    print(word)
    already_picked.append(word)
    print(already_picked)
    input('')
