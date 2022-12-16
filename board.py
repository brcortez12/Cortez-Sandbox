import piece

class Board:
    def __init__(self):
        cols, rows = (8,8)
        self.board = [[piece.Empty() for i in range(cols)] for j in range(rows)]
        params = [7, True]
        
        for i in range(2):
            # White
            self.board[params[0]][0] = piece.Rook(params[1])
            self.board[params[0]][1] = piece.Knight(params[1])
            self.board[params[0]][2] = piece.Bishop(params[1])
            self.board[params[0]][3] = piece.Queen(params[1])
            self.board[params[0]][4] = piece.King(params[1])
            self.board[params[0]][5] = piece.Bishop(params[1])
            self.board[params[0]][6] = piece.Knight(params[1])
            self.board[params[0]][7] = piece.Rook(params[1])
            params = [0, False]

        # Pawns
        for i in range(8):
            self.board[6][i] = piece.Pawn(True)
            self.board[1][i] = piece.Pawn(False)
            

    def print_board(self):
        for i in range(8):
            for j in range(7):
                print(self.board[i][j].name, end = " | ")
            print(self.board[i][7].name)

b1 = Board()

b1.print_board()
