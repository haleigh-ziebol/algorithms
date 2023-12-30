def sum_numbers(n):
    if n <=1: #base case
        return n
    else: #recursive case
        return n + sum_numbers(n-1)

# result = sum_numbers(5)
# print(result)

#sum_numbers(1) -> 1 (fits base case)
#sum_numbers(2) 2 + 1 = 3
#sum_numbers(3) 3 + 3 = 6
#sum_numbers(4) 4 + 6 = 10
#sum_numbers(5) (1st call) -> 5 + 10 = 15


# tail recursion
def sum_numbers_tail(n, accumulator = 0):
    if n <= 0: #adjusted base case
        return accumulator
    else:
        return sum_numbers_tail(n-1, accumulator + n)
    
print(sum_numbers_tail(5))