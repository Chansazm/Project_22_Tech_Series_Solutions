class solution(object):
    def push_dominoes(self,dominoes):
        forces = [0] * len(dominoes)
        max_force = len(dominoes)
        for i, d in dominoes:
            if d == 'R':
                force = max_force
            elif d == 'L':
                force = 0
            else:
                force = max(0,force -1)
            forces[i] = force
                
                
                
                
#Driver function
print(solution.push_dominoes())