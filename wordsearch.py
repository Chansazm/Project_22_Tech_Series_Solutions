class grid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def _searchright(self,index, word):
        for i in range(len(matrix)):
            if word[i] != self.matrix[index][i]:
                return False
        return True

    def _searchdown(self,index,word):
        for i in range(len(matrix)):
            if word[i] != self.matrix[i][index]:
                return False
        return True

    def wordsearch(self,word):
        for i in range(len(matrix)):
            if self._searchdown(i,word):
                return True
        for i in range(len(matrix)):
            if self._searchright(i,word):
                return True
            return False


# driver function
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'X', 'V', 'K'],
    ['A', 'X', 'B', 'K'],
    ['M', 'X', 'J', 'M'],
]
print(grid(matrix).wordsearch('FOAM'))
