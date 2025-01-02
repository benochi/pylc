# Integer to Ancient Numeric System
# Medium

# An ancient numeric system uses a combination of symbols to represent numbers. The symbols and their values are:
# SYMBOL      VALUE
# A                 1
# B                  5
# C                 10
# D                 50
# E                  100
# F                  500
# G                 1000


# Here is a problem similar to the Roman numeral conversion problem:

# Problem: Integer to Ancient Numeric System
# An ancient numeric system uses a combination of symbols to represent numbers. The symbols and their values are:

# Symbol    Value
# A    1
# B    5
# C    10
# D    50
# E    100
# F    500
# G    1000
# The rules for constructing numbers in this system are as follows:

# If the value starts with 4 or 9, use a subtractive form:

# Example: 4 = "AB" (1 less than 5), 9 = "AC" (1 less than 10).
# Similarly, 40 = "CE", 90 = "CE", 400 = "EF", and 900 = "EG".
# Symbols representing powers of 10 (A, C, E, G) can appear consecutively up to 3 times. For example:

# 3 = "AAA"
# 30 = "CCC"
# 3000 = "GGG"
# Symbols for 5 (B, D, F) cannot appear consecutively. Instead, use subtractive forms if needed.

# Task:
# Given an integer 
# num
# num, convert it to its equivalent representation in this ancient numeric system.

# Examples

# 1.
# Input:
# num = 3749
# Output:
# "GGGFDCEAB"
# Explanation:
# 3000 = GGG
# 700 = FDCE (500 + 100 + 100)
# 40 = CE (10 less than 50

# 2.
# Input:
# num = 58
# Output:
# "DBBAA"
# Explanation:
# 50 = D
# 8 = BAAA (5 + 1 + 1 + 1)

# 3.
# Input:
# num = 1994
# Output:
# "GEGCEAB"
# Explanation:
# 1000 = G
# 900 = EG (100 less than 1000)
# 90 = CE (10 less than 100)
# 4 = AB (1 less than 5)

# Constraints
# 1 <= num <= 3999


def numeralConversion(num):
  value_to_symbol = [
        (1000, 'G'), (900, 'EG'), (500, 'F'), (400, 'EF'),
        (100, 'E'), (90, 'CE'), (50, 'D'), (40, 'CD'),
        (10, 'C'), (9, 'AC'), (5, 'B'), (4, 'AB'), (1, 'A')
    ]
  result = []
  
  for value, symbol in value_to_symbol:
    while num >= value:
      num -= value
      result.append(symbol)

  return "".join(result)

print(numeralConversion(1994)) #"GEGCEAB" 
print(numeralConversion(58))  #"DBAAA"
print(numeralConversion(3749)) #GGGFEECDAC"
