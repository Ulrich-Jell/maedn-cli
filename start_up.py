import sys
from termcolor import colored, cprint


########## Creation of the Board ##########
board = []

for y in range(21):
  board.append(0)

with open("brett.csv", "r") as file:
    l = 0
    for line in file:
        lineSplitted = line.strip().split(";")
        board[l] = lineSplitted
        l +=1

########## Creation of the Players ##########
class Player():
    def __init__(self, team, color, played_by, start, name):
        self.team = team
        self.color = color
        self.played_by = played_by
        self.start = start
        self.name = name

team1 = []
team2 = []
team3 = []
team4 = []
teams = [team1, team2, team3, team4]

one = Player(team1, "red", "human", colored(board[0][12], "grey", "on_red"), "one")
two = Player(team2, "green", "human", colored(board[12][20], "grey", "on_green"), "two")
three = Player(team3, "blue", "human", colored(board[20][8], "grey", "on_blue"), "three")
four = Player(team4, "yellow", "human", colored(board[8][0], "grey", "on_yellow"),"four")

global active_player
active_player = one

########## Coloring of the board ##########
board[2][15] = colored(board[2][15], one.color)
board[2][17] = colored(board[2][17], one.color)
board[4][15] = colored(board[4][15], one.color)
board[4][17] = colored(board[4][17], one.color)
start = "on_" + one.color
board[0][12] = colored(board[0][12], "grey", start)

board[16][15] = colored(board[16][15], two.color)
board[16][17] = colored(board[16][17], two.color)
board[18][15] = colored(board[18][15], two.color)
board[18][17] = colored(board[18][17], two.color)
start = "on_" + two.color
board[12][20] = colored(board[12][20], "grey", start)

board[16][3] = colored(board[16][3], three.color)
board[16][5] = colored(board[16][5], three.color)
board[18][3] = colored(board[18][3], three.color)
board[18][5] = colored(board[18][5], three.color)
start = "on_" + three.color
board[20][8] = colored(board[20][8], "grey", start)

board[2][3] = colored(board[2][3], four.color)
board[2][5] = colored(board[2][5], four.color)
board[4][3] = colored(board[4][3], four.color)
board[4][5] = colored(board[4][5], four.color)
start = "on_" + four.color
board[8][0] = colored(board[8][0], "grey", start)


def print_board():
  for e in range(len(board)):
      
      print("".join(board[e]))

########## Definition of the Routes ##########

from route import route


route1 = route

start2 = 10
route2 = {}

start3 = 20
route3 = {}

start4 = 30
route4 = {}

routes234 = {start2:route2, start3:route3, start4:route4}

for k,v in routes234.items():
    for e in range(0,(len(route)-k)):
        v[e] = route[k+e]
    h = 0
    for e in range(len(route)-k, len(route)):
        v[e] = route[h]
        h += 1

