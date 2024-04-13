import random
def name(size):
    size = 3 # input maybe later
def make_new_board():
    board = [[0 for i in range(size)]for i in range(size)] 
def bomb_plante(num_bombs):                                      
    bomb_planted = 0
    while bomb_planted < num_bombs: 
    coords = random.randint(0, size**2-1)  
    row = coords // size 
    col = coords % size
    if board[row][col] == 0:
        board[row][col] = 'X'
    bomb_planted+=1
def assign_values_to_board():
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'X':
                get_num_neighboring_bomb(r,c) 
i=0
def get_num_neighboring_bomb(row,col):
            while i<num_bombs:
                for r in range(row-1,row+2):
                    for c in range(col-1,col+2):
                        if(-1<r<3 and -1<c<3): 
                            if(board[r][c] != 'X'):
                                board[r][c]+=1
            i+=1
