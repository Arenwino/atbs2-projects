'''
Chapter 5 Dictionaries and Structuring Data

Chess Dictionary Validator

In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument 
and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white
king. Each player can only have at most 16 pieces, at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
be on space '9z'. The piece names begin with either a 'w' or 'b' to represent 
white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or
'king'. This function should detect when a bug has resulted in an improper
chess board.

'''
correctcb = {'8h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
wrongNumber = {'8h': 'bking', '6c': 'wqueen', '0g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
wrongLetter = {'8h': 'bking', '6i': 'wqueen', '0g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
twoBKings = {'8h': 'bking', '2h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
twoWKings = {'8h': 'bking', '6c': 'wqueen', '2g': 'wking', '5g': 'bqueen', '3e': 'wking'}
seventeenBPieces = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bbishop', '1f': 'bbishop', '1g': 'bbishop', '1h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}
seventeenWPieces = {'8a': 'bking', '8b': 'bqueen', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bbishop', '8f': 'bbishop', '8g': 'bbishop', '8h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn', '6a': 'wpawn'}
nineBPawns = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bbishop', '1g': 'bbishop', '1h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}
nineWPawns = {'8a': 'bking', '8b': 'bqueen', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bbishop', '8f': 'bbishop', '8g': 'bbishop', '8h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn', '6a': 'wpawn'}
wrongNames = {'8h': 'bkeeng', '6c': 'wqueen', '2g': 'wking', '5g': 'bqueen', '3e': 'wking'}

piecesNames = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

def isValidChessBoard(chessBoard):

    totalbCount = 0
    totalwCount = 0
    bkingCount = 0
    wkingCount = 0
    bpawnCount = 0    
    wpawnCount = 0

    for currentValue in chessBoard.values():
        if(currentValue[0] is 'b'):
            totalbCount += 1
        if(currentValue[0] is 'w'):
            totalwCount += 1
        if(currentValue is 'bking'):
            bkingCount += 1
        if(currentValue is 'wking'):
            wkingCount += 1
        if(currentValue is 'bpawn'):
            bpawnCount += 1
        if(currentValue is 'wpawn'):
            wpawnCount += 1
     
        if(bkingCount > 1):
            print('There is more than one black king')
            return False
        if(wkingCount > 1):
            print('There is more than one white king')
            return False

        if(totalbCount > 16):
            print('There are more than 16 black chess pieces on this board')
            return False
        if(totalwCount > 16):
            print('There are more than 16 white chess pieces on this board')
            return False

        if(bpawnCount > 8):
            print('There are more than 8 black pawns on this board')
            return False
        if(wpawnCount > 8):
            print('There are more than 8 white pawns on this board')
            return False
        if(currentValue[1:] not in piecesNames):
            print(f'{currentValue[1:]} is not a valid chess piece name')
            return False

    for currentKey in chessBoard.keys():
        if(int(currentKey[0]) < 1 or int(currentKey[0]) > 8):
            print(f'Position is not between 8 and 8: {currentKey}')
            return False
        elif(ord(currentKey[1]) < 97 or ord(currentKey[1]) > 104):
            print(f'Position is not between a and h: {currentKey}')
            return False
    return True

print(isValidChessBoard(correctcb))
print(isValidChessBoard(wrongNumber)) 
print(isValidChessBoard(wrongLetter))
print(isValidChessBoard(twoBKings))
print(isValidChessBoard(twoWKings))
print(isValidChessBoard(seventeenBPieces))
print(isValidChessBoard(seventeenWPieces))
print(isValidChessBoard(nineBPawns))
print(isValidChessBoard(nineWPawns))
print(isValidChessBoard(wrongNames))