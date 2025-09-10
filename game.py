class Board(object):
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.pieces = ('X', 'O')
        self.turn = 0

    def get_piece(self):
        if self.turn % 2 == 0:
            return self.pieces[0]
        else:
            return self.pieces[1]
        
    def display(self):
        """
        Display the board to the terminal
        """
        print("BOARD")
        for i,row in enumerate(self.board):
            row_disp = ("|").join(row)
            print(row_disp)
            if i < 2:
                print("-----")
        print()
        return
    
    def place(self, piece, location):
        """
        Places a piece on the board at the specified location
        """
        r, c = location
        self.board[r][c] = piece
        return
    
    def step(self):
        # get user input

        # check if user input is at a valid location

        # place piece at location

        # check board pattern for player victory

        # check if board is full/draw

        # update turn index
        return
    

def main():
    board = Board()
    print("TIC-TAC-TOE!")
    board.display()

    board.place(piece=board.get_piece(),location=(1,1))
    board.display()

if __name__ == "__main__":
    main()