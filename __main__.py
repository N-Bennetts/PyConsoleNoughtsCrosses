# NAME:  __main__.py
# DOES:  Main executable.
# FROM:  PyConsoleNoughts+Crosses
# MADE:  v1.0, 09.Apr.2024, N-Bennetts
# FORM:  v1.0, 09.Apr.2024, N-Bennetts
# ===================================================================================================

# Import required modules.

import os, random

# SetupGame - Does pre-game setup.

def SetupGame():
    # 1 - Show logo.
    print("PYTHON CONSOLE -> NOUGHTS + CROSSES\nv1.0 by N-Bennetts\n\n")
    # 2 - Pick player mode.
    Valid = False
    while Valid != True:
        PlayerMode = input("\nWHO'S PLAYING?\n\n\t1 | HUMAN V HUMAN\n\t2 | HUMAN V COMPUTER\n\n? ")
        if PlayerMode == "1":
            PlayerMode = "H"
            Valid = True
        elif PlayerMode == "2":
            PlayerMode = "C"
            Valid = True
        else:
            print("Try again.\n")
            Valid = False
    # 3 - If against computer, player 1 gets to pick roles.
    if PlayerMode == "C":
        Valid = False
        while Valid != True:
            P1Role = input("\nPICK YOUR ROLE?\n\n\t1 | NOUGHT\n\t2 | CROSS\n\n? ")
            if P1Role == "1":
                P1Role = "N"
                P2Role = "C"
                Valid = True
            elif P1Role == "2":
                P1Role = "C"
                P2Role = "N"
                Valid = True
            else:
                print("Try again.\n")
                Valid = False
    else:
        P1Role = "N"
        P2Role = "C"
    # 4 - Pick who goes first.
    Valid = False
    while Valid != True:
        FirstMove = input("\nWHO GOES FIRST?\n\n\t1 | NOUGHT\n\t2 | CROSS\n\n? ")
        if FirstMove == "1":
            FirstMove = "N"
            Valid = True
        elif FirstMove == "2":
            FirstMove = "C"
            Valid = True
        else:
            print("Try again.\n")
            Valid = False
    # 5 - Confirm ready.
    print("\n\nGAME STARTING\n\n")
    # 6 - Set up game variables.
    global P1, P2, First, PlayMode, Array # Access outside is important.
    if P1Role == "N": # Roles and board marks.
        P1 = "O"
    if P1Role == "C":
        P1 = "X"
    if P2Role == "N":
        P2 = "O"
    if P2Role == "C":
        P2 = "X"
    if P1Role == FirstMove: # First mover.
        First = "P1"
    if P2Role == FirstMove:
        First = "P2"
    PlayMode = PlayerMode # Is computer P2?
    Array = { "A1" : ".", "A2" : ".", "A3" : ".", "B1" : ".", "B2" : ".", "B3" : ".", "C1" : ".", "C2" : ".", "C3" : "."}
    return True

# PlayGame - Handles play session.

