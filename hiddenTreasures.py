#Hidden-Treasures by James Leahy, Bronwyn Conroy, Declan Moore and Eanna O' Donnchadha
#--------------------------------------------------------

from random import randrange

#creating an empty list where board will be created
board = []                                    

#--------------------------------------------------------

#User input for level
#Dictionary for the difficulty level / gameboard size
#Functions to create our board and choose a coordinate
def user_diff():
	diff = raw_input("Enter your difficulty; \n""Easy"", ""Medium"" or ""Hard"": ")
	diff = diff.lower()
	return diff

levels = { "easy" : 3, "medium" : 5, "hard" : 10}

diff = user_diff() 
#Calls function 'diff' for size = levels[diff]

while diff not in levels:
	diff = user_diff()
#tests if user did not enter easy, medium or hard and asks again until they do
	
size = levels[diff]
#consults dictionary for size of board according to level

for x in range(size):
    board.append(["-"] * size)

def print_board(board):
    for row in board:
        print " ".join(row)

#creates board


#--------------------------------------------------------

#Start - introducing game and displaying board

print "Ayyy matey!\nI've heard theres a hidden treasure on this island.\nHelp me find it on the map below and I'll give you Pieces o' eight!\nX marks the spot."
print_board(board)

def random_row(board):
    return randrange(0, len(board) - 1)

def random_col(board):
    return randrange(0, len(board[0]) - 1)

row = random_row(board) 
col = random_col(board) 
#--------------------------------------------------------

#Game Rules

turn = 5
for i in range(turn + 1):

    #only ask user to guess again if their turns are not used up
    if (i < turn) :
	print "Turn ", i + 1
    	#make board user friendly, row 0 is row 1
   	guess_row = int(raw_input("Guess Row:")) - 1	
    	guess_col = int(raw_input("Guess Col:")) - 1
    
    if guess_row == row and guess_col == col:
        print "Yo-ho-ho! That there be the booty I was lookin' for!"
	board[row][col] = "X"
	print_board(board)
	break 
	# drops out of the for loop because user guessed correct


    elif i == turn:
	print "Shiver me timbers - we best give it a rest for the day Matey!"
	# +1 to make coordinates uder friendly, not start at 0
	print "Correct row ", row + 1		
	print "Correct col ", col + 1
	board[row][col] = "X"
	print_board(board)
    else:
	# guess < 0 or guess > length of board - not on board
        if (guess_row < 0 or guess_row > size - 1) or (guess_col < 0 or guess_col > size - 1): 
            print "Avast - the blasted government have spies there, it's unsafe."
        elif(board[guess_row][guess_col] == "O" or board[guess_col][guess_row] == "O"):
            print "You guessed that one already, me hearty!"
        else:
            print "The booty is not here, keep searching!"
            board[guess_row][guess_col] = "O"        
        print_board(board)

    


