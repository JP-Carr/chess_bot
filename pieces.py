from itertools import count
class piece:
    _id=count(1) #id 0 represents an empty space
        
    def __init__(self, colour, position, living=True):
        self.colour=colour
        self.living=living
        self.position=position
        self._id = next(self._id)
        
    def __repr__(self):
        return "ID: #{} | {} {} | Position:{} | Living={}".format(self._id, self.colour, self.__class__.__name__, self.position, self.living)
        
class king(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
        
class queen(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)

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

#x=king("white", (0,0))
#y=king("white", (0,0))
#print(y)