import random
class game:
    def __init__(self,size,num_bombs):
        self.size = int(input("what size whould you like?\n"))
        self.num_bombs = int(input("how many bombs would you like?\n"))
        self.make_new_board()
      

    def make_new_board(self):
        self.board = [[0 for i in range(self.size)]for i in range(self.size)] 
        self.bomb_plant()
    

    def bomb_plant(self):
        print("the best num of bombs is 1/4 - 1/3 of size**2)
        if self.num_bombs >= self.size**2:
            print("wrong input")
        else:
            self.bomb_planted = 0
            while self.bomb_planted  <  self.num_bombs: 
                self.coords = random.randint(0, self.size**2-1)  
                self.row = self.coords // self.size 
                self.col = self.coords % self.size
                if self.board[self.row][self.col] == 0:
                    self.board[self.row][self.col] = 'x'
                    self.bomb_planted+=1
                    self.get_num_neighboring_bomb(self.row , self.col)
                    


    def get_num_neighboring_bomb(self,row,col):
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if(-1<r<self.size and -1<c<self.size):
                    if(self.board[r][c] != 'x'):
                        self.board[r][c]+=1
        if self.bomb_planted == self.num_bombs:
            print(*self.board,sep='\n')

game(3,2)
 
