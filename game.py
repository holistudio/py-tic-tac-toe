class Board(object):
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]

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
    
    def step(self, piece, location):
        """
        Places a piece on the board at the specified location
        """
        r, c = location
        self.board[r][c] = piece
        return
    

def main():
    board = Board()
    print("TIC-TAC-TOE!")
    board.display()
    board.step(piece='X',location=(1,1))
    board.display()

if __name__ == "__main__":
    main()