from movement import *

#player, no,  home, route, progress, x_pos, y_pos, old_pos

one1 = Meeple(one, "1 ", "board[2][15]", route1, "H", 2, 15, board[2][15])
one2 = Meeple(one, "2 ", "board[2][17]", route1, "H", 2, 17, board[2][17])
one3 = Meeple(one, "3 ", "board[4][15]", route1, "H", 4, 15, board[4][15])
one4 = Meeple(one, "4 ", "board[4][17]", route1, "H", 4, 17, board[4][17])

two1 = Meeple(two, "1 ", "board[16][15]", route2, "H", 16, 15, board[16][15])
two2 = Meeple(two, "2 ", "board[16][17]", route2, "H", 16, 17, board[16][17])
two3 = Meeple(two, "3 ", "board[18][15]", route2, "H", 18, 15, board[18][15])
two4 = Meeple(two, "4 ", "board[18][17]", route2, "H", 18, 17, board[18][17])

three1 = Meeple(three, "1 ", "board[16][3]", route3, "H", 16, 3, board[16][3])
three2 = Meeple(three, "2 ", "board[16][5]", route3, "H", 16, 5, board[16][5])
three3 = Meeple(three, "3 ", "board[18][3]", route3, "H", 18, 3, board[18][3])
three4 = Meeple(three, "4 ", "board[18][5]", route3, "H", 18, 5, board[18][5])

four1 = Meeple(four, "1 ", "board[2][3]", route4, "H", 2, 3, board[2][3])
four2 = Meeple(four, "2 ", "board[2][5]", route4, "H", 2, 5, board[2][5])
four3 = Meeple(four, "3 ", "board[4][3]", route4, "H", 4, 3, board[4][3])
four4 = Meeple(four, "4 ", "board[4][5]", route4, "H", 4, 5, board[4][5])

########## changes ##########
one1.set_progress(5)
one4.set_progress(0)
four3.set_progress(14)


########## teams ##########
team1.extend([one1, one2, one3, one4])
team2.extend([two1, two2, two3, two4])
team3.extend([three1, three2, three3, three4])
team4.extend([four1, four2, four3, four4])







    