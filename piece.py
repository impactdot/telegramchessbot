# распишите юникод здесь
# pawn - пешка
# bishop - слон
# knight - конь
# king - король
# queen - ферзь
# rook - ладья


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
        self.king = False
        self.pawn = False
        self.img = ""

    def isSelected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def __str__(self):
        return self.img


class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        if color == "b":
            self.img = "\u2659"
        else:
            self.img = "\u265F"


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        if color == "b":
            self.img = "\u2657"
        else:
            self.img = "\u265D"


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        if color == "b":
            self.img = "\u2655"
        else:
            self.img = "\u265B"


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        if color == "b":
            self.img = "\u2654"
        else:
            self.img = "\u265A"


class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        if color == "b":
            self.img = "\u2656"
        else:
            self.img = "\u265C"


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        if color == "b":
            self.img = "\u2658"
        else:
            self.img = "\u265E"

    def valid_moves(self):
        # используйте self.row и self.col, чтобы определить возможные ходы
        pass


# white pieces
white_rook_test = Rook(0, 0, "w")
print(white_rook_test)