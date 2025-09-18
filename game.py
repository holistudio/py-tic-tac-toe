class Agent(object):
    def __init__(self):
        pass
    def action(self, state):
        # given the state of the board, pick a next location of piece
        location = (0,0)
        return location
    
class Board(object):
    def __init__(self):
        # initial empty board
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]

        # possible board pieces
        self.pieces = ('X', 'O')

        self.turn = 0 # turn index
        # assume turn 0, 2, .. is human player

        # track if game is over or not
        self.terminal = False

    def get_piece(self):
        """
        Alternate between X or O piece depending on the turn index
        """
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
        print("=====")
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

        # TODO: check if location is within bounds of the board

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
    
    def check_victory(self):
        """
        Check connect 3 pattern in all possible variations
        """
        def check_rows(board):
            """
            Check connect 3 pattern in rows
            """
            for i in range(3):
                # print(f"Checking row {i}...")
                # check if none of the locations in the row are blank
                location_blank = (board[i][0] == " ") or (board[i][1] == " ") or (board[i][2] == " ")
                if not location_blank:
                    # check if all pieces are same for this row
                    if board[i][0] == board[i][1]:
                        if board[i][1] == board[i][2]:
                            return True
            return False
        
        def check_cols(board):
            """
            Check connect 3 pattern in columns
            """
            for i in range(3):
                # print(f"Checking col {i}...")
                # check if none of the locations in the col are blank
                location_blank = (board[0][i] == " ") or (board[1][i] == " ") or (board[2][i] == " ")
                if not location_blank:
                    # check if all pieces are same for this col
                    if board[0][i] == board[1][i]:
                        if board[1][i] == board[2][i]:
                            return True
            return False
        
        def check_diags(board):
            """
            Check connect 3 pattern in diagonals
            """
            # top left to bottom right diagonal
            # print('Checking diagonal 1...')
            # check if none of the locations in the col are blank
            location_blank = (board[0][0] == " ") or (board[1][1] == " ") or (board[2][2] == " ")
            if not location_blank:
                # check if all pieces are same for this col
                if board[0][0] == board[1][1]:
                    if board[1][1] == board[2][2]:
                        return True
            
            # top right to bottom left diagonal
            # print('Checking diagonal 2...')
            # check if none of the locations in the col are blank
            location_blank = (board[2][0] == " ") or (board[1][1] == " ") or (board[0][2] == " ")
            if not location_blank:
                # check if all pieces are same for this col
                if board[2][0] == board[1][1]:
                    if board[1][1] == board[0][2]:
                        winning_piece = board[0][2]
                        return True
            return False
        
        # immediately return True if one of the checks is met
        if check_rows(self.board):
            return True
        
        if check_cols(self.board):
            return True
        
        if check_diags(self.board):
            return True
        
        return False
                

    def step(self, agent_location):
        """
        Operations to perform at every step of the game
        """
        # get current piece
        piece = self.get_piece()

        # if it's the first turn, it's human
        # otherwise place AI piece
        if self.turn % 2 != 0:
            # # place AI piece
            # self.place(piece,agent_location)
            # # update turn index
            # self.turn += 1
            # # switch to next piece
            # piece = self.get_piece()
            loc = agent_location
        else:
            # get user input
            # check if user input is at a valid location
            valid_move = False
            while not valid_move:
                print(f'[{self.turn}] Player {piece}, enter row,column:')
                input_loc = input()
                loc = self.parse_input(input_loc)
                valid_move = self.check_valid_move(loc)

        # place user piece at location
        self.place(piece,loc)

        # check board pattern for player victory
        victory = self.check_victory()
        if victory:
            print()
            print(f'WINNER PLAYER {piece}!')

            # display the board before the main while loop ends
            self.display()

        # check draw if board is full and still no victory from either player
        draw = False
        if self.turn >= 8 and not victory:
            draw = True
            print()
            print(f'DRAW!')

            # display the board before the main while loop ends
            self.display()

        if victory or draw:
            self.terminal = True

        # update turn index
        if not self.terminal:
            self.turn += 1

        return self.board, self.terminal
    

def main():
    # intialize board
    board = Board()

    # initialize agent
    agent = Agent()

    print("TIC-TAC-TOE!")

    # initialize loop termination condition
    terminal = False
    location = None

    while not terminal:
        # game displays the board at every step
        board.display()

        # get board state and game terminal condition
        state, terminal = board.step(location)
        
        # get the next piece location from the agent
        location = agent.action(state)

    print("GAME OVER!")
        

if __name__ == "__main__":
    main()