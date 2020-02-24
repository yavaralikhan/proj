import numpy as np
chessboard = np.zeros((8, 8), dtype=int)
#print(chessboard)
chessboard[1::2, ::2] = 1
chessboard[::2, 1::2] = 1
#print(chessboard)
indexes = []
for i in range(0, len(chessboard)):
    print("Where would you like to place the queen?".format(i+1))
    i = int(input("Enter row position"))
    j = int(input("enter col position"))

    if (i >= 0 or i <= 7) and (j >= 0 or i <= 7):
        chessboard[i][j] = 5
    else:
        print("Enter valid choice")

    indexes.append([i, j])
    print("!!!!!!!!!!!!!!!!!!!!")
    print(chessboard)
    print(indexes)