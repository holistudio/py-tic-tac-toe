class Board(object):
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    def display(self):
        """
        Display the board to the terminal
        """
        for i,row in enumerate(self.board):
            row_disp = ("|").join(row)
            print(row_disp)
            if i < 2:
                print("-----")
        return
    

def main():
    board = Board()
    print("TIC-TAC-TOE!")
    board.display()

if __name__ == "__main__":
    main()