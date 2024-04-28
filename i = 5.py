import random
import re 
class game:
    def __init__(self):
        self.Length = int(input("What lenght whould you like?\n"))
        self.Width = int(input("What width whould you like?\n"))
        self.num_bombs = int(input("How many bombs would you like?\n"))
        self.diged = 0
        if self.Length >= 3 and self.Width  >= 3:
            self.make_new_board()
        else:
            print("Lenght and Width must be at least 2")
      

    def make_new_board(self):
        self.board = [[0 for i in range(self.Length)]for i in range(self.Width)] 
        self.bomb_plant()
    

    def bomb_plant(self): 
        if self.num_bombs >= self.Length * self.Width -1:  # -1 or even more 
            print("wrong input")
        else:
            self.bomb_planted = 0
            while self.bomb_planted  <  self.num_bombs: 
                self.coords = random.randint(0, self.Length * self.Width -1)           # 3 by 3 first squeres are open
                self.row = self.coords // self.Length 
                self.col = self.coords % self.Width
                if self.board[self.row][self.col] != 'x':
                    self.board[self.row][self.col] = 'x'
                    self.bomb_planted+=1
                    self.get_num_neighboring_bomb(self.row,self.col)
                    


    def get_num_neighboring_bomb(self,row,col):
        for r in range(self.row-1,self.row+2):
            for c in range(self.col-1,self.col+2):
                if(-1<r<self.Width and -1<c<self.Length):
                    if(self.board[r][c] == 0):
                        self.board[r][c]+=1
        if self.bomb_planted == self.num_bombs:
            print(*self.board,sep='\n')
            self.make_visboard()
    

    def input_coords(self):
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: ")) # 0, 3  
        self.row2, self.col2 = int(user_input[0])-1, int(user_input[-1])-1
        if self.dig == 0:
            self.dig(self.row2,self.col2)
        else:
            self.digstart(self.row2,self.col2)

    def make_visboard(self):
        self.visboard = [['?' for i in range(self.Length)]for i in range(self.Width)]
        print(*self.visboard,sep = '\n')
        self.input_coords()

    
    def dig(self,row2,col2):
        if(-1<self.row2<self.Width and -1<self.col2<self.Length):
            if self.board[row2][col2] == 'x':
                print("gameover")
                print(*self.board,sep='\n')
            else:
                if self.visboard[row2][col2] == self.board[row2][col2]:
                    print("nah uh , you cant say the same coords twice")     
                else:
                 self.visboard[self.row2][self.col2] = self.board[self.row2][self.col2]
                 self.diged = self.diged + 1
                 for r2 in range(self.row2-1,self.row2+2):
                   for c2 in range(self.col2-1,self.col2+2):
                       if(-1<r2<self.Width and -1<c2<self.Length):
                           if self.board[r2][c2] != 'x':
                             if self.visboard[r2][c2] != self.board[r2][c2]:
                                 self.visboard[r2][c2] = self.board[r2][c2]
                                 self.diged = self.diged + 1
                if self.diged == self.Length * self.Width - self.num_bombs:       
                    print(*self.board,sep = '\n')
                    print("good game!!!!!!")
                else:
                    print(*self.visboard,sep = '\n')
                    self.input_coords()

        else:
            print("wrong input , not in board")
            self.input_coords()



    def digstart(self,row2,col2):
        if(-1<self.row2<self.Width and -1<self.col2<self.Length):
            if self.board[row2][col2] == 'x':
                print("gameover")
                print(*self.board,sep='\n')
            else:
              if self.visboard[row2][col2] == self.board[row2][col2]:
                    print("nah uh , you cant say the same coords twice") 
                    self.input_coords()
              else:
                self.visboard[self.row2][self.col2] = self.board[self.row2][self.col2]
                self.diged = self.diged + 1
                for r2 in range(self.row2-1,self.row2+2):
                    for c2 in range(self.col2-1,self.col2+2):
                        if(-1<r2<self.Width and -1<c2<self.Length):
                           if self.board[r2][c2] != 'x' :
                             if self.visboard[r2][c2] != self.board[r2][c2]:
                                 self.visboard[r2][c2] = self.board[r2][c2]
                                 self.diged = self.diged + 1
                                 if self.board[r2][c2]==0:
                                  self.digstart0(r2,c2)
                                 else:
                                    self.visboard[r2][c2] = self.board[r2][c2]
                                    
        else:
          print("wrong input , not in board")
          self.input_coords()
    
        print(*self.visboard,sep='\n')
        self.input_coords()
    def digstart0(self,r2,c2):
       for r2 in range(r2-1,r2+2):
            for c2 in range(c2-1,c2+2):
              if(-1<r2<self.Width and -1<c2<self.Length):
                    if self.board[r2][c2] != 'x' :
                        if self.visboard[r2][c2] != self.board[r2][c2]:
                            self.visboard[r2][c2] = self.board[r2][c2]
                            self.diged = self.diged + 1
                            if self.board[r2][c2]==0:
                                self.digstart0(r2,c2)
       



game()


