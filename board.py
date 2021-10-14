# распишите юникод здесь
# pawn - пешка
# bishop - слон
# knight - конь
# king - король
# queen - ферзь
# rook - ладья


class Piece():
    def __init__(self, color, type, unic):
        self.color = color
        self.type = type
        self.unic = unic

    def __str__(self):
        return self.unic


# white pieces
w_king = Piece("white", "king", "\u2654")
w_queen = Piece("white", "queen", "\u2655")
w_rk = Piece("white", "rook", "\u2656")
w_bs = Piece("white", "bishop", "\u2657")
w_kn = Piece("white", "knight", "\u2658")
w_pw = Piece("white", "pawn", "\u2659")
# black pieces
b_king = Piece("black", "king", "\u265A")
b_queen = Piece("black", "queen", "\u265B")
b_rk = Piece("black", "rook", "\u265C")
b_bs = Piece("black", "bishop", "\u265D")
b_kn = Piece("black", "knight", "\u265E")
b_pw = Piece("black", "pawn", "\u265F")
# test
print(w_king)
