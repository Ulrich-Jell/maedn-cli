import random
import os
import time
import numpy as np
from start_up import *
from termcolor import colored, cprint
from time import sleep


   
class Meeple():
    def __init__(self, player, no,  home, route, progress, x_pos, y_pos, old_pos):
        self.player = player
        self.no = no
        self.home = home
        self.route = route
        self.progress = progress
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.old_pos = old_pos

        

    def move(self, dice):
        print("move()")
        sleep(1)
        for s in range (1, dice):
            self.go()
            print_board()

        if board[self.route[self.progress +1][0]][self.route[self.progress +1][1]] == "()":
            self.go()
            print_board()
            if dice == 6:
                start_check(self.player.team)
            else:
                next_player()
        else:
            print("geht nicht")

    def go(self):
        print("go()")
        sleep(1)
        board[self.x_pos][self.y_pos] = self.old_pos
        sleep(1)
        self.progress += 1
        self.x_pos =self.route[self.progress][0] # route1[1][0] => 2
        self.y_pos =self.route[self.progress][1] # route1[1][1] => 12
        self.old_pos = board[self.x_pos][self.y_pos]
        board[self.x_pos][self.y_pos] = colored(self.no, self.player.color)
        clear_screen()

    def set_progress(self, progress):
        board[self.x_pos][self.y_pos] = colored("()", self.player.color)
        sleep(1)
        self.progress = progress
        self.x_pos =self.route[self.progress][0] # route1[1][0] => 2
        self.y_pos =self.route[self.progress][1] # route1[1][1] => 12
        self.old_pos = board[self.x_pos][self.y_pos]
        board[self.x_pos][self.y_pos] = colored(self.no, self.player.color)
       




def turn(team): #turn of the player
    
    print("dice_check()")
    sleep(1)
    t = []
    for m in team: #check if there are meeples en route
        if m.progress != "H":
            t.append(True)
        else:
            t.append(False)   
    
    if True in t: #at least one meeple en route
        start_check(team) # if necessary, move meeple from start.
        print("start_check() passed")
        if t.count(True) == 1:      
            dice = random.randint(1, 6)
            if dice == 6:
                print("sechs gewürfelt - Figur raus ziehen, wenn möglich.")
                leave_home(team)
            else:
                print("Player " + active_player.name + " rolls a " + str(dice))
                input("Press any key to continue")
                team[t.index(True)].move(dice)
        else:
            dice = random.randint(6, 6)
            if dice == 6:
                input("sechs gewürfelt - Figur raus ziehen, wenn möglich.")
                leave_home(team)
            else:
                print("Player " + active_player.name + " rolls a " + str(dice))
                c = input("Please choose a Meeple")
                if t[int(c) - 1]:
                    team[int(c) -1].move(dice)

    else: #no meeples en route => roll the dice three times
        d = []
        d.append(random.randint(1, 6))
        d.append(random.randint(1, 6))
        d.append(random.randint(6, 6))
        print("Player " + active_player.name + " rolls a "+ str(d[0]), ", a " + str(d[1]) + " and a " + str(d[2]))
        
        if 6 in d:
            input("Press any key to move one meeple out of the start")
            leave_home(team)
            
            
        else:
            print("Unfortunately, you did not roll a 6.")
            input("Press any key to let the next player continue.")
            clear_screen()
            print_board()
            next_player()

def leave_home(team):
    for m in team:
        if m.progress =="H":
            board[m.x_pos][m.y_pos] = colored("()", m.player.color)
            m.progress = 0
            m.x_pos =m.route[0][0]
            m.y_pos =m.route[0][1]
            board[m.x_pos][m.y_pos] = colored(m.no, "grey", "on_" + str(m.player.color))
            m.old_pos = colored("()", "grey", "on_"+str(m.player.color))
            clear_screen()
            print_board()
            r = random.randint(1,5)
            print("Player " + active_player.name + " rolls a " + str(r))
            input("Press any key to continue")
            m.move(r)
            break

def start_check(team): #Is there a Meeple on "start" and another in "home"?
    print("start_check()")
    sleep(1)
    t = []
    for m in team:
        if m.progress == "H":
            t.append(True)
        else:
            t.append(False)

    if True in t:
        h = []
        for m in team:
            if m.progress == 0:
                h.append(True)
            else:
                h.append(False)
        
        if True in h:
            print("start räumen - zugzwang")
            print(h)
            print(np.where(h)[0])
            dice = random.randint(1,6)
            input(dice, " gewürfelt.")
            team[int(np.where(h)[0])].move(dice)
        else:
            print("Haus ist leer - freie wahl")
    
    else:
        print("start frei - freie Wahl")

def clear_screen():        
        os.system('cls' if os.name == 'nt' else 'clear')

def next_player():
    global active_player
    if active_player.name == "four":
        active_player = one
        
   
    else:    
        players = [one, two, three, four]
        active_player = players[(players.index(active_player)) + 1]

    print("Player ", active_player.name, ". It's your turn.")
    input("Press any key to continue")
    turn(active_player.team)
        
        

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
one1.set_progress(4)
one4.set_progress(0)


########## teams ##########
team1.extend([one1, one2, one3, one4])
team2.extend([two1, two2, two3, two4])
team3.extend([three1, three2, three3, three4])
team4.extend([four1, four2, four3, four4])


