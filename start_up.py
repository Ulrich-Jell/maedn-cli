import sys
from termcolor import colored, cprint


########## Creation of the Players ##########
class Player():
    def __init__(self, team, color, played_by):#, route, goal):
        self.team = team
        self.color = color
        self.played_by = played_by

team1 = []
team2 = []
team3 = []
team4 = []

one = Player(team1, "magenta", "human")
two = Player(team2, "green", "human")
three = Player(team3, "blue", "human")
four = Player(team4, "yellow", "human")

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
board[8][0] = colored(board[8][0], four.color)


def print_board():
  for e in range(len(board)):
      
      print("".join(board[e]))

########## Definition of the Routes ##########
# route = []
# with open('Route.txt') as f:
#     lines = f.readlines()


# for line in lines:
#     route.append(line.strip())  

route = {
  0:[0,12],
  1:[2,12],
  2:[4,12],
  3:[6,12],
  4:[8,12],
  5:[8,14],
  6:[8,16],
  7:[8,18],
  8:[8,20],
  9:[10,20],
  10:[12,20],
  11:[12,18],
  12:[12,16],
  13:[12,14],
  14:[12,12],
  15:[14,12],
  16:[16,12],
  17:[18,12],
  18:[20,12],
  19:[20,10],
  20:[20,8],
  21:[18,8],
  22:[16,8],
  23:[14,8],
  24:[12,8],
  25:[12,6],
  26:[12,4],
  27:[12,2],
  28:[12,0],
  29:[10,0],
  30:[8,0],
  31:[8,2],
  32:[8,4],
  33:[8,6],
  34:[8,8],
  35:[6,8],
  36:[4,8],
  37:[2,8],
  38:[0,8],
  39:[0,10]
}


route1 = route

# start2 = 'board[12][20]'
# route2 = []

# start3 = 'board[20][8]'
# route3 = []

# start4 = 'board[8][0]'
# route4 = []

# routes234 = {start2:route2, start3:route3, start4:route4,}

# for k,v in routes234.items():
#     for e in route[route.index(k):]:
#         v.append(e)
#     for f in route[:route.index(k)]:
#         v.append(f)


#from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


#board[2][1] = (Style.RESET_ALL)

