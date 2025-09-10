class Board(object):
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.pieces = ('X', 'O')
        self.turn = 0
        self.terminal = False

    def get_piece(self):
        if self.turn % 2 == 0:
            return self.pieces[0]
        else:
            return self.pieces[1]
        
    def display(self):
        """
        Display the board to the terminal
        """
        print()
        print("BOARD")
        print("=====")
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
        # get current piece
        piece = self.get_piece()
        # get user input
        print(f'Player {piece}, enter row,column:')
        input_loc = input()

        # check if user input is at a valid location

        # place piece at location
        loc = input_loc.split(',')
        loc = [int(x) for x in loc]
        self.place(piece,loc)

        # check board pattern for player victory

        # check if board is full/draw

        # update turn index
        self.turn += 1
        return
    

def main():
    board = Board()
    print("TIC-TAC-TOE!")

    while not board.terminal:
        board.display()
        board.step()
        

if __name__ == "__main__":
    main()