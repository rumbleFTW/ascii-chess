from funcs import *
from values import *
import os



b1 = board()
b2 = imaginaryBoard()



while end:                                                     #MainLoop
    control += 1
    if os.name == 'posix': os.system('clear')
    else: os.system('cls')
    legalCount = 0
    print(message)
    printr(b1)
    message = ''
    team1, team2 = True, True
    if control %2 == 0:
        while team1:
            print("White's Move:")
            team = 'w'
            if inCheck(team, b1.array):
                if isMate(team, b1, b2):
                    print("Checkmate!, Black wins.")
                    end = False
                    break
            if isMate(team, b1, b2):
                    print("Stalemate!, It's a Draw.")
                    end = False
                    break
            inp = input()
            try:
                command = commands(inp, team)
                for item in find(command.piece, b1.array):
                    if command.targetIndex in legalMoves(command.piece, item, b1.array):
                        print(legalMoves(command.piece, item, b1.array))
                        if isCheck(team, item, command.targetIndex, b1, b2):
                            break
                        if(command.piece == 'wP') and command.targetIndex[0] == 0:
                            if(command.promotion != 'wK' and command.promotion != 'wP'):
                                b1.move(item, command.targetIndex)
                                b1.array[command.targetIndex[0]][command.targetIndex[1]] = command.promotion        #Promotion
                                legalCount += 1
                                team1 = False
                            break
                        b1.move(item, command.targetIndex)
                        legalCount += 1
                        team1 = False
                        break
                if legalCount<=0:
                        print('Please enter a Legal move!')
            except:
                print('Please enter a Valid move!')
    else:
        while team2:
            print("Black's Move:")
            team = 'b'
            if inCheck(team, b1.array):
                if isMate(team, b1, b2):
                    print("Checkmate!, White wins.")
                    end = False
                    break
            if isMate(team, b1, b2):
                    print("Stalemate!, It's a Draw.")
                    end = False
                    break
            inp = input()
            try:
                command = commands(inp, team)
                for item in find(command.piece, b1.array):
                    if command.targetIndex in legalMoves(command.piece, item, b1.array):
                        print(legalMoves(command.piece, item, b1.array))
                        if isCheck(team, item, command.targetIndex, b1, b2):
                            break
                        if(command.piece == 'bP') and command.targetIndex[0] == 7:                              
                            if(command.promotion != 'bK' and command.promotion != 'bP'):
                                b1.move(item, command.targetIndex)
                                b1.array[command.targetIndex[0]][command.targetIndex[1]] = command.promotion        #Promotion
                                legalCount += 1
                                team2 = False
                            break
                        b1.move(item, command.targetIndex)
                        legalCount += 1
                        team2 = False
                        break
                if legalCount<=0:
                        print('Please enter a Legal move!')
            except:
                print('Please enter a Valid move!')
                