import random 
import pygame
import time 
import os
TILESIZE = 32
tile_numbers = []
for i in range(0, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join(f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("TileFlag.png")), (TILESIZE, TILESIZE))


pygame.font.init()
Length = 24
Width = 20
length_window = TILESIZE * Length
width_window = TILESIZE *  Width
num_bombs = 25
dug = set() 
blue = (0, 0, 255)
visboard = [['?' for i in range(Length)]for i in range(Width)]
cover_field = [[0 for i in range(Length)]for i in range(Width)]
board = [[0 for q in range(Length)]for i in range(Width)] 

NUM_FONT = pygame.font.SysFont('Comic Sans MS', 22)
red = (255, 0, 0)
pygame.init()
pygame.display.set_caption(" Minesweeper ") 
window = pygame.display.set_mode((length_window,width_window))
window2 = pygame.display.set_mode((length_window,width_window))
pygame.display.flip()
white = [255, 255, 255]
black = (0,0,0)
green = (0, 255, 0)
color = (140,140,140)


class mine:

    def __init__(self):
        self.opend= 0
        self.bomb_planted = 0
        while self.bomb_planted  <  num_bombs: 
            col = random.randint(0 , Length-1)   
            row = random.randint(0, Width-1)
            if board[row][col] != -1:
                board[row][col] = -1
                self.bomb_planted+=1
                self.get_num_neighboring_bomb(row,col)    


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
        if cover_field[row][col] != 2:
            dug.add((row, col))
            if board[row][col] == -1:
                print("YOU LOST :( !! ")
                for row2 in range(Width):
                    for col2 in range(Length):
                        cover_field[row2][col2] = 1
                self.draw()
                return False
            


            elif board[row][col] == 0:
             if cover_field[row][col] != 2:
                for r in range(row-1,row+2):
                    for c in range(col-1,col+2):
                        if(-1<r<Width and -1<c<Length):
                            if (r, c) in dug or board[r][c] == -1 or cover_field[row][col] == 2:
                                continue 
                            self.opend = self.opend + 1
                            cover_field[r][c] = 1
                            self.dig(r, c)
    


   
    def Window(self):
        self.draw()
        q = 1
        while self.opend != Width * Length - num_bombs:   
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    quit()                                  
                if q == 1:
                    self.start_time = time.time()
                    q+=1
                if pygame.mouse.get_pressed()[0]:  
                    row,col = self.get_coords(pygame.mouse.get_pos())
                    if cover_field[row][col] != 2 and cover_field[row][col] == 0:
                        cover_field[row][col] = 1
                        self.opend = self.opend + 1
                        dig2 = self.dig(row,col)
                        if dig2 == False:
                            self.time()
                            pygame.quit()
                            quit()
                if pygame.mouse.get_pressed()[2]: 
                    row,col = self.get_coords(pygame.mouse.get_pos())
                    if cover_field[row][col] == 0:
                        cover_field[row][col] = 2
                    elif cover_field[row][col] == 2:
                        cover_field[row][col] = 0
                        
            self.draw()


        print("GOOD GAME! YOU WON!")
        self.time()



    def get_coords(self,mouse_pos):  # *
        mx,my = mouse_pos
        row = my//TILESIZE
        col = mx//TILESIZE
        return row,col 
    
    def draw(self):
        for i,row2 in enumerate(board):
            y2 = TILESIZE * i
            for j, value in enumerate(row2):
                x2 = TILESIZE * j
                if cover_field[i][j]==0:
                    pygame.draw.rect(window2 , white , (x2,y2,TILESIZE,TILESIZE))
                    pygame.draw.rect(window2 , black , (x2,y2,TILESIZE,TILESIZE),2)

                elif cover_field[i][j] == 1:
                    pygame.draw.rect(window2 , color , (x2,y2,TILESIZE,TILESIZE))
                    pygame.draw.rect(window2 , black , (x2,y2,TILESIZE,TILESIZE),2)
                    if value == 0:
                        text = tile_numbers[0]
                    if value == 1:
                        text = tile_numbers[1]
                    if value == 2:
                        text = tile_numbers[2]
                    if value == 3:
                        text = tile_numbers[3]
                    if value == 4:
                        text = tile_numbers[4]
                    if value == 5:
                        text = tile_numbers[5]
                    if value == 6:
                        text = tile_numbers[6]
                    if value == 7:
                        text = tile_numbers[7]
                    if value == 8:
                        text = tile_numbers[8]
                    
            
                    center_x = x2 + TILESIZE / 2 -15
                    center_y = y2 + TILESIZE / 2 -15
                    window.blit(text, (center_x,center_y))
                else:
                    pygame.draw.rect(window2 , red , (x2,y2,TILESIZE,TILESIZE))
                    pygame.draw.rect(window2 , black , (x2,y2,TILESIZE,TILESIZE),2)





                  
        pygame.display.flip()


    def time(self):                                              
         current_time = time.time()
         elapsed_time = int(current_time - self.start_time)
         minutes = elapsed_time // 60
         seconds = elapsed_time % 60
         formatted_time = f"{minutes:02d}:{seconds:02d}"
         print(formatted_time)














mine()
    
