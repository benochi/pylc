# Temperature Trend Span
# Medium
# Given an array temps[] where each element represents the daily temperature of a city, calculate the trend span for each day. 
# The trend span of the temperature on a given day
#  𝑖 is defined as the maximum number of consecutive days just before 𝑖 (including day 𝑖) for which the temperature was greater than or 
# equal to the temperature on day 𝑖.

# Example 1
# Input:
# temps = [73, 71, 70, 74, 75, 72, 76]

# Output:
# [1, 1, 1, 4, 5, 1, 7]

# Explanation:

# Day 1 (73): Trend span = 1 (Only itself).
# Day 2 (71): Trend span = 1 (Only itself).
# Day 3 (70): Trend span = 1 (Only itself).
# Day 4 (74): Trend span = 4 (Days [70, 71, 73, 74]).
# Day 5 (75): Trend span = 5 (Days [70, 71, 73, 74, 75]).
# Day 6 (72): Trend span = 1 (Only itself).
# Day 7 (76): Trend span = 7 (All previous days and itself).


# Example 2
# Input:
# temps = [50, 60, 55, 65, 70, 60]

# Output:
# [1, 2, 1, 4, 5, 1]

# Explanation:

# Day 1 (50): Trend span = 1.
# Day 2 (60): Trend span = 2 (Days [50, 60]).
# Day 3 (55): Trend span = 1 (Only itself).
# Day 4 (65): Trend span = 4 (Days [50, 55, 60, 65]).
# Day 5 (70): Trend span = 5 (Days [50, 55, 60, 65, 70]).
# Day 6 (60): Trend span = 1 (Only itself).


# Constraints
# 1<= len(temps) <= 10^5
# -100 <= temps[i] <= 100

def Temp(temps):
  output = [1] * len(temps)
  highest = temps[0]
  for i in range(1, len(temps)):
    if temps[i] >= highest:
      output[i] = i + 1
      highest = temps[i]
    elif temps[i - 1] and temps[i] > temps[i - 1]:
      j = i - 1
      midCount = 1
      while temps[j] and temps[i] and temps[i] >= temps[j]:
        midCount += 1
        j -=1
      output[i] = midCount
        
  return output
      
print(Temp(temps = [73, 71, 70, 74, 75, 72, 76])) #[1, 1, 1, 4, 5, 1, 7]
print(Temp(temps = [50, 60, 55, 65, 70, 60])) # [1, 2, 1, 4, 5, 1]
print(Temp(temps = [73, 70, 72, 74, 75, 7, 8, 19, 73, 74, 80])) #[1, 1, 2, 4, 5, 1, 2, 3, 4, 5, 11]
print(Temp(temps = [73, 73, 73])) #1,2,3