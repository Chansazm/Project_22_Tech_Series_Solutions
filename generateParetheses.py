class solution(object):

    def _generateHelper(self, n, left, right, str):
        if left + right == 2 * n:
            return [str]
        
        result = []
        if left < n:
            result += self._generateHelper(n, left + 1, right, str + '(')
            
        if right < left:
            result += self._generateHelper(n, left, right+1, str + ')')

        return result

    def generateParens(self, n):
        return self._generateHelper(n, 0, 0,'')
print(solution().generateParens(3))
#great
