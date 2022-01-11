# from board import *
# from players import *
from time import sleep
from termcolor import colored, cprint
import maedn

#maedn.start_up.print_board()

active_player = maedn.start_up.one
print(active_player)
print(active_player.team)
maedn.movement.position_check(active_player.team)

#maedn.movement.one1.move()


# Message=input("Enter Your Message") 
# if Message=="Hello": 
#     one1.move()
# else: 
#     print("Bye") 

