class solution(object):
    def push_dominoes(self,dominoes):
        forces = [0] * len(dominoes)
        max_force = len(dominoes)
        force = 0
        for i, d in enumerate(dominoes):
            if d == 'R':
                force = max_force
            elif d == 'L':
                force = 0
            else:
                force = max(0,force -1)
            forces[i] = force
        
        for i, d in enumerate(dominoes):
            if d == 'L':
                force = max_force
            elif d == 'R':
                force = 0
            else:
                force = max(0,force -1)
            forces[i] -= force
            
        Results = ''
        for f in forces:
            if f == 0:
                Results += '.'
            elif f > 0:
                Results += 'R'
            else:
                Results += 'L'
        return Results
              
                
               
#Driver function
print(solution().push_dominoes('R..L..RR'))