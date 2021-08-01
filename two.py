def twoStrings(s1, s2):
    flag = False
    for i in range(len(s1)-1):
        for j in range(len(s2)-1):
            if s1[i] == s2[j]:
                flag = True
    if flag is True:
        print('YES')
    
    else:
        print('No')
    flag = False
    return None


#print(twoStrings('aba', 'cba'))
print(twoStrings('aba', 'xyz'))
