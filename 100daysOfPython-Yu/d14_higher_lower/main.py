    """Breakdown:
    -logo of the game gets printed
    -data A (values from list/dict "data" by value: name, description, country -> choosen randomly) gets printed
    -logo : VS gets printed
    -data B (values from list/dict "data" by value: name, description, country -> choosen randomly) gets printed
    -Player chooses if option B hast HIGHER or LOWER amount of followers
    -if Player wrong game is over/ counter is displayed
    -else Player is right and counter += 1 / data A = data B / new data B is again choosen randomly from list/dict / game repeats 
    """
    
    """To-Do-list:
    +print game logo
    -from constants.data: 
        -choose random list item
        -get list items keys and values > move to new constant via dict comprehension 
        -assign to dict_A/B as a list
        -embedd into a def
    -use def in main to create random lists for A,B 
    -compare follower_count of A,B (higher, lower)
    -if player wrong > print(lost + constants.round_count)
    -else player wins round > reassign A = B ; create new B via def; rerun until is_game_lost = True
    """
    
    """Comments:
    """
    


import constants
import functions
import random

print (constants.logo)

print(constants.data[4]['description'],['country'])