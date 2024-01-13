
## two strings s and t, return min window in s which will contain all characters in t; if no window exists, return empty string

from collections import Counter
def minWindow(s, t):
    if not t or not s:
        return ""
    ## dictionary to keep count of all unique char in t
    dict_t = Counter(t)

    # number unique char in t, which need to be in desired window
    required = len(dict_t)

    # l and right pointer
    l,r = 0,0

    #formed used to keep track of how many unique char in t
    ## are present in current window in its desired frequency

    # dictionary which counts all unique char in current window
    window_counts = {}

    # (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):
        #Add on char from right to window
        character = s[r]
        window_counts[character] = window_counts.get(character,0) + 1

        #if frequency of current char added equals desired count in t, then increment formed count by 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

            # keep expanding window once we are done contracting
            r += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
    

    
    
    
    
    
    
    
    
    
    ## start index of potential window on first occurence of a char in t (store position as start)
    ## then loop through remaining
    ## end when char all found (store position of last char as end)
    ## compare length of substring to next