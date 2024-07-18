# Time Complexity : O(n!)
# space complexity : O(m*n)

# Approach :

#  we solve using backtracking
#  a attacking queen should be checked in three directions.
# one by checking the rows previous to current position with the same column
# two by decrementing row and col from present location ( diagonal).
# three by incrementing row and col from present location ( diagonal)
# we mark true initially if a queen suits the location else make it false
# through backtracking we find all possible locations of the queen in the grid

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []
        if not n:
            return [[""]]

        self.recurse(0)
        return self.solutions

    def isSafe(self, rowVal, colVal):

        rowCheck = rowVal-1
        colCheck = colVal

        while rowCheck >= 0 and colCheck >= 0:

            if self.grid[rowCheck][colCheck] == True:
                return False

            rowCheck = rowCheck-1

        diagRowCheck = rowVal-1
        diagColCheck = colVal-1

        while diagRowCheck >= 0 and diagColCheck >= 0:

            if self.grid[diagRowCheck][diagColCheck] == True:
                return False

            diagRowCheck = diagRowCheck-1
            diagColCheck = diagColCheck-1

        diagRowCheck = rowVal-1
        diagColCheck = colVal+1

        while diagRowCheck >= 0 and diagColCheck < len(self.grid[0]):

            if self.grid[diagRowCheck][diagColCheck] == True:
                return False

            diagRowCheck = diagRowCheck-1
            diagColCheck = diagColCheck+1

        return True

    def recurse(self, row):

        sol = []
        if row == len(self.grid):

            for i in range(len(self.grid)):
                rowString = ""
                for j in range(len(self.grid[0])):
                    if self.grid[i][j] == True:
                        rowString += "Q"
                    else:
                        rowString += "."
                sol.append(rowString)

            self.solutions.append(sol)

            return

        for i in range(len(self.grid[0])):

            if self.isSafe(row, i):

                self.grid[row][i] = True
                self.recurse(row+1)
                self.grid[row][i] = False
