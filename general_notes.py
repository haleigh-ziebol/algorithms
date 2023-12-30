# Intro to Algs

# characteristics - 
## correctness (produces correct output for valid input)    ## efficiency (accomplish task switfly with minimal resource use)
## simplicity (straighforward, avoids unnecessary complexity, easier to maintain and modify)
    
# recursion -
## break problem down into smaller instances of same problem -- eventually arrive at solution

# parts-
## base case - stops recursion, stopping criteria for alg, must be clearly defined
## recursive case - function calls itself for smaller subset of original prob, moves close to base case, core of function where problem solving occurs
## call stack - LIFO, the last will be the base case!, each return pops a frame off the stack

# errors -
## stack overflow- missing or incorectly defined base case, function keeps calling itself until call stack runs out of space
## must return result at each step

#advantages-
## simplicity in problem solving
## clear and concise code (can eliminate need for complex loops)

#disadvantages-
## higher memory usage
## potential for stack overflow - function calls itself too many times before reaching base case
## can be slower than iterative; overhead associated with each function call to set up stack
## sometimes can calculate same result multiple times

#tail recursion -
##recursive call is very last operation performed
## performs all processing and arrives at final result before making recursive call; no pending operations after
## current function state does not need to be maintained
## can be more efficient, compiler can optimize
## simplified stack mgmt, each call does not depend on result of another