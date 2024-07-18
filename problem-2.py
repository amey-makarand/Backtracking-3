# Time Complexity : O(n * 4^(n)) for each character , 4 recursive calls are made
# space complexity : O(n), n is length of the word

# Approach :

#  we solve using backtracking and dfs
#  traverse the grid and start a backtrack call for that index
# search 4 directions which is up down left right and check if the character is found at that position
# if so initiaite a another backtrack following the same
# whenever we find the character at that location store in a temp variable and make that location as #
# return true only if the len of the word is equal to index
# else false


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.backtrack(board, word, 0, i, j):
                        return True

        return False

    def backtrack(self, board, word, index, rowInd, colInd):

        if index == len(word):
            return True

        if rowInd < 0 or rowInd == len(board) or colInd < 0 or colInd == len(board[0]) or board[rowInd][colInd] == "#":
            return False

        if word[index] == board[rowInd][colInd]:

            temp = board[rowInd][colInd]
            board[rowInd][colInd] = "#"

            for dirVal in self.dirs:

                rowTarget = dirVal[0] + rowInd
                colTarget = dirVal[1] + colInd

                if self.backtrack(board, word, index+1, rowTarget, colTarget):
                    return True

            board[rowInd][colInd] = temp

        return False
