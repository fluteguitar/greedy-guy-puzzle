import sys
file_inp = "board.txt"
dir_adjustment = [(0, -1), (1, 0), (0,1), (-1, 0)]
dir_name = 'Lelf Down Right Up'.split()

def inside_the_board(x, y, m, n):
    return (0<=x<m) and (0<=y<n)
    
def available(board, cur_position, direction):
    """
    Check if it is possible to enter direction
    """
    x,y = cur_position
    dx, dy = dir_adjustment[direction]
    x = x + dx
    y = y + dy
    
    return (inside_the_board(x,y,len(board), len(board[0])) and board[x][y] == 0)

    
def check_finish_tour(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True

    
def log_result(starting_position, path):
#    for i in range(0, len(path)):
    #        print i, path[i]
    print "FIND A PATH from starting position {}".format(starting_position)
    print '\n'.join(["{} - {}".format(i, dir_name[path[i]]) for i in range(0, len(path))])

def copy_board(board):
    new_board = []
    for row in board:
        t_row = [elt for elt in row]
        new_board.append(t_row)
    return new_board


def update_board(board, cur_position, i):
    x,y = cur_position
    dx, dy = dir_adjustment[i]
    new_board = copy_board(board)
    while (True):
        x = x + dx
        y = y + dy
        if (not inside_the_board(x,y, len(board), len(board[0]))) or board[x][y] == 1:
            break
        new_board[x][y] = 1
    return new_board, (x-dx,y-dy)


def pretty_print(board):
    for row in board:
        print ' '.join([str(x) for x in row])
    
def go(board, starting_position, cur_position, path):
#    pretty_print(board)
#    print starting_position, cur_position, path
    if check_finish_tour(board):
        log_result(starting_position, path)
        sys.exit()
    
    for i in range(0, len(dir_adjustment)):
        if available(board, cur_position, i):
            new_board, new_position = update_board(board, cur_position, i)
            go(new_board, starting_position, new_position, path + [i])


def get_data(filename):
    f = open(filename, "r")
    board = []
    for line in f.readlines():
        row = []
        line = line.strip("\n")
        for char in line:
            row.append(int(char))
        board.append(row)
    f.close()
    return board


def solve():
    _board = get_data(file_inp)
    print _board
    for i in range(0, len(_board)):
        for j in range(0, len(_board[i])):
            if _board[i][j] == 0:
#                print i,j, _board
                temp_board = copy_board(_board)
                temp_board[i][j] = 1
                go(temp_board, (i,j), (i,j), [])

    print "This program fails to find a viable solution"


solve()
    
