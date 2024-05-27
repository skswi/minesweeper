import random 
import pygame
import time 
from time import sleep
import os




TILESIZE = 32





tile_numbers = []
for i in range(0, 6):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join(f"Tile{i}.jpeg")), (TILESIZE, TILESIZE)))
for i in range(7,9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join(f"Tile{i}.png")), (TILESIZE, TILESIZE)))


playagain =  pygame.transform.scale(pygame.image.load(os.path.join("playagain.jpg")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("TileFlag.png")), (TILESIZE, TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("TileMine.png")), (TILESIZE, TILESIZE))
won = pygame.transform.scale(pygame.image.load(os.path.join("won.jpg")), (TILESIZE, TILESIZE))


pygame.font.init()
Length = 24
Width = 20
length_window = TILESIZE * Length
width_window = TILESIZE *  Width
num_bombs = 50
blue = (0, 0, 255)


FONT = pygame.font.SysFont('Comic Sans MS', 22)
red = (255, 0, 0)
pygame.init()
pygame.display.set_caption("Minesweeper ") 
window = pygame.display.set_mode((length_window,width_window))
pygame.display.flip()
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
color = (140,140,140)


class mine:

    def __init__(self):
        self.i = 0
        self.opend = 0
        self.board = [[0 for q in range(Length)]for i in range(Width)] 
        self.cover_field = [[0 for i in range(Length)]for i in range(Width)]
        self.bomb_planted = 0 
        while self.bomb_planted  <  num_bombs: 
            col = random.randint(0 , Length-1)   
            row = random.randint(0, Width-1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                self.bomb_planted+=1
                self.get_num_neighboring_bomb(row,col)    


    def get_num_neighboring_bomb(self,row,col):
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if(-1<r<Width and -1<c<Length):
                     if(self.board[r][c] != -1):
                        self.board[r][c]+=1
        if self.bomb_planted == num_bombs:
            self.Window()




    def dig(self,row,col):
        if self.cover_field[row][col] != 2:
            if self.board[row][col] == -1:
                for row2 in range(Width):
                    for col2 in range(Length):
                        self.cover_field[row2][col2] = 1
                self.draw()
                sleep(1)
                self.winorlose = "lose"
                self.new_window()

                
            


            elif self.board[row][col] == 0:
             if self.cover_field[row][col] != 2:
                for r in range(row-1,row+2):
                    for c in range(col-1,col+2):
                        if(-1<r<Width and -1<c<Length):
                            if self.cover_field[r][c] == 1 or self.board[r][c] == -1 or self.cover_field[r][c] == 2:
                                continue 
                            self.opend = self.opend + 1
                            self.cover_field[r][c] = 1
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
                    if self.cover_field[row][col] != 2 and self.cover_field[row][col] == 0:
                        self.cover_field[row][col] = 1
                        self.opend = self.opend + 1
                        dig2 = self.dig(row,col)
                        if dig2 == False:
                            self.time()
                            pygame.quit()
                            quit()
                if pygame.mouse.get_pressed()[2]: 
                    row,col = self.get_coords(pygame.mouse.get_pos())
                    if self.cover_field[row][col] == 0:
                        self.cover_field[row][col] = 2
                    elif self.cover_field[row][col] == 2:
                        self.cover_field[row][col] = 0
                        
            self.draw()
        self.winorlose = "won"
        self.new_window()













    def new_window(self):
        scale_factor=8
        screen_width, screen_height = window.get_size()
        blurred_surface = pygame.transform.smoothscale(window, (screen_width // scale_factor, screen_height // scale_factor))
        blurred_surface = pygame.transform.smoothscale(blurred_surface, (screen_width, screen_height))
        window.blit(blurred_surface, (0, 0))
        small_font = pygame.font.Font(None, 40)
        time = self.time() 
        large_font = pygame.font.Font(None, 50)
        verylarge_font = pygame.font.Font(None, 75)
        text = small_font.render(time,False,black)
        center_x = width_window /2 +65
        center_y = length_window /2 -50
        window.blit(text, (center_x,center_y))
        if self.winorlose == "won":
            text = verylarge_font.render("You won",False,green)
            center_x = length_window /2 -120
            center_y = width_window /2 -180
            window.blit(text, (center_x,center_y))
        else:
            text = verylarge_font.render("You lost",False,red)
            center_x = length_window /2 -120
            center_y = width_window /2 -160
            window.blit(text, (center_x,center_y))
        text = small_font.render("time took:",False,black)
        center_x = width_window /2 -70
        center_y = length_window /2 -50
        window.blit(text, (center_x,center_y))
        
        while self.i != 5:
         large_font = pygame.font.Font(None, 50)
         text= large_font.render("click if you want to play again", True, black)
         button_y = length_window /2 -85
         button_x = width_window /2 -180
         button_width = text.get_width() + 20
         button_height = text.get_height() + 10
         window.blit(text, (button_x,button_y))
         pygame.display.flip()
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
             self.i=5
            if event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = pygame.mouse.get_pos()
             if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                sleep(0.5)
                self.__init__()
        pygame.quit()
        quit()
         



    def get_coords(self,mouse_pos):  
        mx,my = mouse_pos
        row = my//TILESIZE
        col = mx//TILESIZE
        return row,col 
    
    def draw(self):
        for i,row2 in enumerate(self.board):
            y2 = TILESIZE * i
            for j, value in enumerate(row2):
                x2 = TILESIZE * j
                if self.cover_field[i][j]==0:
                    pygame.draw.rect(window , white , (x2,y2,TILESIZE,TILESIZE))
                    pygame.draw.rect(window , black , (x2,y2,TILESIZE,TILESIZE),2)

                elif self.cover_field[i][j] == 1:
                    pygame.draw.rect(window , color , (x2,y2,TILESIZE,TILESIZE))
                    pygame.draw.rect(window , black , (x2,y2,TILESIZE,TILESIZE),2)
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
                    if value == -1:
                        text = tile_mine
                    
                    
            
                    center_x = x2 + TILESIZE / 2 -15
                    center_y = y2 + TILESIZE / 2 -15
                    window.blit(text, (center_x,center_y))
                else:
                    pygame.draw.rect(window , red , (x2,y2,TILESIZE,TILESIZE))
                    pygame.draw.rect(window , black , (x2,y2,TILESIZE,TILESIZE),2)
                if self.cover_field[i][j] == 2:
                    text = tile_flag
                    center_x = x2 + TILESIZE / 2 -15
                    center_y = y2 + TILESIZE / 2 -15
                    window.blit(text, (center_x,center_y))






                  
        pygame.display.flip()


    def time(self):                                              
         current_time = time.time()
         elapsed_time = int(current_time - self.start_time)
         minutes = elapsed_time // 60
         seconds = elapsed_time % 60
         formatted_time = f"{minutes:02d}:{seconds:02d}"
         return formatted_time







mine()
        
