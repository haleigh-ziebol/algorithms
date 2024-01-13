## time complexity O(N log(N)), space complexity O(1)
def valid_anagram(string1, string2):
    str1 = ''.join(sorted(string1.lower()))
    str2 = ''.join(sorted(string2.lower()))
    ## check if equivalent
    if str1 == str2:
        return "true"
    else:
        return "false"
    
## time complexity O(N), space complexity O(1)
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in t:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False
        else:
            return False
    return True