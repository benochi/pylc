def getMaximumCharge(charge):
    # Memoization to store computed results
    memo = {}
    
    def merge(arr):
        # Convert array to tuple for hashability in memoization
        arr_tuple = tuple(arr)
        
        # If result already computed, return memoized result
        if arr_tuple in memo:
            return memo[arr_tuple]
        
        # Base case: if only one system remains, return its charge
        if len(arr) == 1:
            return arr[0]
        
        # Track maximum charge achievable
        max_charge = float('-inf')
        
        # Try removing each system and merging neighbors
        for i in range(len(arr)):
            # Create a new list with the system removed
            new_arr = arr[:i] + arr[i+1:]
            
            # Merge neighbors if possible
            if i > 0 and i < len(new_arr):
                new_arr[i-1] += new_arr[i]
                new_arr.pop(i)
            
            # Recursively solve for the new configuration
            current_charge = merge(new_arr)
            max_charge = max(max_charge, current_charge)
        
        # Memoize and return result
        memo[arr_tuple] = max_charge
        return max_charge
    
    return merge(charge)


print(getMaximumCharge([3, -5, 4, -2, 6]))  # Expected: 13
print(getMaximumCharge([3, -4, 7, -5, 6]))  # Expected: 16
print(getMaximumCharge([2, -3, 6, -1, 8]))  # Expected: 16
print(getMaximumCharge([1, -7, 3, 3, -4, 9, -6]))  # Expected: 12
print(getMaximumCharge([5, -9, 2, 8, 1, -6]))  # Expected: 8
print(getMaximumCharge([5, -9, 2, 8, 1, 27]))  # Expected: 35



