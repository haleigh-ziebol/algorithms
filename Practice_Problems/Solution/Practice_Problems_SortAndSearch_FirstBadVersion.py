def isBadVersion(version):
    return version >= 4

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Test the function with 5 versions
n = 5
print("First Bad Version:", firstBadVersion(n))  # Expected output: 4