from typing import List
from functools import lru_cache
import copy

def get_maximum_charge(charge: List[int]) -> int:
    # Convert list to tuple for hashable state in memoization
    charges = tuple(charge)
    
    @lru_cache(None)
    def simulate(curr_charges: tuple) -> int:
        if len(curr_charges) == 1:
            return curr_charges[0]
        
        max_charge = float('-inf')
        
        # Try removing each system except first and last
        for i in range(len(curr_charges)):
            # Create new state after removal and combination
            new_charges = list(curr_charges)
            
            # If not leftmost or rightmost, combine neighbors
            if 0 < i < len(curr_charges) - 1:
                combined_charge = curr_charges[i-1] + curr_charges[i+1]
                new_charges = new_charges[:i-1] + [combined_charge] + new_charges[i+2:]
            # If leftmost, just remove it
            elif i == 0:
                new_charges = new_charges[1:]
            # If rightmost, just remove it
            else:
                new_charges = new_charges[:-1]
            
            # Recursive call with new state
            result = simulate(tuple(new_charges))
            max_charge = max(max_charge, result)
        
        return max_charge
    
    return simulate(charges)

# Test function
def test_maximum_charge():
    # Test case from problem
    test1 = [-2, 4, 3, -2, 1]
    assert get_maximum_charge(test1) == 4
    
    # Additional test cases
    test2 = [-1,1,2,3,4,5,-8,-9,10]
    test3 = [-1, 1, -1, 1]
    test4 = [1, 2, 3]
    
    print("Test 1:", get_maximum_charge(test1))  # Should print 4
    print("Test 2:", get_maximum_charge(test2))
    print("Test 3:", get_maximum_charge(test3))
    print("Test 4:", get_maximum_charge(test4))

if __name__ == "__main__":
    test_maximum_charge()