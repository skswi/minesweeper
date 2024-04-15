import random
size = int(input("what size of the board whould you like?"))
board = [[0 for i in range(size)]for i in range(size)]
num_bombs = int(input("how much bombs whould you like?"))
if num_bombs >= size**2:
  print("wrong input")
else:
    bomb_planted = 0
    while bomb_planted < num_bombs: 
        coords = random.randint(0, size**2-1)  
        row = coords // size 
        col = coords % size
        if board[row][col] == 0:
            bomb_planted+=1
            board[row][col] = 'X'
            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    if(-1<r<size and -1<c<size):
                        if(board[r][c] != 'X'):
                            board[r][c]+=1
    print(*board,sep='\n')