def PlayGame():
    if First == "P1":
        LastKnownTurn = "P2"
    if First == "P2":
        LastKnownTurn = "P1"
    Done = False
    PossibleMoves = ["", "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    Turn = 1
    while Done != True:
        # 1 - Show the game for the first time.
        print("\n -- TURN: " + str(Turn) + " --\n")
        print("\n\n +-----------+\n" + f' | {Array["A1"]} | {Array["A2"]} | {Array["A3"]} |\n | {Array["B1"]} | {Array["B2"]} | {Array["B3"]} |\n | {Array["C1"]} | {Array["C2"]} | {Array["C3"]} |' +"\n +-----------+\n\n")
        # 2 - Allow whoever's turn to occur and have impact.
        if LastKnownTurn == "P1":
            # We're P2, and could be human or computer.
            if PlayMode == "C":
                # We're a computer.
                print("COMPUTER IS THINKING...")
                PickedValidMove = False
                while PickedValidMove != True:
                    Move = PossibleMoves[random.randint(1,9)]
                    if Array[Move] == ".":
                        Move = Move
                        PickedValidMove = True
                    else:
                        PickedValidMove = False
                Array[Move] = P2
                LastKnownTurn = "P2"
            elif PlayMode == "H":
                # We're a human.
                Valid = False
                while Valid != True:
                    Move = input("PLAYER 2 - YOUR MOVE CAN BE A1/A2/A3/B1/B2/B3/C1/C2/C3 (TOP-TO-BOTTOM)\n\n? ").upper()
                    if len(Move) > 0 and Move in PossibleMoves and Array[Move] == ".":
                        Move = Move
                        Valid = True
                    else:
                        print("Try again.")
                        Valid = False
                Array[Move] = P2
                LastKnownTurn = "P2"
        elif LastKnownTurn == "P2":
            # We're P1, and only human,
            Valid = False
            while Valid != True:
                Move = input("PLAYER 1 - YOUR MOVE CAN BE A1/A2/A3/B1/B2/B3/C1/C2/C3 (TOP-TO-BOTTOM)\n\n? ").upper()
                if len(Move) > 0 and Move in PossibleMoves and Array[Move] == ".":
                    Move = Move
                    Valid = True
                else:
                    print("Try again.")
                    Valid = False
            Array[Move] = P1
            LastKnownTurn = "P1"
        # 3 - Show the game for the second time, counting that turn.
        print("\n\n +-----------+\n" + f' | {Array["A1"]} | {Array["A2"]} | {Array["A3"]} |\n | {Array["B1"]} | {Array["B2"]} | {Array["B3"]} |\n | {Array["C1"]} | {Array["C2"]} | {Array["C3"]} |' +"\n +-----------+\n\n")
        # 4 - Evaluate if either player has won or not, and if so, say that and then continue.
        Turn = Turn + 1
        Summary = str(" " + Array["A1"] + Array["A2"] + Array["A3"] + Array["B1"] + Array["B2"] + Array["B3"] + Array["C1"] + Array["C2"] + Array["C3"])
        WinConditionMet = ""
        if str(Summary[1] + Summary[2] + Summary[3]) == "OOO":   # NOUGHT has HORZ LINE 1.
            WinConditionMet = "O"
        elif str(Summary[1] + Summary[2] + Summary[3]) == "XXX": # CROSS has HORZ LINE 1.
            WinConditionMet = "X"
        elif str(Summary[4] + Summary[5] + Summary[6]) == "OOO": # NOUGHT has HORZ LINE 2.
            WinConditionMet = "O"
        elif str(Summary[4] + Summary[5] + Summary[6]) == "XXX": # CROSS has HORZ LINE 2.
            WinConditionMet = "X"
        elif str(Summary[7] + Summary[8] + Summary[9]) == "OOO": # NOUGHT has HORZ LINE 3.
            WinConditionMet = "O"
        elif str(Summary[7] + Summary[8] + Summary[9]) == "XXX": # CROSS has HORZ LINE 3.
            WinConditionMet = "X"
        elif str(Summary[1] + Summary[4] + Summary[7]) == "OOO": # NOUGHT has VERT LINE 1.
            WinConditionMet = "O"
        elif str(Summary[1] + Summary[4] + Summary[7]) == "XXX": # CROSS has VERT LINE 1.
            WinConditionMet = "X"
        elif str(Summary[2] + Summary[5] + Summary[8]) == "OOO": # NOUGHT has VERT LINE 2.
            WinConditionMet = "O"
        elif str(Summary[2] + Summary[5] + Summary[8]) == "XXX": # CROSS has VERT LINE 2.
            WinConditionMet = "X"
        elif str(Summary[3] + Summary[6] + Summary[9]) == "OOO": # NOUGHT has VERT LINE 3.
            WinConditionMet = "O"
        elif str(Summary[3] + Summary[6] + Summary[9]) == "XXX": # CROSS has VERT LINE 3.
            WinConditionMet = "X"
        elif str(Summary[1] + Summary[5] + Summary[9]) == "OOO": # NOUGHT has NW/>SE STRIKE.
            WinConditionMet = "O"
        elif str(Summary[1] + Summary[5] + Summary[9]) == "XXX": # CROSS has NW/>SE STRIKE.
            WinConditionMet = "X"
        elif str(Summary[3] + Summary[5] + Summary[7]) == "OOO": # NOUGHT has NE</SW STRIKE.
            WinConditionMet = "O"
        elif str(Summary[3] + Summary[5] + Summary[7]) == "XXX": # CROSS has NE</SW STRIKE.
            WinConditionMet = "X"
        if WinConditionMet == P1:
            input("\nPLAYER 1 WINS!\n\n")
            Done = True
        if WinConditionMet == P2:
            input("\nPLAYER 2 WINS!\n\n")
            Done = True
        # 5 - Evaluate if nothing more can be done - if so, call a draw, and then validate exit/restart.
        if Summary.count(".") < 1:
            print("DRAW.\n\n")
            Done = True

# Core program loop.

while True:
    if SetupGame() == True:
        PlayGame()
        pass
    continue

# End.
