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
        
    def move_piece(self, old_position, new_position):
        if self.check_space(new_position)==True:
            kill_id=self.grid[new_position[0]][new_position[1]]
        else:
            kill_id=None
            
        self.grid[new_position[0]][new_position[1]]=self.grid[old_position[0]][old_position[1]]
        self.grid[old_position[0]][old_position[1]]=0
        return kill_id
if __name__=="__main__":       
    x=board()
    x.grid[0][0]=5
    x.grid[1][1]=3
    print(x)
    print(x.move_piece((0,0), (1,1)))
    print(x)
