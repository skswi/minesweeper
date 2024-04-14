import random
class game:
    def name(self,size,num_bombs):
        self.size = 3 # input maybe later
        self.num_bombs = 2 # input maybe later
    def make_new_board(self):
        board = [[0 for i in range(self.size)]for i in range(self.size)]
    def get_num_neighboring_bomb(self,row,col):            
            for i in range(2):
                for r in range(row-1,row+2):
                    for c in range(col-1,col+2):
                        if(-1<r<3 and -1<c<3): 
                            if(self.board[r][c] != 'X'):
                                self.board[r][c]+=1 
            return self.board
    def bomb_plante(self):                                      
        self.bomb_planted = 0
        while self.bomb_planted < self.num_bombs: 
            self.coords = random.randint(0, self.size**2-1)  
            self.row = self.coords // self.size 
            self.col = self.coords % self.size
            if self.board[self.row][self.col] == 0:
              self.board[self.row][self.col] = 'X'
              self.bomb_planted+=1
    def assign_values_to_board(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 'X':
                    self.get_num_neighboring_bomb(self,r,c)