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
    
    def parse_input(self, input_loc):
        """
        Convert user input string into list/row, column coordinates
        """
        # TODO: check format of the user input is correct
        loc = input_loc.split(',')
        loc = [int(x) for x in loc]
        return loc
    
    def check_valid_move(self, loc):
        # get row, column coordinates
        r, c = loc

        # if the board location is blank, the user move is valid
        if self.board[r][c] == " ":
            return True
        else:
            print("ERROR: Invalid location, try again.")
            return False

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
        # check if user input is at a valid location
        valid_move = False
        while not valid_move:
            print(f'Player {piece}, enter row,column:')
            input_loc = input()
            loc = self.parse_input(input_loc)
            valid_move = self.check_valid_move(loc)

        # place piece at location
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