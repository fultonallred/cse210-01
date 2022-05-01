# W02 Prove: Developer - Solo Code Submission (tic-tac-toe game)
# Author: Fulton Allred


def main():

    xo_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_positions = []
    o_positions = []

    # The number of times the game has looped.
    loop_count = 0

    # Loop until there is a winner.
    while True:


        # Determine who's turn it is based on the number of loops.
        if (loop_count % 2) == 0:
            player = 1
        else:
            player = 2

        # Draw the gameboard.
        draw_board(xo_positions)

        # Loop until valid play is made.
        while True:
            # Ask player 1 to play.
            play = get_play()

            # Validate the play.
            verification = verify_play(play, xo_positions)

            if verification == True:
                break
        
        # Apply last play to the positions list.
        xo_positions, x_positions, o_positions = edit_positions(player, play, xo_positions, x_positions, o_positions)

        # Determine win.
        winner = determine_win(x_positions, o_positions)

        # Exit loop if there is a winner.
        if winner == True:
            break

        loop_count += 1


        


# Draw the current board.
def draw_board(xo_positions):
    """This function draws the game board.

    Parameters:
        none 

    Return:
        gameboard - the gameboard"""

    print(f"{xo_positions[0]} | {xo_positions[1]} | {xo_positions[2]}")
    print("- + - + -")
    print(f"{xo_positions[3]} | {xo_positions[4]} | {xo_positions[5]}")
    print("- + - + -")
    print(f"{xo_positions[6]} | {xo_positions[7]} | {xo_positions[8]}")

# Get a play.
def get_play():
    """This function gets an position that is being played on.
    
    Parameters:
        none

    Return:
        play - the position that is being played on"""

    play = int(input("Choose a position to play on: "))

    return play - 1 

# Make sure the play is legal.
def verify_play(play, xo_positions):
    """This function verifies that the play is legal.
    
    Parameters:
        play - the play that is being verified
        xo_positions - the current state of the board to check against

    Return:
        verified - either true of false"""

    verified = True

    # The play will not be verified if there is already and x or o on the
    # position.
    if xo_positions[play] == "X" or xo_positions[play] == "O":
        verified = False

    return verified

# Apply the play to the positions list.
def edit_positions(player, play, xo_positions, x_positions, o_positions):
    """Change the position list according to the last play made.
    
    Parameters:
        player - determines either X or O
        xo_positions - the current state of the board
        
    Return:
        xo_positions - the updated state of the board"""

    # Add X for player 1, or add O for player 2.    
    if player == 1:
        xo_positions[play] = "X"
        x_positions.append(play)

    if player == 2:
        xo_positions[play] = "O"
        o_positions.append(play)

    return xo_positions, x_positions, o_positions

def determine_win(x_positions, o_positions):
    """This function determines if either x or o has a winning position.
    
    Parameters:
        x_position - a list of all of player 1's plays
        o_position - a list of all of player 2's plays
    
    Return:
        winner - the player that wins"""

    winner = False

    winning_positions = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 8],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
        ]

    x_positions.sort()
    o_positions.sort()
    

    for position in winning_positions:
        if x_positions == position:
            winner = True
        elif o_positions == position:
            winner = True

    return winner

main()