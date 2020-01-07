import re


def isValidChessBoard(dict):
    validpiece = ['pawn','knight','bishop', 'rook','queen','king']
    countvalues = {'bcount':0, 'wcount':0,'bpawn':0,'wpawn':0, 'bking':0,'wking':0}
    for k in dict.keys(): #ensures positions is correct
         if re.match("[1-8][a-h]",k) == None:
            return False
    for j in dict.values(): #checks if piece is valid
        if j == '':
            return False
        elif j[0] != 'b' and j[0] != 'w' or j[1:] not in validpiece:
            return False
        else:
            countvalues[j[0]+'count'] += 1
        if j[1:] == 'king' or j[1:] == 'pawn': #checks if pawn or king and adds to count
            countvalues[j]+=1
            if countvalues[j] >1:
                return False
            elif countvalues[j] >8:
                return False
    if countvalues['bking'] == 0 or countvalues['wking'] == 0:
        return False
    return True


dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(dict))
