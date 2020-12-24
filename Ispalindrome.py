from collections import defaultdict

def ispalindrome(str):
        count = defaultdict(int)
        pal = ''
        odd = ''
        for c in str:
            count[c] += 1
        for c, cnts in count.items():
            if cnts % 2 == 0:
                pal += c * (cnts // 2)
            elif odd == '':
                odd = c
                pal += c * (cnts // 2)
            else:
                return False
        return pal + odd + pal[::-1]
    
def simplePalindrome(str):
    if str[::-1] == str:
        return True
    else:
        return False

def palindrome(str):
    i = 0
    j = len(str) - 1
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True
            

                
#print(ispalindrome('wow'))
#print(simplePalindrome('wow'))
print(palindrome('wow'))