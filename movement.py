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
        st = compare_meeple_positions(self.x_pos, self.y_pos)
        gt = compare_meeple_positions((self.route[self.progress +dice][0]),(self.route[self.progress +dice][1]))
        #check if goal is empty
        if board[self.route[self.progress +dice][0]][self.route[self.progress +dice][1]] == "()":
            print("Zielfeld frei")
            for s in range (1, dice):
                self.go()
                print_board()
            self.go()
            print_board()
            end_turn(dice)

        elif st == gt:
            input("geht nicht")
            p = []
            for m in active_player.team:
                if m.progress != "H":
                    p.append(m)
                
                if len(p) == 1:
                    p[0].move(dice)
                else:
                    print("Meeple Auswählen")
                    end_turn(dice)
        else:
            print("Gegner Schlagen")
            end_turn(dice)

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
            dice = random.randint(1, 6)
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
            end_turn(d[0])

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
            dice = random.randint(4,4)
            print("4 is fixed")
            print(dice, "gewürfelt.")
            input("Beliebige Taste drücken, um fortzufahren")
            team[int(np.where(h)[0])].move(dice)
        else:
            print("Haus ist leer - freie wahl")
    
    else:
        print("start frei - freie Wahl")

def clear_screen():        
        os.system('cls' if os.name == 'nt' else 'clear')

def end_turn(dice):
    global active_player
    if dice == 6:
        turn(active_player)
    

    if active_player.name == "four":
        active_player = one
    else:    
        players = [one, two, three, four]
        active_player = players[(players.index(active_player)) + 1]

    print("Player ", active_player.name, ". It's your turn.")
    input("Press any key to continue")
    turn(active_player.team)

def compare_meeple_positions(a , b): #helper function to get the team of a meeple occupying a field
    mp = []
    for t in teams:
        mpt = []
        for m in t:
            mpt.append([m.x_pos, m.y_pos])
        mp.append(mpt)
    
    for i in range(4):
        if [a, b] in mp[i]:
            return i

        
        

#route = {0:[0,12], 1:[2,12], 2:[4,12], 3:[6,12], 4:[8,12], 5:[8,14], 6:[8,16]




