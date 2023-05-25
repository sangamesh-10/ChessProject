from Piece import *
from Square import *





class SquarePieceHybrid:
    

    def __init__(self, sq, piece):
        self.sq = sq
        self.piece = piece
    
    def __init__(self, row, col, pc, pt):
        self.sq = Square(row, col)
        self.piece = Piece(pc, pt)
    
    # def candidate_squares(self):
    #     candidates = []
    #     type = self.piece.type

    #     if(type==PieceType.King):
    #         pass
