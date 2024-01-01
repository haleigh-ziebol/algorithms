# general
## break problems into similar sub problems
## solve subproblem only once, store results in table

# core principles
## overlapping subproblems (reoccur multiple times in process of solving - ex: fibonacci)
## optimal substructure (ex: shortest path problem in graph theory)

# implementation
    # memoization
    ## top-down approach, store results in cache, uses recursion
    ## checks for existing solution, lazy manner, memory efficient
    
    # tabulation
    ## bottom-up approach, stores results in table, uses iteration
    ## solves all sub-probs first, avoids recursion, space efficient (fewer function calls) and faster
