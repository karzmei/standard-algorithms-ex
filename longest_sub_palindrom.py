def grow_palindrom_odd(s: str):
    if len(s) == 0:
        return 0, ""
    else:
        exm = s[0]
    max_len = 1
    for i in range(1,len(s)-1):
        valid = True
        l = i-1
        r = i+1
        cur_max = 1
        while valid and (l>=0) and (r< len(s)):
            if ( s[l] != s[r] ) :
                valid = False
            else:
                cur_max += 2
                if cur_max > max_len:
                    max_len = cur_max
                    exm = s[l:r+1]
            l -= 1
            r += 1
    return max_len, exm

def grow_palindrom_even(s):
    if len(s) == 0:
        return 0, ""
    exm = ""
    min_nontriv_exm = ""
    max_len = 2
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            l = i-1
            r = i+2
            cur_max = 2
            min_nontriv_exm = s[i:i+2]
            valid = True
            while valid and (l>=0) and (r < len(s)):
                if s[l] != s[r] :
                    valid = False
                else:
                    cur_max += 2
                    if cur_max > max_len :
                        max_len = cur_max
                        exm = s[l:r+1]
                l -= 1
                r += 1
    if max_len == 2:
        exm = min_nontriv_exm
    return max_len, exm
    
    
def is_palindrome(s: str) -> bool :
    i = 0
    j = len(s) - 1
    valid = True
    while (i <= j):
        if s[i] != s[j]:
            valid = False
            break
        i += 1
        j -= 1
    return valid
    
def fixed_length_palindrom(s, w_len):
    # checks if there's a palindrom of fixed size, w_len, in s
    found = False
    exm = ""
    i = 0
    while (found == False) and (i < len(s) - w_len) :
        if is_palindrom(s[i:i+w_len]):
            found = True
            exm = s[i:i+w_len]
        i += 1
            
    return found, exm

    
def longest_palindrome(s: str) -> str:
    max_len_odd, exm_odd = grow_palindrom_odd(s)
    max_len_even, exm_even = grow_palindrom_even(s)
        
    if len(exm_odd) > len(exm_even):
        return exm_odd
    else:
        return exm_even
        
        
if __name__ == '__main__':
    s = 'ababaa'
    print(longest_palindrome(s))