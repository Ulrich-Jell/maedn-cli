import random
import os
import maedn
from termcolor import colored, cprint
from time import sleep

     
class Meeple():
    def __init__(self, color, no,  home, route, progress, x_pos, y_pos, old_pos, en_route):
        self.color = color
        self.no = no
        self.home = home
        self.route = route
        self.progress = progress
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.old_pos = old_pos
        self.en_route = en_route
        

    def move(self):
        #sleep(1)
        d = 6 #random.randint(2, 6)        
        for s in range (1, d):
            self.go()
            maedn.start_up.print_board()

        if maedn.start_up.board[self.route[self.progress +1][0]][self.route[self.progress +1][1]] == "()":
            self.go()
            maedn.start_up.print_board()
        else:
            print("geht nicht")
            
        print(d)

    def go(self):
        maedn.start_up.board[self.x_pos][self.y_pos] = self.old_pos
        sleep(1)
        self.progress += 1
        self.x_pos =self.route[self.progress][0] # route1[1][0] => 2
        self.y_pos =self.route[self.progress][1] # route1[1][1] => 12
        self.old_pos = maedn.start_up.board[self.x_pos][self.y_pos]
        maedn.start_up.board[self.x_pos][self.y_pos] = colored(self.no, self.color)
        os.system('cls' if os.name == 'nt' else 'clear')

def position_check(team):
    print(team)
    t = []
    for w in team:
        print(w.en_route)
        if w.en_route == True:
            t.append(True)
        else:
            t.append(False)

    print(t)

    if True in t:
        print("einal würfeln")
    else:
        print("drei Mal würfeln")
        
        

#route = {0:[0,12], 1:[2,12], 2:[4,12], 3:[6,12], 4:[8,12], 5:[8,14], 6:[8,16]

one1 = Meeple(maedn.start_up.one.color, "1 ", "board[2][15]", maedn.start_up.route1, 1, 2, 12, "()", True) #colored(maedn.start_up.board[2][15], maedn.start_up.one.color), True)
one2 = Meeple(maedn.start_up.one.color, "2 ", "board[2][17]", maedn.start_up.route1, 2, 4, 12, "()", True) #colored(maedn.start_up.board[2][15], maedn.start_up.one.color), True)

team1 = [one1, one2]
