# you have 2 crystal balls that will break if dropped from high enough distance, 
# determine the exact spot in which it will break in the most optimized way. 
# you cannot break both balls. 
import math 

def crystalBall(breaks):
    n = len(breaks)
    step = math.floor(math.sqrt(n))
    prev = 0

    # step until breaks[prev] hits a True value. 
    while prev < n and not breaks[prev]:
        prev += step

    # Second crystal ball: Linear search within the identified range
    start = max(0, prev - step + 1) #this goes back one prev, which was false, and start at the next index.
    for i in range(start, min(prev + 1, n)):
        if breaks[i]:
            return 1  # Return True when breaking point hit. could return i for index. 
    
    return -1



breaks = [False, False, False, False, True, True, True]
print(crystalBall(breaks))  # Output: 1
breaks = [False, False, False, False, False, False, True]
print(crystalBall(breaks))  # Output: 1

# Test Case 3: No breaking point
breaks = [False, False, False, False, False]
print(crystalBall(breaks))  # Output: -1

# Test Case 4: Breaking point at the beginning
breaks = [True, True, True, True, True]
print(crystalBall(breaks))  # Output: 1

# Test Case 5: Large input with breaking point near the end
breaks = [False] * 999 + [True] * 1
print(crystalBall(breaks))  # Output: 1