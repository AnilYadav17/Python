def flps(s):
    n = len(s)
    if n <= 1:
        return "Not Found"
    
    lps = [0] * n
    length = 0
    i = 1
    
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    ans = lps[-1]
    if ans == 0:
        return "Not Found"
    return s[:ans]

if __name__ == "__main__":
    import sys
    input_str = sys.stdin.read().strip()
    if input_str:
        print(flps(input_str))