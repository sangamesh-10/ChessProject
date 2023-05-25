import random
# import codecs

from Board import *
from Move import *
from Piece import *
from PieceColor import *
from PieceType import *
from Square import *
from SquarePieceHybrid import *

class CunningAnu:
    def __init__(self, color):
        self.color = color
        self.opp_color = -1
        if(self.color==PieceColor.White):
            self.opp_color = PieceColor.Black
        else:
            self.opp_color = PieceColor.White
        

    def move(self, board):
        pieces = []
        candidate_moves = []
        for i in range(8):
            for j in range(8):
                tmp_sph = board[i][j]
                if(self.color == tmp_sph.piece.color):
                    pm = self.possible_moves(tmp_sph, board)
                    for move in pm:
                        candidate_moves.append(move)
                    # candidate_moves.append(self.possible_moves(tmp_sph))
        
        # print("Candidate moves reached")
        # non_cands = []
        # for c in candidate_moves:
            # print("I ran")
            # print(isinstance(c, Move))
            # print(type(c))
            # if not isinstance(c, Move):
            #     non_cands.append(c)
        
        # print(f"The length of candidates is:: {len(candidate_moves)}")
        # print(f"The length of non candidtae moves is:: {len(non_cands)}")
        # print(candidate_moves)
        # candidate_moves = list(filter(lambda x: board[x.to_sq.row][x.to_sq.col].piece.type == PieceType.Nill, candidate_moves))
        # candidate_moves = list(filter(lambda x: self.not_crossing(x, board), candidate_moves))
        chosen_move = random.choice(candidate_moves)
        # print(type(chosen_move))
        board[chosen_move.from_sq.row][chosen_move.from_sq.col] = SquarePieceHybrid(chosen_move.from_sq.row, chosen_move.from_sq.col, PieceColor.Nill, PieceType.Nill)
        board[chosen_move.to_sq.row][chosen_move.to_sq.col] = SquarePieceHybrid(chosen_move.to_sq.row, chosen_move.to_sq.col, chosen_move.piece.color, chosen_move.piece.type)


    
    def possible_moves(self, sph, board):
        poss_moves = []
        poss_squares = []
        # match sph.piece.type:
        if sph.piece.type== PieceType.King:
            row = sph.sq.row
            col = sph.sq.col

            arr1 = [row-1, row, row+1]
            arr2 = [col-1, col, col+1]
            for i in arr1:
                for j in arr2:
                    if((i!= row or j!=col) and (i > -1 and i < 8) and (j > -1 and j < 8)):
                        if(board[i][j].piece.type == PieceType.Nill or board[i][j].piece.color == self.opp_color):
                            tmp_sq = Square(i, j)
                            poss_squares.append(tmp_sq)
                            poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i, j)))
                    
            pass
        elif sph.piece.type ==  PieceType.Queen:
            # Rook moves
            arr3 = [1, 2, 3, 4, 5, 6, 7]
            arr4 = [-1, -2, -3, -4, -5, -6, -7]
            row = sph.sq.row
            col = sph.sq.col
            # prohibited = set()
            for i in arr3:
                tmp1 = row+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[tmp1][col].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                    elif(board[tmp1][col].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                        break
                    elif(board[tmp1][col].piece.color == self.color):
                        break
            
            for i in arr4:
                tmp1 = row+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[tmp1][col].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                    elif(board[tmp1][col].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                        break
                    elif(board[tmp1][col].piece.color == self.color):
                        break

            
            for i in arr3:
                tmp1 = col+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[row][tmp1].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                    elif(board[row][tmp1].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                        break
                    elif(board[row][tmp1].piece.color == self.color):
                        break
            
            for i in arr4:
                tmp1 = col+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[row][tmp1].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                    elif(board[row][tmp1].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                        break
                    elif(board[row][tmp1].piece.color == self.color):
                        break
            #Bishop time
            arr_1 = [1, -1]
            arr_2 = [1, -1]
            arr1 = [1, -1]
            arr2 = [1, -1]
            row = sph.sq.row
            col = sph.sq.col
            prohibited = set()
            k=1
            break_outer = False

            # print("I ran 1")
            while(k < 7):
                for indi, i in enumerate(arr1):
                    for indj, j in enumerate(arr2):
                        if(tuple([indi, indj]) not in prohibited):
                            tmpi  = row+i
                            tmpj = col + j
                            if((tmpi > -1 and tmpi < 8) and (tmpj > -1 and tmpj < 8)):
                                # print(tmpi, tmpj)
                                if(board[tmpi][tmpj].piece.type == PieceType.Nill):
                                    tmp_move = Move(sph.piece.color, sph.piece.type, Square(sph.sq.row, sph.sq.col), Square(tmpi, tmpj))
                                    poss_squares.append(Square(tmpi, tmpj))
                                    poss_moves.append(tmp_move)
                                elif(board[tmpi][tmpj].piece.color==self.opp_color):   
                                    poss_squares.append(Square(tmpi, tmpj))
                                    tmp_move = Move(sph.piece.color, sph.piece.type, Square(sph.sq.row, sph.sq.col), Square(tmpi, tmpj))
                                    poss_moves.append(tmp_move)
                                    prohibited.add(tuple([indi, indj]))
                                elif(board[tmpi][tmpj].piece.color==self.color):
                                    prohibited.add(tuple([indi, indj]))
                        # print(prohibited)
                k+=1
                for i in range(len(arr1)):
                    arr1[i] = k*arr_1[i]
                # print(arr1)
                # arr2 = arr2*k
                for i in range(len(arr2)):
                    arr2[i] = k*arr_2[i]

            # print("I ran 2")
            # print(poss_moves)
            pass
        elif sph.piece.type== PieceType.Rook:
            arr3 = [1, 2, 3, 4, 5, 6, 7]
            arr4 = [-1, -2, -3, -4, -5, -6, -7]
            row = sph.sq.row
            col = sph.sq.col
            # prohibited = set()
            for i in arr3:
                tmp1 = row+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[tmp1][col].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                    elif(board[tmp1][col].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                        break
                    elif(board[tmp1][col].piece.color == self.color):
                        break
            
            for i in arr4:
                tmp1 = row+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[tmp1][col].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                    elif(board[tmp1][col].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                        break
                    elif(board[tmp1][col].piece.color == self.color):
                        break

            
            for i in arr3:
                tmp1 = col+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[row][tmp1].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                    elif(board[row][tmp1].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                        break
                    elif(board[row][tmp1].piece.color == self.color):
                        break
            
            for i in arr4:
                tmp1 = col+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[row][tmp1].piece.type == PieceType.Nill):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                    elif(board[row][tmp1].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                        break
                    elif(board[row][tmp1].piece.color == self.color):
                        break
            pass
        elif sph.piece.type== PieceType.Bishop:
            arr_1 = [1, -1]
            arr_2 = [1, -1]
            arr1 = [1, -1]
            arr2 = [1, -1]
            row = sph.sq.row
            col = sph.sq.col
            prohibited = set()
            k=1
            break_outer = False

            # print("I ran 1")
            while(k < 7):
                for indi, i in enumerate(arr1):
                    for indj, j in enumerate(arr2):
                        if(tuple([indi, indj]) not in prohibited):
                            tmpi  = row+i
                            tmpj = col + j
                            if((tmpi > -1 and tmpi < 8) and (tmpj > -1 and tmpj < 8)):
                                # print(tmpi, tmpj)
                                if(board[tmpi][tmpj].piece.type == PieceType.Nill):
                                    tmp_move = Move(sph.piece.color, sph.piece.type, Square(sph.sq.row, sph.sq.col), Square(tmpi, tmpj))
                                    poss_squares.append(Square(tmpi, tmpj))
                                    poss_moves.append(tmp_move)
                                elif(board[tmpi][tmpj].piece.color==self.opp_color):   
                                    poss_squares.append(Square(tmpi, tmpj))
                                    tmp_move = Move(sph.piece.color, sph.piece.type, Square(sph.sq.row, sph.sq.col), Square(tmpi, tmpj))
                                    poss_moves.append(tmp_move)
                                    prohibited.add(tuple([indi, indj]))
                                elif(board[tmpi][tmpj].piece.color==self.color):
                                    prohibited.add(tuple([indi, indj]))
                        # print(prohibited)
                k+=1
                for i in range(len(arr1)):
                    arr1[i] = k*arr_1[i]
                # print(arr1)
                # arr2 = arr2*k
                for i in range(len(arr2)):
                    arr2[i] = k*arr_2[i]

            # print("I ran 2")
            # print(poss_moves)
            pass
        elif sph.piece.type== PieceType.Knight:
            row = sph.sq.row
            col = sph.sq.col

            arr1 = [-1, -2, 1, 2]
            arr2 = [-1, -2, 1, 2]

            for i in arr1:
                for j in arr2:
                    if(abs(i) != abs(j)):
                        tmp1 = row + i
                        tmp2 = col + j

                        if((tmp1 > -1 and tmp1 < 8) and (tmp2 > -1 and tmp2 < 8)):
                            if(board[tmp1][tmp2].piece.type == PieceType.Nill or board[tmp1][tmp2].piece.color == self.opp_color):
                            
                                tmp_sq = Square(tmp1, tmp2)
                                poss_squares.append(tmp_sq)
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, tmp2)))

            pass
        elif sph.piece.type== PieceType.Pawn:
            if(sph.piece.color==PieceColor.White):
                row = sph.sq.row
                col = sph.sq.col

                i = row
                j = col

                if(i > 0 and board[i-1][j].piece.type == PieceType.Nill):
                    poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i-1, j)))
                elif(i > 0 and j > 0 and board[i-1][j-1].piece.color == self.opp_color):
                    poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i-1, j-1)))
                elif(i > 0 and j < 7 and board[i-1][j+1].piece.color == self.opp_color):
                    poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i-1, j+1)))
                
            elif(sph.piece.color==PieceColor.Black):
                row = sph.sq.row
                col = sph.sq.col

                i = row
                j = col

                if(i < 7 and board[i+1][j].piece.type == PieceType.Nill):
                    poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i+1, j)))
                elif(i < 7 and j > 0 and board[i+1][j-1].piece.color == self.opp_color):
                    poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i+1, j-1)))
                elif(i < 7 and j < 7 and board[i+1][j+1].piece.color == self.opp_color):
                    poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i+1, j+1)))
                
            
        # print("Possible moves reached")
        return poss_moves








if __name__ == '__main__':
    b = Board()
    b.print_board()
    ca = CunningAnu(PieceColor.White)
    ca2 = CunningAnu(PieceColor.Black)
    for i in range(200):
        ca.move(b.board)
        b.print_board()
        if(b.check_win()):
            print("White won the game")
            break
        ca2.move(b.board)
        b.print_board()
        if(b.check_win()):
            print("Black won the game")
            break
        