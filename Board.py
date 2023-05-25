import codecs

from PieceColor import *
from PieceType import *
from SquarePieceHybrid import *

class Board:

    def return_str(self, sph):
        color = sph.piece.color
        type = sph.piece.type

        color_str = ""
        type_str = ""

        isPiece = False

        if(color == PieceColor.Black):
            isPiece = True
            color_str = "B"
        elif(color == PieceColor.White):
            isPiece = True
            color_str = "W"

        if(type == PieceType.Rook):
            type_str = "R"
        elif(type == PieceType.Knight):
            type_str = "N"
        elif(type == PieceType.Bishop):
            type_str = "B"
        elif(type == PieceType.King):
            type_str = "K"
        elif(type == PieceType.Queen):
            type_str = "Q"
        elif(type==PieceType.Pawn):
            type_str = "P"
        
        ans = color_str + type_str
        if isPiece == True:
            return ans
        else:
            return "  "


    def print_board(self):
        with codecs.open("out.txt", 'a', "utf-8") as f:
            f.write("\n")
            f.write("-" * 33 + "\n")
            for i in range(8):
                for j in range(8):
                    f.write("|")
                    outit = self.d[self.return_str(self.board[i][j])]
                    f.write(outit)
                    if(outit=="  "):
                        f.write(" ")
                    # f.write(" ")
                    # f.write("|")
                f.write("|"+ "\n")
                f.write("-"*33+ "\n")
            f.write("\n")
        
    def check_win(self):
        wk_there = False
        bk_there = False

        for i in range(8):
            for j in range(8):
                if(self.board[i][j].piece.type==PieceType.King and self.board[i][j].piece.color==PieceColor.White):
                    wk_there = True
                if(self.board[i][j].piece.type==PieceType.King and self.board[i][j].piece.color==PieceColor.Black):
                    bk_there = True

        if(wk_there == False or bk_there==False):
            return True
        else:
            return False
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

        self.d = {
            "WP" : "\u2659 ",
            "WR" : "\u2656 ",
            "WN" : "\u2658 ",
            "WB" : "\u2657 ",
            "WK" : "\u2654 ",
            "WQ" : "\u2655 ",
            "BP" : "\u265F ",
            "BR" : "\u265C ",
            "BN" : "\u265E ",
            "BB" : "\u265D ",
            "BK" : "\u265A ",
            "BQ" : "\u265B ",
            "  " : "  "
        }
        
        tmp_hybrid = SquarePieceHybrid(0, 0, PieceColor.Black, PieceType.Rook)

        self.board[0][0] = tmp_hybrid

        for i in range(2, 6):
            for j in range(0, 8):
                self.board[i][j] = SquarePieceHybrid(i, j, PieceColor.Nill, PieceType.Nill)
        
        for j in range(0, 8):
            self.board[1][j] = SquarePieceHybrid(1, j, PieceColor.Black, PieceType.Pawn)
        
        for j in range(0, 8):
            self.board[6][j] = SquarePieceHybrid(6, j, PieceColor.White, PieceType.Pawn)
        
        for j in range(0, 8):
            sph = self.fill_initial_posns(j, PieceColor.Black)
            if(sph!=-1):
                self.board[0][j] = sph
        
        for j in range(0, 8):
            sph = self.fill_initial_posns(j, PieceColor.White)
            if(sph!=-1):
                self.board[7][j] = sph
        
        self.board[0][3] = SquarePieceHybrid(0, 3, PieceColor.Black, PieceType.King)
        self.board[0][4] = SquarePieceHybrid(0, 4, PieceColor.Black, PieceType.Queen)
        self.board[7][3] = SquarePieceHybrid(7, 3, PieceColor.White, PieceType.King)
        self.board[7][4] = SquarePieceHybrid(7, 4, PieceColor.White, PieceType.Queen)

    def fill_initial_posns(self, col, pc):
        dist1 = abs(col-0)
        dist2 = abs(col-7)

        indicator = min(dist1, dist2)

        pt = -1
        if indicator==0:
            pt = PieceType.Rook
        elif indicator==1:
            pt = PieceType.Knight
        elif indicator == 2:
            pt = PieceType.Bishop
        
        row = -1
        if(pc==PieceColor.Black):
            row = 0
        elif(pc==PieceColor.White):
            row=7
        
        if(pt!=-1):
            tmp_ans = SquarePieceHybrid(row, col, pc, pt)
            return tmp_ans
        else:
            return -1

