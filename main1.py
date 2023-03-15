# Task
# The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<n, print i** .
#
# Example
# n=3
#
# The list of non-negative integers that are less than n=3  is [0, 1, 2,] . Print the square of each number on a separate line.

# n = int(input(">>>>"))
# for i in range(n):
#     print(i * i)

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#
# In the Gregorian calendar, three conditions are used to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
#
# Task
# #
# # Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# #
# # Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
#
#
# def is_leap(year):
#     leap = False
#
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#     return leap
#
#
# year = int(input('>>>'))
# print(is_leap(year))
#
# The included code stub will read an integer, n , from STDIN.
#
# Without using any string methods, try to print the following:
# 1, 2,3 ...n
#
# Note that "" represents the consecutive values in between.
#
# Example
# n=5
#
# Print the string 12345.
#
# if __name__ == '__main__':
#     n = int(input('>>>>>'))
#     for i in range(1, n+1):
#         print(i, end="")




# List Comprehensions

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
if __name__ == '__main__':
    x = int(input('>>'))
    y = int(input('>>>'))
    z = int(input('>>>>'))
    n = int(input('>>>>>'))
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print (ans)
