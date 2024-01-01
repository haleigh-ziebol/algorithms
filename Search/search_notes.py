# definition
## method to find item or its position in data structure


# LINEAR
## sequentially checking elements until you find match or search all
## time complexity = O(1) to O(n) usually closer to O(n)
## space complexity = O(1)


# BINARY  ~~sorted~~
## compare target value to middle element in **sorted** array
### split array in half if not equal, decide which half to search
### end when subarray size is 0
## time complexity = O(log(n)) (cutting n in half til it reaches n)
## space complexity = O(1)


# INTERPOLATION ~~sorted~~
## interpolate values to find a specific key in a sorted array
## assumes elements in array are uniformly distributed
## ex: guess location of word in dictionary using order of alphabet
## small data sets or not evenly distributed => binary can be better
