from values import *



def opponent(team):                                                             #Opponent
    if team == 'w':
        return 'b'
    else:
        return 'w'



def printr(obj):                                                                #Printing the board with Unicodes
    print("__________________")
    for item in obj.defeatedWhite:
        print(symbols[item], end = ' ')
    print()
    print("__________________")
    for i in range(8):
        print(8-i, end = ' ')
        for j in range(8):
            print(symbols[obj.array[i][j]], end = ' ')
        print()
    print('0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    print("__________________")
    for item in obj.defeatedBlack:
        print(symbols[item], end = ' ')
    print()
    print("__________________")



def find(piece, array):                                                         #Returns a list of positions of the possible pieces
    res = []
    for i in range(0, 8):
        for j in range(0, 8):
            if array[i][j] == piece:
                res.append([i, j])
    return res



def emptyFiller(index):                                                         #Fills empty positions of the board
    if index[0]%2==0:
        if index[1]%2==0:
            return '1'
        else:
            return '0'
    else:
        if index[1]%2==0:
            return '0'
        else:
            return '1'
      


def legalMoves(piece, pos, board):                                              #Calculating the arrays of legal moves
    row = pos[0]
    column = pos[1]
    moves = []
    team = piece[0]
    if piece[-1] == 'R':                                        #Rook Function
        rowdum ,columndum = row+1, column+1
        while(rowdum <= 7):
            if board[rowdum][column][0]==team:
                break
            elif board[rowdum][column][0]=='0' or board[rowdum][column][0]=='1':
                moves.append([rowdum, column])
            else:
                moves.append([rowdum, column])
                break
            rowdum+=1 
        rowdum = row-1
        while(rowdum >= 0):
            if board[rowdum][column][0]==team:
                break
            elif board[rowdum][column][0]=='0' or board[rowdum][column][0]=='1':
                moves.append([rowdum, column])
            else:
                moves.append([rowdum, column])
                break
            rowdum-=1
        while(columndum <= 7):
            if board[row][columndum][0]==team:
                break
            elif board[row][columndum][0]=='0' or board[row][columndum][0]=='1':
                moves.append([row, columndum])
            else:
                moves.append([row, columndum])
                break
            columndum+=1 
        columndum = column-1
        while(columndum >= 0):
            if board[row][columndum][0]==team:
                break
            elif board[row][columndum][0]=='0' or board[row][columndum][0]=='1':
                moves.append([row, columndum])
            else:
                moves.append([row, columndum])
                break
            columndum-=1
        return moves
    if piece[-1] == 'B':                                    #Bishop Function
        rowdum ,columndum = row+1, column+1
        while (rowdum <= 7 and columndum <= 7):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break 
            rowdum += 1
            columndum += 1
        rowdum, columndum = row-1, column-1
        while (rowdum >= 0 and columndum >= 0):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum -= 1
            columndum -= 1
        rowdum, columndum = row-1, column+1
        while (rowdum >= 0 and columndum <= 7):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum -= 1
            columndum += 1
        rowdum, columndum = row+1, column-1
        while (rowdum <= 7 and columndum >= 0):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum += 1
            columndum -= 1
        return moves
    if piece[-1] == 'Q':                                    #Queen Function
        rowdum ,columndum = row+1, column+1
        while(rowdum <= 7):
            if board[rowdum][column][0]==team:
                break
            elif board[rowdum][column][0]=='0' or board[rowdum][column][0]=='1':
                moves.append([rowdum, column])
            else:
                moves.append([rowdum, column])
                break
            rowdum+=1 
        rowdum = row-1
        while(rowdum >= 0):
            if board[rowdum][column][0]==team:
                break
            elif board[rowdum][column][0]=='0' or board[rowdum][column][0]=='1':
                moves.append([rowdum, column])
            else:
                moves.append([rowdum, column])
                break
            rowdum-=1
        while(columndum <= 7):
            if board[row][columndum][0]==team:
                break
            elif board[row][columndum][0]=='0' or board[row][columndum][0]=='1':
                moves.append([row, columndum])
            else:
                moves.append([row, columndum])
                break
            columndum+=1 
        columndum = column-1
        while(columndum >= 0):
            if board[row][columndum][0]==team:
                break
            elif board[row][columndum][0]=='0' or board[row][columndum][0]=='1':
                moves.append([row, columndum])
            else:
                moves.append([row, columndum])
                break
            columndum-=1
        rowdum ,columndum = row+1, column+1
        while (rowdum <= 7 and columndum <= 7):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum += 1
            columndum += 1
        rowdum, columndum = row-1, column-1
        while (rowdum >= 0 and columndum >= 0):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum -= 1
            columndum -= 1
        rowdum, columndum = row-1, column+1
        while (rowdum >= 0 and columndum <= 7):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum -= 1
            columndum += 1
        rowdum, columndum = row+1, column-1
        while (rowdum <= 7 and columndum >= 0):
            if board[rowdum][columndum][0]==team:
                break
            elif board[rowdum][columndum][0]=='0' or board[rowdum][columndum][0]=='1':
                moves.append([rowdum, columndum])
            elif board[rowdum][columndum][0]!=team:
                moves.append([rowdum, columndum])
                break
            rowdum += 1
            columndum -= 1
        return moves
    if piece[-1] == 'K':                                    #King Function
        for i in range(0, 1):
            if(row+1<=7):
                if(board[row+1][column][0]!=team):
                    moves.append([row+1, column])
            if(row-1>=0):
                if(board[row-1][column][0]!=team):
                    moves.append([row-1, column])
            if(column+1<=7):
                if(board[row][column+1][0]!=team):
                    moves.append([row, column+1])
            if(column-1>=0):
                if(board[row][column-1][0]!=team):
                    moves.append([row, column-1])
            if(row+1<=7 and column+1<=7):
                if(board[row+1][column+1][0]!=team):
                    moves.append([row+1, column+1])
            if(row-1>=0 and column-1>=0):
                if(board[row-1][column-1][0]!=team):
                    moves.append([row-1, column-1])
            if(row+1<=7 and column-1>=0):
                if(board[row+1][column-1][0]!=team):
                    moves.append([row+1, column-1])
            if(row-1>=0 and column+1<=7):
                if(board[row-1][column+1][0]!=team):
                    moves.append([row-1, column+1])
        return moves
    if piece[-1] == 'N':                                     #Knight Function
        if(column+2<=7):
            if(row-1>=0):
                if(board[row-1][column+2][0] != team):
                    moves.append([row-1, column+2])
            if(row+1<=7):
                if(board[row+1][column+2][0] != team):
                    moves.append([row+1, column+2])
        if(column+1<=7):
            if(row-2>=0):
                if(board[row-2][column+1][0] != team):
                    moves.append([row-2, column+1])
            if(row+2<=7):
                if(board[row+2][column+1][0] != team):
                    moves.append([row+2, column+1])
        if(column-2>=0):
            if(row-1>=0):
                if(board[row-1][column-2][0] != team):
                    moves.append([row-1, column-2])
            if(row+1<=7):
                if(board[row+1][column-2][0] != team):
                    moves.append([row+1, column-2])
        if(column-1>=0):
            if(row-2>=0):
                if(board[row-2][column-1][0] != team):
                    moves.append([row-2, column-1])
            if(row+2<=7):
                if(board[row+2][column-1][0] != team):
                    moves.append([row+2, column-1])
        return moves
    if piece == 'bP':                                       #BlackPawn
        if(row+1<=7):
            if(board[row+1][column][0] =='0' or board[row+1][column][0] == '1'):                                       
                moves.append([row+1, column])
            if(column-1>=0): 
                if(board[row+1][column-1][0]=='w'): 
                    moves.append([row+1, column-1])
            if(column+1<=7): 
                if(board[row+1][column+1][0]=='w'): 
                    moves.append([row+1, column+1])
        if row == 1:
            if(board[row+2][column][0]) == '0' or (board[row+2][column][0]) == '1':
                moves.append([row+2, column])
        return moves
    if piece == 'wP':                                       #WhitePawn
        if(row-1>=0):
            if(board[row-1][column][0] =='0' or board[row-1][column][0] == '1'):                                      
                moves.append([row-1, column])
            if(column-1>=0): 
                if(board[row-1][column-1][0]=='b'): 
                    moves.append([row-1, column-1])
            if(column+1<=7): 
                if(board[row-1][column+1][0]=='b'): 
                    moves.append([row-1, column+1])
        if row == 6:
            if(board[row-2][column][0]) == '0' or (board[row-2][column][0]) == '1':
                moves.append([row-2, column])
        return moves



def allMoves(team, array):                                                      #Calculating all the possible moves for the team
    moveArray = []
    for i in range(0, 8):
        for j in range(0, 8):
            if(array[i][j][0] == team):
                if(legalMoves(array[i][j], [i, j], array)!=None):
                    moveArray+=(legalMoves(array[i][j], [i, j], array))
    return moveArray



def isCheck(team, index1, index2, obj, obj2):                                   #Check function
    obj2.array = list(map(list, obj.array))
    obj2.move(index1, index2)
    if find(team+'K', obj2.array)[0] in allMoves(opponent(team), obj2.array):
        return  True
    return False
    


def inCheck(team, array):
    if find(team+'K', array)[0] in allMoves(opponent(team), array):
        return  True
    return False



def isMate(team, obj, obj2):                                                    #Checkmate function
    for i in range(0, 8):
        for j in range(0, 8):
            if(obj.array[i][j][0] == team):
                if legalMoves(obj.array[i][j], [i, j], obj.array) != None:
                    for item in legalMoves(obj.array[i][j], [i, j], obj.array):
                        if isCheck(team, [i, j], item, obj, obj2) == False:
                            return False
    return True



class commands:                                                                 #Converting input into commands
    def __init__(self, inp, team) :                                              #Constructor
        inp = inp.upper()
        self.team = team
        self.castling = None
        if(len(inp) == 2):
            self.piece = team+'P'
            self.targetIndex =[8-int(inp[-1]), posLet[inp[-2]]]
        elif '=' in inp:
            self.piece = team+'P'
            self.promotion= team+(inp[-1].upper())
            self.targetIndex =[8-int(inp[-3]), posLet[inp[-4]]]
        elif('x' in inp):
            self.piece = team+inp.split('x', 1)[0]
            self.targetIndex =[8-int(inp.split('x', 1)[1][1]), posLet[inp.split('x', 1)[1][0]]]
        elif(inp == 'O-O-O'):
            self.castling = 'queen'
        elif(inp == 'O-O'):
            self.castling = 'king'
        else:
            self.piece = team + inp[0]
            self.targetIndex =[8-int(inp[-1]), posLet[inp[-2]]]



class board:                                                                    #All properties of board 
    def __init__(self):                                                         #Constructor
        self.array = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB' , 'bN' , 'bR'],       #2-D Array representing the board
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['1', '0', '1', '0', '1', '0', '1', '0'],
        ['0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0'],
        ['0', '1', '0', '1', '0', '1', '0', '1'],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        '''self.array = [['bR', 'bN', 'bB', 'bK', 'bQ', 'bN', 'bB', 'bR'], ['bP', 'bP', 'wQ', 'bP', 'bP', 'bP', 'bP', '1'], ['1', '0', '1', '0', '1', '0', '1', '0'], ['0', '1', '0', '1', '0', '1', '0', '1'], ['1', '0', '1', '0', '1', 'wB', '1', 'bP'], ['0', '1', '0', 'wP', '0', '1', '0', '1'], ['wP', 'wP', 'wP', '0', 'wP', 'wP', 'wP', 'wP'], ['wR', 'wN', '0', 'wK', '0', 'wB', 'wN', 'wR']]'''
        self.defeatedBlack = []
        self.defeatedWhite = []
    def capture(self, attackIndex, takenIndex):                                 #Capturing of pieces
        if self.array[takenIndex[0]][takenIndex[1]][0] == 'w':
            self.defeatedWhite.append(self.array[takenIndex[0]][takenIndex[1]])
        else:
            self.defeatedBlack.append(self.array[takenIndex[0]][takenIndex[1]])
        self.array[takenIndex[0]][takenIndex[1]] = self.array[attackIndex[0]][attackIndex[1]]
        self.array[attackIndex[0]][attackIndex[1]] = emptyFiller(attackIndex)
    def move(self, pieceIndex, targetIndex):                                    #Moving of pieces
        if(self.array[targetIndex[0]][targetIndex[1]] == '0' or self.array[targetIndex[0]][targetIndex[1]] == '1'):
            self.array[targetIndex[0]][targetIndex[1]] = self.array[pieceIndex[0]][pieceIndex[1]]
            self.array[pieceIndex[0]][pieceIndex[1]] = emptyFiller(pieceIndex)
        else:
            self.capture(pieceIndex, targetIndex)



class imaginaryBoard:                                                           #All properties of imaginaryBoard 
    def __init__(self):
        self.array = []
    def capture(self, attackIndex, takenIndex):                                 #Capturing of pieces
        self.array[takenIndex[0]][takenIndex[1]] = self.array[attackIndex[0]][attackIndex[1]]
        self.array[attackIndex[0]][attackIndex[1]] = emptyFiller(attackIndex)
    def move(self, pieceIndex, targetIndex):                                    #Moving of pieces
        if(self.array[targetIndex[0]][targetIndex[1]] == '0' or self.array[targetIndex[0]][targetIndex[1]] == '1'):
            self.array[targetIndex[0]][targetIndex[1]] = self.array[pieceIndex[0]][pieceIndex[1]]
            self.array[pieceIndex[0]][pieceIndex[1]] = emptyFiller(pieceIndex)
        else:
            self.capture(pieceIndex, targetIndex)



def swap(board, index1, index2):                                                #Swapping two pieces
    temp = board[index1[0]][index1[1]]
    board[index1[0]][index1[1]] = board[index2[0]][index2[1]]
    board[index2[0]][index2[1]] = temp