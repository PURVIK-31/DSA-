from itertools import combinations  

def probability_of_a(n, elements, k):  
    # Find all indices with 'a'  
    indices_a = [i for i, letter in enumerate(elements) if letter == 'a']  
    num_a = len(indices_a)  # number of indices with 'a'  
    num_not_a = n - num_a   # number of indices without 'a'  
    
    # Total possible combinations of selecting k indices out of n  
    total_combinations = sum(1 for _ in combinations(range(n), k))  
    
    # Favorable combinations: combinations of selecting all from non-'a' positions  
    if num_not_a >= k:  
        favorable_combinations = sum(1 for _ in combinations(range(num_not_a), k))  
    else:  
        favorable_combinations = 0  # If there are fewer non-'a' elements than k, this is zero  
    
    probability = 1 - (favorable_combinations / total_combinations)  
    return round(probability, 4)  

# Read input values  
n = int(input().strip())  
elements = input().strip().split()  
k = int(input().strip())  

# Compute and print the probability  
print(probability_of_a(n, elements, k))