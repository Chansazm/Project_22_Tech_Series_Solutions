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

                
print(ispalindrome('wow'))
print(simplePalindrome('wow'))