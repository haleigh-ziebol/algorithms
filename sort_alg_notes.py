#resource mgmt, make data accessible, enhances the way software interacts with data

# alg operation types

##in place- rearranges elements within array without need for additional storage (or uses a small, constant amt of addtional storage space)
### ex: bubble, insertion, quick sorts
### maximizes available memory

## out of place- rearrange elements in additional space where copy of array (or significant amt of it) is stored
### ex: merge
### require more memory, creates stable algs - preserve relative order of equal elements


# stability - preservation of relative order of records with equal keys

## stable - preserved; unstable - not preserved

# BUBBLE
## repeatedly bubbles up largest element to correct position at end of array, 1 at a time
## time complexity: O(n^2) 
### ex: 10 records could require 100 operations

    # ex: [29, 10, 14, 37, 13]
    ## compare first two: 29, 10; 29 > 10 -> swap position to 10, 29
    ## then [10, 29, 14, 37, 13]
    ## compare next two: 29, 14; 29 > 14 -> swap til [10, 14, 29, 37, 13]
    ## 37> 13 so swap it to end; keep passing through

# SELECTION
## find smallest element in unsorted segment and swap with leftmost unsorted element
### moves boundary of unsorted segment one to right
## time complexite = O(n^2)
## space complexity= O(1)

# INSERTION
## insert element into correct order in sorted section
## time complexite = O(n^2)
## space complexity= O(1)

# MERGE   ~divide & conquer~
## breaks into smaller parts, then deal with separately and combine to solve
## time complexite = O(n log(n))
## space complexity= O(n)  additional space required for temporary arrays in process
