from start_up import *
from movement import *
from q import *
from time import sleep
from termcolor import colored, cprint

print_board()

print(active_player.name)
dice_check(active_player.team)
next_player()

print(active_player.name)
dice_check(active_player.team)
next_player()

dice_check(active_player.team)
next_player()

dice_check(active_player.team)
next_player()
#start_check(active_player.team)

#one1.move()

next_player()




# Message=input("Enter Your Message") 
# if Message=="Hello": 
#     one1.move()
# else: 
#     print("Bye") 

