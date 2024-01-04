#two sum
# calculate complement and look for it

# def twoSum(nums, target):
#     #create dictionary to store value and index
#     hashmap = {}
#     # iterate in array
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in hashmap:
#             return [hashmap[complement], i]
#         #store number and index in hashmap
#         hashmap[num] = i
#     return []

# print(twoSum([1,8,3,4,5], 7))