from Piece import *

class Move:
    def __init__(self, piece, from_sq, to_sq):
        self.piece = piece
        self.from_sq = from_sq
        self.to_sq = to_sq

    def __repr__(self):
        return f"Color: {self.piece.color}| Type: {self.piece.type}   From: {self.from_sq.row}{self.from_sq.col}   To: {self.to_sq.row}{self.to_sq.col}\n"


    def __init__(self, piece_color, piece_type, from_sq, to_sq):
        self.piece = Piece(piece_color, piece_type)
        self.from_sq = from_sq
        self.to_sq = to_sq
