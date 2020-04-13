import pygame,sys,random
SIZE = 15  # size of single cell
BLOCK_HEIGHT =50 # number of cell in height
BLOCK_WIDTH = 100  # number of cell in width
SCREEN_WIDTH = SIZE * (BLOCK_WIDTH)  # width of window
SCREEN_HEIGHT = SIZE * BLOCK_HEIGHT  # height of window
BG_COLOR = (40, 40, 60)  # background color
LINE_COLOR=(255,0,0)
CELL_COLOR=(255,255,255)    
LINE_WIDTH=1
BLACK = (0, 0, 0)

def update_life(board):
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
    rows = len(board)
    cols = len(board[0])

    def check_alive(board,x,y):
        count=0
        for position in neighbors:
            check_x=position[0]+x
            check_y=position[1]+y
            if check_x>=0 and check_x<rows and check_y>=0 and check_y<cols:
                if board[check_x][check_y]==1:
                    count+=1
        return count

    copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

    for x in range(rows):
        for y in range(cols):
            alive_cell=check_alive(copy_board,x,y)
            if copy_board[x][y]==1:
                if alive_cell<2:
                    board[x][y]=0
                elif alive_cell==2 or alive_cell==3:
                    board[x][y]=1
                elif alive_cell>3:
                    board[x][y]=0
            elif copy_board[x][y]==0:
                if alive_cell==3:
                    board[x][y]=1

def update_disp(screen,board,size,width,height,line_width):


    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]==1:
                pygame.draw.rect(screen,CELL_COLOR,(col*size,row*size,size-line_width,size-line_width))
            else:
                pygame.draw.rect(screen,BG_COLOR,(col*size,row*size,size-line_width,size-line_width))

    # for row in range(1,height):
    #     pygame.draw.line(screen,LINE_COLOR,(0,size*row), (width,size*row),line_width)
    # for col in range(1,width):
    #     pygame.draw.line(screen,LINE_COLOR,(size*col,0),(size*col,height),line_width)

def main():
    board=[]
    for i in range(BLOCK_HEIGHT):
        board.append([])
        for j in range(BLOCK_WIDTH):
            board[i].append(random.randint(0,1))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Game Of Life')
    screen.fill(BG_COLOR)
    clock = pygame.time.Clock() 
    time_passed = clock.tick()  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        update_disp(screen,board,SIZE,SCREEN_WIDTH,SCREEN_HEIGHT,LINE_WIDTH)
        update_life(board)
        pygame.display.update()
        time_passed = clock.tick(1)
        


if __name__ == '__main__':

    main()