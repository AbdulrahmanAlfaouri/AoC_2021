import sys

with open("input.txt") as text:
    in_text = "".join(text.readlines())

ss = in_text.split("\n\n")
in_numbers = ss[0].split(",")
boards = [j.split("\n") for j in ss[1:]]


def main():
    b = 0
    for i in range(len(in_numbers)):
        b += 1
        chosenInputNumbers = in_numbers[0:b]

        for board in boards:
            bingoboard = BingoBoard()
            bingoBoardColumns = bingoboard.getBingoBoardColumns(board)
            rows = bingoboard.updateEmptyBoard(chosenInputNumbers, bingoBoardColumns)
            columns = bingoboard.getEmptyBoardRows()

            unMarkedNumbers = []

            if bingoboard.isWinnerBoard(rows, columns):
                print(bingoBoardColumns)
                print(columns)
                for column in bingoBoardColumns:
                    for cellNumber in column:
                        unMarkedNumbers.append(cellNumber)

                # for part2 uncomment this
                # for inNumber in slice:
                #     if inNumber in bingcolumnsnNumbers:
                #         bingcolumnsnNumbers.remove(inNumber)


                theSum = 0
                for unmarkedNumber in unMarkedNumbers:
                    theSum += int(unmarkedNumber)

                # for part2 uncomment this
                # boards.remove(board)

                print(
                f"""This is the Winner Board !! ,
                the sum of unmarked numbers is {theSum} ,the winning number is {chosenInputNumbers[-1]}, 
                the final score is {theSum * int(chosenInputNumbers[-1])}
                """
                )

                # for part2 comment this
                sys.exit()


class BingoBoard:
    def __init__(self):
        self.boardColumns = None
        self.emptyBoardRows = []

        self.emptyBoardColomns = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
        ]

        self.unmarkedNumbers = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
        ]

    def getBingoBoardColumns(self, current_board):
        self.boardColumns = [b1.split() for b1 in current_board]
        return self.boardColumns

    def getEmptyBoardRows(self):

        for num in range(len(self.emptyBoardColomns)):
            self.emptyBoardRows.append([])
            for jj in range(len(self.emptyBoardColomns)):
                self.emptyBoardRows[num].append(self.emptyBoardColomns[jj][num])
        return self.emptyBoardRows

    def updateEmptyBoard(self, in_numbers_slice, board):
        emtpyBoardColumns = self.emptyBoardColomns

        for num1, (j, k) in enumerate(zip(board, emtpyBoardColumns)):
            for hh in in_numbers_slice:
                if hh in board[num1]:
                    # update the empty board with the matched numbers in the same position in the board
                    emtpyBoardColumns[num1][board[num1].index(hh)] = emtpyBoardColumns[num1][board[num1].index(hh)].replace("", hh)

        return emtpyBoardColumns

    @staticmethod
    def isWinnerBoard(rows, columns):
        for rowOrcolumn in (rows, columns):
            for numAndcell in enumerate(rowOrcolumn):
                winningCondition = True
                for cell in rowOrcolumn:
                    # it's a losing row or column if even one cell  = ''
                    if cell[numAndcell[0]] == "":
                        winningCondition = False

                if winningCondition:
                    return True


if __name__ == "__main__":
    main()
