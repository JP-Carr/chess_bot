from itertools import count, product
from numpy import array, concatenate, delete, unique
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
  
    def verifiy_moves(self, options):
     #   for i in range(len(options)):
       #     print(any(options[i]==self.position))
        
        deletion_indices=[i for i in range(len(options)) if all(options[i]<self.max_range )==False or all(options[i]>-1 )==False or all(options[i]==self.position)]#+[i for i in range(len(options)) if all(abs(options[i])>-1 )==False]
      #  print(deletion_indices)
        allowed_options=delete(options,deletion_indices,0)
     #   unique_allowed_options=unique([tuple(row) for row in allowed_options], axis=0)
        return allowed_options
    
class king(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
    def moves(self):
        options=array([[n,m]for n,m in product(range(-1,2),range(-1,2))])+self.position 
        allowed_options=self.verifiy_moves(options)
        return allowed_options
            
        
class queen(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position) 
    def moves(self):
        n_options=array([[n,0] for n in range(-self.max_range,self.max_range+1)])+self.position
        m_options=array([[0,m] for m in range(-self.max_range,self.max_range+1)])+self.position
        diag1_options=array([[n,n] for n in range(-self.max_range,self.max_range+1)])+self.position
        diag2_options=array([[-n,n] for n in range(-self.max_range,self.max_range+1)])+self.position
        
        options=concatenate((n_options,m_options,diag1_options, diag2_options))
        allowed_options=self.verifiy_moves(options)
        return allowed_options

class bishop(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
    def moves(self):
        diag1_options=array([[n,n] for n in range(-self.max_range,self.max_range+1)])+self.position
        diag2_options=array([[-n,n] for n in range(-self.max_range,self.max_range+1)])+self.position
        options=concatenate((diag1_options, diag2_options))
        allowed_options=self.verifiy_moves(options)
        return allowed_options
        
class knight(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position) 
    def moves(self):
        steps=array([[1,2], [2,1], [-1,2], [-2,1]])
        options1=steps+self.position
        options2=-steps+self.position
        options=concatenate((options1, options2))
       # print(options)
        allowed_options=self.verifiy_moves(options)
        return allowed_options
    
class rook(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
    def moves(self):
        n_options=array([[n,0] for n in range(-self.max_range,self.max_range+1)])+self.position
        m_options=array([[0,m] for m in range(-self.max_range,self.max_range+1)])+self.position
        options=concatenate((n_options, m_options))
        allowed_options=self.verifiy_moves(options)
        return allowed_options
        
class pawn(piece):
    def __init__(self, colour, position, living=True):
        super().__init__(colour, position)
        if colour=="black" or colour=="b":
            self.n_move_dir=-1
        elif colour=="white" or colour=="w":
            self.n_move_dir=1
    def moves(self):
        options=array([self.n_move_dir,0])+self.position
        allowed_options=self.verifiy_moves(options)
        return allowed_options

if __name__=="__main__":
  #  piece.r=5
    #x=king("white", [0,0])
    y=bishop("white", (5,5))
    print(y.moves())
    #y.moves()
