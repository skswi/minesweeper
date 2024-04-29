import random
import re 
class game:
    def __init__(self):
        self.Length = int(input("What lenght whould you like?\n"))
        self.Width = int(input("What width whould you like?\n"))
        self.num_bombs = int(input("How many bombs would you like?\n"))
        self.dug = set()
        self.visboard = [['?' for i in range(self.Length)]for i in range(self.Width)]
        if self.Length >= 3 and self.Width  >= 3:
            self.make_new_board()
        else:
            print("Lenght and Width must be at least 2")
      

    def make_new_board(self):
        self.board = [[0 for q in range(self.Length)]for i in range(self.Width)] 
        self.bomb_plant()
    

    def bomb_plant(self): 
        if self.num_bombs >= self.Length * self.Width -1:  # -1 or even more 
            print("wrong input")
        else:
            self.bomb_planted = 0
            while self.bomb_planted  <  self.num_bombs: 
                self.coords = random.randint(0, self.Length * self.Width -1)       
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
            print(*self.visboard,sep='\n')
            self.input_coords()



    

    def input_coords(self):
        while len(self.dug) < self.Length * self.Width - self.num_bombs:
         if len(self.dug) == self.Length * self.Width - self.num_bombs:
          print("YOU WONNNN ")
          print(*self.visboard,sep = '\n')
         user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: ")) # 0, 3  
         self.row2, self.col2 = int(user_input[0])-1, int(user_input[-1])-1
         if self.visboard[self.row2][self.row2] != self.board[self.row2][self.col2]:    
          if(-1<self.row2<self.Width and -1<self.col2<self.Length):
            self.dig(self.row2, self.col2)
            print(*self.visboard,sep = '\n')
 
          
          else:
            print("wrong coords")
            self.input_coords

         




    def dig(self,row,col):
        self.dug.add((row, col))
        self.visboard[row][col] = self.board[row][col]
        
        if self.board[row][col] == 'x':
            print("YOU LOST :( !! ")
            print(*self.board,sep = '\n')
            return False
            
        elif self.board[row][col] == 0:
         for r in range(row-1,row+2):
            for c in range(col-1,col+2):
              if(-1<r<self.Width and -1<c<self.Length):
                if (r, c) in self.dug or self.board[r][c] == 'x':
                    continue 
                self.visboard[r][c] = self.board[r][c]
                self.dig(r, c)
game()





