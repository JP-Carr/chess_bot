from numpy import array, zeros
class board:
    def __init__(self,x=8, y=None):
        self.x=x
        if y!=None:    
            self.y=y
        else:
            self.y=x
            
        self.grid=zeros((self.x,self.y), dtype=int)
        
    def __repr__(self):
        return str(self.grid)
    
    def check_space(self, position):
        """
        Checks if a sqaure on the board is occupied

        Parameters
        ----------
        position : tuple (x,y)
             coordinates of square to check.

        Returns
        -------
        bool
            Returns True if occupied.

        """
        if self.grid[position[0]][position[1]]==0:
            return False
        else:
            return True
        
x=board()
x.check_space((2,2))
print(x)