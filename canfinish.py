class solution(object):
    def _hascycle(self,graph,course,seen,cashe):
        if course in cashe:
            return cashe[course]
        if course in seen:
            return True
        if course not in graph:
            return False
        seen.add(course)
        ret = False
        for neighbours in graph[course]:
            if self._hascycle(graph,neighbours,seen,cashe):
                ret = True
                break
        seen.remove(course)
        cashe[course] = ret
        return ret
        
        
    def canfinish(self,numcourses,prerequesites):
        graph = {}
        for prereque in prerequesites:
            if prereque[0] in graph:
                graph[prereque[0]].append(prereque[1])
            else:
                graph[prereque[0]] = [prereque[1]]
        
        for course in range(numcourses):
            if self._hascycle(graph,course,set(),{}):
                return False
            return True
        
#Driver function
print(solution().canfinish(2,[[1,0]]))
#True
print(solution().canfinish(2,[[1,0],[0,1]]))
#False