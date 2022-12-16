class Piece():
    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self, board, start, to):
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[94m' + self.name + '\033[0m'

class Rook(Piece):
    def __init__(self, color, first_move = True):
        # super().__init__(...) can be super helpful in just calling the 
        # parrent init function to avoid the same lines of code
        super().__init__(color)
        self.name = "R"
        self.first_move = first_move

    def is_valid_move(self, board, start, to):
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self, color, first_move = True):
        super().__init__(color)
        self.name = "K"
        self.first_move = first_move

    def is_valid_move(self):
        pass
    
    # I added an extra method for the King class
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "GP"

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"

    def is_valid_move(self):
        pass

class Empty(Piece):
    def __init__(self):
        self.name = "-"