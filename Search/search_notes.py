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
### uses formula to pick position of guesses
## assumes elements in array are uniformly distributed
## ex: guess location of word in dictionary using order of alphabet
## small data sets or not evenly distributed => binary can be better
## time complexity = O(log( log(n) )) to O(n)
## space complexity = O(1)

#ADVANCED

# JUMP ~~sorted~~
## compromise between linear and binary
## jumps ahead at fixed intervals (square root of array's length) and perform linear search in interval
## simpler than binary, improve on linear
## efficient: data set too large for linear, not structured or large enough for binary

# FIBONACCI ~~sorted~~
## breaks into various subarrays based on fibonacci numbers
## key: size of array unknown or unbounded
## can be more efficient on average than binary

# EXPONENTIAL
## binary + jump
## rapidly expand range expnentially until find range, then binary search it
## unbounded or infinite array or with undetermined size
## looking for first occurence of value in array
## efficient: when element to be searched is closer to beginning (faster than binary)


#COMPARING
## best algorithm = depends
#depends on:
## nature of data (is it updated or altered frequently)
## type of data structure
    ## type of queries


