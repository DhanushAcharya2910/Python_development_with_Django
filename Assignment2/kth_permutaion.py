import math

def find_kth_permutation(numbers, k):
    n = len(numbers)
    
    if k < 1 or k > math.factorial(n):
        return None  
    
    k -= 1  
    result = []
    
    while n > 0:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        result.append(numbers.pop(index))
    
    return result


numbers = [1, 2, 3]
k = 3

kth_permutation = find_kth_permutation(numbers, k)

if kth_permutation is not None:
    print(f"The {k}-th permutation is: {kth_permutation}")
else:
    print(f"Invalid value of k.")
