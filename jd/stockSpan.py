# The stock span problem is a financial problem where we have a series of daily price quotes for a stock denoted by an array arr[] 
# and the task is to calculate the span of the stock’s price for all days. The span arr[i] of the stock’s price on a given day i is 
# defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is 
# less than or equal to its price on the current day.

# Examples:

# Input: arr[] = [100, 80, 60, 70, 60, 75, 85]
# Output: [1, 1, 1, 2, 1, 4, 6]
# Explanation: Traversing the given input span 100 is greater than equal to 100 and there are no more elements behind it so the span is 1,
#  80 is greater than equal to 80 and smaller than 100 so the span is 1, 60 is greater than equal to 60 and smaller than 80 so the 
# span is 1, 70 is greater than equal to 60,70 and smaller than 80 so the span is 2 and so on.  Hence the output will be 1 1 1 2 1 4 6.


# Input: arr[] = [10, 4, 5, 90, 120, 80]
# Output: [1, 1, 2, 4, 5, 1]
# Explanation: Traversing the given input span 10 is greater than equal to 10 and there are no more elements behind it so the span is
#  1, 4 is greater than equal to 4 and smaller than 10 so the span is 1, 5 is greater than equal to 4,5 and smaller than 10 so the span 
# is 2,  and so on. Hence the output will be 1 1 2 4 5 1

#price <= currentDay

def stockSpan(prices):
  n = len(prices)
  res = [1] * n 
  stack = []
  
  for i in range(n):
    while stack and prices[i] >= prices[stack[-1]]:
      stack.pop()

    if stack:
      res[i] = i - stack[-1]
    else:
      res[i] = i + 1
    
    stack.append(i)
  return res

print(stockSpan([10, 4, 5, 90, 120, 80])) # [1, 1, 2, 4, 5, 1]
print(stockSpan([100, 80, 60, 70, 60, 75, 85])) #[1, 1, 1, 2, 1, 4, 6]
print(stockSpan([10, 4, 5, 6, 7, 4, 8, 9, 2])) # [1, 1, 2, 3, 4, 5, 1]