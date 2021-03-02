#import time
#start=time.perf_counter()
#print(time.perf_counter()-start)
from random import randint
class bot():
    def __init__(self, colour):
        self.colour=colour
    
    def move(self, board, pcs_dict):
         my_pcs,opp_pcs={},{}
         
         for i in pcs_dict:
             if pcs_dict[i].colour==self.colour:
                 my_pcs[i]=pcs_dict[i]
             else:
                 opp_pcs[i]=pcs_dict[i]
                 
         piece=my_pcs[str(randint(1, 16))]
         print(piece)
         moves=piece.moves()
         kill_moves=[]
         for move in moves:
             path=board.path(piece.position, move)
             for space in path:
                 space_state=board.check_space(space)
                 if space_state!=0:
                     if pcs_dict[str(space_state)].colour==self.colour:
                         break
                     else:
                         kill_moves.append(move)
         print(kill_moves)