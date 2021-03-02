import pieces as pcs
from board import board
from bot import bot
"""
-------------------------
White      |  Black
1.  king   |  17. king
2.  rook   |  18. rook
3.  rook   |  19. rook
4.  knight |  20. knight
5.  knight |  21. knight
6.  bishop |  22. bishop
7.  bishop |  23. bishop
8.  queen  |  24. queen
9.  pawn   |  25. pawn
10. pawn   |  26. pawn
11. pawn   |  27. pawn
12. pawn   |  28. pawn
13. pawn   |  29. pawn
14. pawn   |  30. pawn
15. pawn   |  31. pawn
16. pawn   |  32. pawn
-------------------------
"""
table=board()
player1=bot("white")

white_king=pcs.king("white", [0,4])
back_white=[pcs.rook("white", [0,0]), pcs.rook("white", [0,7])]+[pcs.knight("white", [0,1]), pcs.knight("white", [0,6])]+[pcs.bishop("white", [0,2]), pcs.bishop("white", [0,5])]+[pcs.queen("white", [0,3])]
white_pawns=[pcs.pawn("white", [1,y]) for y in range(8)]
white=[white_king]+back_white+white_pawns

black_king=pcs.king("black", [7,4])
back_black=[pcs.rook("black", [7,0]), pcs.rook("black", [7,7])]+[pcs.knight("black", [7,1]), pcs.knight("black", [7,6])]+[pcs.bishop("black", [7,2]), pcs.bishop("black", [7,5])]+[pcs.queen("black", [7,3])]
black_pawns=[pcs.pawn("black", [6,y]) for y in range(8)]
black=[black_king]+back_black+black_pawns

pcs_dict={str(i._id):i for i in white+black}

for i in white:
    table.setup(i.position, i._id)
for i in black:
    table.setup(i.position, i._id)
#print(table.grid)

#------------------------------------------------------------------------------
turn=0
while white_king.living and black_king.living:
    turn+=1
    player1.move(table, pcs_dict)
    
    break
if white_king.living:
    print("White wins - {} turns".format(turn))
else:
    print("Black wins - {} turns".format(turn))