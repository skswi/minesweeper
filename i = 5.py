import random 
import pygame

pygame.font.init()
Length = 15
Width = 15
length_window = 600
width_window = 600
num_bombs = 15
dug = set() 
blue = (0, 0, 255)
visboard = [['?' for i in range(Length)]for i in range(Width)]
cover_field = [[0 for i in range(Length)]for i in range(Width)]
board = [[0 for q in range(Length)]for i in range(Width)] 
size = 40
NUM_FONT = pygame.font.SysFont('Ariel', 20)
red = (255, 0, 0)
pygame.init()
pygame.display.set_caption(" Minesweeper ") 
window = pygame.display.set_mode((length_window,width_window))
pygame.display.flip()
white = [255, 255, 255]
black = (0,0,0)
green = (0, 255, 0)
color = (140,140,140)
class mine:

    def __init__(self):
        self.bomb_planted = 0
        while self.bomb_planted  <  num_bombs: 
            self.coords = random.randint(0, Length * Width -1)       
            self.row = self.coords // Length 
            self.col = self.coords % Width
            if board[self.row][self.col] != -1:
                board[self.row][self.col] = -1
                self.bomb_planted+=1
                self.get_num_neighboring_bomb(self.row,self.col)    


    def get_num_neighboring_bomb(self,row,col):
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if(-1<r<Width and -1<c<Length):
                    if visboard[r][c] != board[r][c]:
                     if(board[r][c] != -1):
                        board[r][c]+=1
        if self.bomb_planted == num_bombs:
            self.Window()




    def dig(self,row,col):
        dug.add((row, col))
        visboard[row][col] = board[row][col]
        if board[row][col] == -1:
            print("YOU LOST :( !! ")
            print(*board,sep = '\n')
            return False
            
        elif board[row][col] == 0:
         for r in range(row-1,row+2):
            for c in range(col-1,col+2):
              if(-1<r<Width and -1<c<Length):
                if (r, c) in dug or board[r][c] == -1:
                    continue 
                visboard[r][c] = board[r][c]
                self.dig(r, c)


   
    def Window(self):
        running = True
        while running:  
            for event in pygame.event.get():                                                 
                if event.type == pygame.QUIT:    
                    running = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row,col = self.get_coords(pygame.mouse.get_pos())
                    if row >= Length and col>= Width:
                        continue
                    cover_field[row][col] = 1
            self.draw()
        pygame.quit()


    def get_coords(self,mouse_pos):
        mx,my = mouse_pos
        row = int(my//size)
        col = int(mx//size)
        return row,col 
    
    def draw(self):
        for i,row2 in enumerate(board):
            y2 = size * i
            for j, value in enumerate(row2):
                x2 = size * j
                if cover_field[i][j]==0:
                    pygame.draw.rect(window , white , (x2,y2,size,size))
                    pygame.draw.rect(window , black , (x2,y2,size,size),2)
                else:
                    pygame.draw.rect(window , color , (x2,y2,size,size))
                    pygame.draw.rect(window , black , (x2,y2,size,size),2)
                    if value == -1:
                        text = NUM_FONT.render(str(value), True , green)
                        center_x = x2 + size // 2
                        center_y = y2 + size // 2
                        window.blit(text, (center_x,center_y))
                        # reveal board 

                    elif value >0:
                        text = NUM_FONT.render(str(value), True , black)
                        center_x = x2 + size // 2
                        center_y = y2 + size // 2
                        window.blit(text, (center_x,center_y))
                    else:
                        text = NUM_FONT.render(str(value), True , blue)
                        center_x = x2 + size // 2
                        center_y = y2 + size // 2
                        window.blit(text, (center_x,center_y))
                        #self.open_zero() + pygame.quit()

                    
        pygame.display.flip()
    

    #def open_zero(self):
mine()



