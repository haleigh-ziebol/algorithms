


def twoSum(nums, target):
    # Create a dictionary to store the value and its index
    hashmap = {}
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            # If the complement is found, return the indices
            return [hashmap[complement], i]
        # Store the number and its index in the hashmap
        hashmap[num] = i
    return []

# Example call to the function
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
# Print the result
print("Function twoSum Output:", result)

def isAnagram(s, t):
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

result = isAnagram("listen", "silent")
print("Function isAnagram Output:",result)  

from collections import Counter
def minWindow(s, t):
    if not t or not s:
        return ""

    # Dictionary to keep a count of all the unique characters in t
    dict_t = Counter(t)

    # Number of unique characters in t, which need to be present in the desired window
    required = len(dict_t)

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t
    # are present in the current window in its desired frequency
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window
    window_counts = {}

    # (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window
            l += 1    

        # Keep expanding the window once we are done contracting
        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

s = "ADOBECODEBANC"
t = "ABC"
result = minWindow(s,t)
print("Function minWindow Output:",result)