import random
def name(size):
    size = 3 # input maybe later
def make_new_board():
    board = [['None' for i in range(size)]for i in range(size)]  # [ none , none ,none]
def bomb_plante(num_bombs):                                      # [ none , none ,X]
                                                                 # [ none , none ,none]
    bomb_planted = 0
    while bomb_planted < num_bombs: 
    coords = random.randint(0, size**2-1)  
    row = coords // size 
    col = coords % size
    if board[row][col] == 'None':
        board[row][col] = 'X'
    bomb_planted+=1
def assign_values_to_board():
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'X':
                get_num_neighboring_bomb(r,c) 
def get_num_neighboring_bomb(row,col):
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)
              # for r in range((0, row-1), (size-1, row+1)+1):
            #for c in range((0, col-1), (size-1, col+1)+1):
