import random
import os
import time
from start_up import *
from termcolor import colored, cprint
from time import sleep

global active_player
active_player = four
   
class Meeple():
    def __init__(self, player, no,  home, route, progress, x_pos, y_pos, old_pos):#, name):
        self.player = player
        self.no = no
        self.home = home
        self.route = route
        self.progress = progress
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.old_pos = old_pos
        #self.name = name
        

    def move(self, dice):               
        for s in range (1, dice):
            self.go()
            print_board()

        if board[self.route[self.progress +1][0]][self.route[self.progress +1][1]] == "()":
            self.go()
            print_board()
            if dice == 6:
                start_check(self.player.team)
            else:
                print("nächster spieler")
        else:
            print("geht nicht")

    def go(self):
        board[self.x_pos][self.y_pos] = self.old_pos
        sleep(1)
        self.progress += 1
        self.x_pos =self.route[self.progress][0] # route1[1][0] => 2
        self.y_pos =self.route[self.progress][1] # route1[1][1] => 12
        self.old_pos = board[self.x_pos][self.y_pos]
        board[self.x_pos][self.y_pos] = colored(self.no, self.player.color)
        os.system('cls' if os.name == 'nt' else 'clear')

def next_player():
    if active_player.name == "four":
        active_player = one
        
   
    else:    
        players = [one, two, three, four]
        active_player = players[(players.index(active_player)) + 1]

    print("Player ", active_player.name, ". It's your turn.")

def dice_check(team):
    #from main import active_player
    t = []
    print(t)
    for m in team:
        print(m.progress)
        if m.progress != "H":
            t.append(True)
        else:
            t.append(False)    
    
    if True in t:        
        dice = random.randint(1, 6)
        print("Player " + active_player.name + " rolls a " + str(dice))
        input("Press any key to continue")

    else:
        d = []
        d.append(random.randint(1, 6))
        d.append(random.randint(1, 6))
        d.append(random.randint(6, 6))
        print("Player " + active_player.name + " rolls a "+ str(d[0]), " a " + str(d[1]) + " and a " + str(d[2]))
        
        if 6 in d:
            input("Press any key to move one meeple out of the start")
            for m in team:
                if m.progress =="H":
                    board[m.x_pos][m.y_pos] = colored("()", m.player.color)
                    m.progress = 0
                    m.x_pos =m.route[0][0]
                    m.y_pos =m.route[0][1]
                    board[m.x_pos][m.y_pos] = colored(m.no, "grey", "on_" + str(m.player.color))
                    m.old_pos = colored("()", "grey", "on_"+str(m.player.color))
                    print_board()
                    r = random.randint(1,5)
                    print("Player " + active_player.name + " rolls a " + str(r))
                    input("Press any key to continue")
                    m.move(r)
                    break
            
        else:
            print("Unfortunately, you did not roll a 6.")
            input("Press any key to let the next player continue.")

def start_check(team):
    t = []
    for m in team:
        if m.progress == 0:
            t.append(True)
        else:
            t.append(False)

    if True in t:
        h = []
        for m in team:
            if m.home == "board[" + str(m.x_pos) + "][" + str(m.y_pos) + "]":
                h.append(True)
            else:
                h.append(False)
        
        if True in h:
            print("start räumen - zugzwang")
        else:
            print("Haus ist leer - freie wahl")
    
    else:
        print("start frei - freie Wahl")
        
        

#route = {0:[0,12], 1:[2,12], 2:[4,12], 3:[6,12], 4:[8,12], 5:[8,14], 6:[8,16]

########## blueprint - do not change ##########
one1 = Meeple(one, "1 ", "board[2][15]", route1, "H", 2, 15, board[2][15])#, "Adalbert")
one2 = Meeple(one, "2 ", "board[2][17]", route1, "H", 2, 17, board[2][17])#, "Anatol")
one3 = Meeple(one, "3 ", "board[4][15]", route1, "H", 4, 15, board[4][15])#, "Albrecht")
one4 = Meeple(one, "4 ", "board[4][17]", route1, "H", 4, 17, board[4][17])#, "Abraham")

two1 = Meeple(two, "1 ", "board[16][15]", route2, "H", 16, 15, board[16][15])#, "Brigitte")
two2 = Meeple(two, "2 ", "board[16][17]", route2, "H", 16, 17, board[16][17])#, "Beate")
two3 = Meeple(two, "3 ", "board[18][15]", route2, "H", 18, 15, board[18][15])#, "Bernadette")
two4 = Meeple(two, "4 ", "board[18][17]", route2, "H", 18, 17, board[18][17])#, "Bonnie")

three1 = Meeple(three, "1 ", "board[16][3]", route3, "H", 16, 3, board[16][3])#, "Claire")
three2 = Meeple(three, "2 ", "board[16][5]", route3, "H", 16, 5, board[16][5])#, "Charlotte")
three3 = Meeple(three, "3 ", "board[18][3]", route3, "H", 18, 3, board[18][3])#, "Constanze")
three4 = Meeple(three, "4 ", "board[18][5]", route3, "H", 18, 5, board[18][5])#, "Cordula")

four1 = Meeple(four, "1 ", "board[2][3]", route4, "H", 2, 3, board[2][3])#, "Detlef")
four2 = Meeple(four, "2 ", "board[2][5]", route4, "H", 2, 5, board[2][5])#, "Dietmar")
four3 = Meeple(four, "3 ", "board[4][3]", route4, "H", 4, 3, board[4][3])#, "Dagobert")
four4 = Meeple(four, "4 ", "board[4][5]", route4, "H", 4, 5, board[4][5])#, "Donald")

########## changes ##########
# one1 = Meeple(one, "1 ", "board[2][15]", route1, 3, 2, 15, board[2][15])
# one2 = Meeple(one, "2 ", "board[2][17]", route1, 3, 2, 17, board[2][17])
# one3 = Meeple(one, "3 ", "board[4][15]", route1, 3, 4, 15, board[4][15])
# one4 = Meeple(one, "4 ", "board[4][17]", route1, 3, 4, 17, board[4][17])


########## teams ##########
team1.extend([one1, one2, one3, one4])
team2.extend([two1, two2, two3, two4])
team3.extend([three1, three2, three3, three4])
team4.extend([four1, four2, four3, four4])


