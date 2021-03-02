from numpy import array, zeros, arange, rot90
import numpy as np

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
        int
            Returns the value of the position.

        """

        return self.grid[position[0]][position[1]]

        
    def move_piece(self, old_position, new_position):
     #   print(new_position)
        if self.check_space(new_position)==True:
            kill_id=self.grid[new_position[0]][new_position[1]]
        else:
            kill_id=None
            
        self.grid[new_position[0]][new_position[1]]=self.grid[old_position[0]][old_position[1]]
        self.grid[old_position[0]][old_position[1]]=0
        return kill_id
    
    def setup(self, position,_id):
        self.grid[position[0]][position[1]]=_id
        
    def path(self, start, finish):
        
        if start[0]<finish[0]:
            n_spaces=arange(start[0],finish[0], dtype=int)
        else:
            n_spaces=arange(start[0],finish[0], -1, dtype=int)
  
        if start[1]<finish[1]:
            m_spaces=arange(start[1],finish[1], dtype=int)
        else:
            m_spaces=arange(start[1],finish[1], -1, dtype=int)
     
            
        #n_spaces=arange(min(start[0],finish[0]),max(start[0],finish[0]), dtype=int)
        #m_spaces=arange(min(start[1],finish[1]),max(start[1],finish[1]), dtype=int)
  #      print(n_spaces)
   #     print(m_spaces)
    #    print("\n")
    
        if len(n_spaces)==0:
            n_spaces=np.ones((1,max(len(n_spaces),len(m_spaces))), dtype=int)*start[0]
        elif len(m_spaces)==0:
            m_spaces=np.ones((1,max(len(n_spaces),len(m_spaces))), dtype=int)*start[1]
        spaces=zeros((2,max(len(n_spaces),len(m_spaces))), dtype=int)    

        spaces[0,:]=n_spaces
        spaces[1,:]=m_spaces


        path=rot90(spaces)

        has_start,has_finish=False,False
        for i in path:
            if all(i==start):
                has_start=True
            if all(i==finish):
                has_finish=True
        if has_start==True:
            index=np.where((path == start).all(axis=1))[0][0]
            path=np.delete(path,index,0)
        if has_finish==False:
            path=np.vstack((finish,path))
        path=rot90(path, 2)
        return path
    
if __name__=="__main__":       
    x=board()
    x.grid[0][0]=5
    x.grid[2][2]=3
    print(x.path(array([0,0]), array([5,5])))
    #print(x.path(array([5,5]), array([0,0])))

