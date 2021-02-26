from itertools import count, product
from numpy import array
class piece:
    _id=count(1) #id 0 represents an empty space
    max_range=8 
    def __init__(self, colour, position, living=True):
        self.colour=colour
        self.living=living
        self.position=array(position)
        self._id = next(self._id)

        
    def __repr__(self):
        return "ID: #{} | {} {} | Position:{} | Living={}".format(self._id, self.colour, self.__class__.__name__, self.position, self.living)
        
class king(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
    def moves(self):
        options=array([array([x,y])+self.position for x,y in product(range(-1,2),range(-1,2))])
        return options
            
        
class queen(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position) 
    def moves(self):
        options=array([array([x,y])+self.position for x,y in product(range(-self.max_range,self.max_range+1),range(-self.max_range,self.max_range+1))])
        return options

class bishop(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
        
class knight(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)

class rook(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
        
class pawn(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)

if __name__=="__main__":
    piece.r=5
    #x=king("white", [0,0])
    y=queen("white", (0,0))
    print(y.moves())
