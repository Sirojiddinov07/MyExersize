# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains . The second line contains an array   of  integers each separated by a space.
#
# Constraints
#
# Output Format

#
# n = int(input('>>'))
# arr = map(int, input('>>>').split())
# print(sorted(set(arr), reverse=True)[1])
#
#
#  Problem:-
#
#  There is a sentence that consists of space-separated strings of upper and lower case English letters. Transform each string according to the given algorithm and return the new sentence.
# Each string should be modified as follows:
# • The first character of the string remains unchanged
# • For each subsequent character, say x, consider a letter
# preceding it, say y:
# • If y precedes x in the English alphabet, transform x to uppercase
# o If x precedes y in the English alphabet, transform x to lowercase
# If x and y are equal, the letter remains unchanged
#
# Example
#
# sentence = "cOOL dog"
# The first letters of both words remain unchanged. Then, for the word "COOL" the first "o" is made uppercase because the letter preceding it, "c", comes earlier in the alphabet. Next, the case of the second "O" is unchanged because the letter preceding is also "o", and finally the "L" is made lowercase because the letter preceding it, "O", comes later in the alphabet. The second word, "dOg", is transformed according to the same rules. Return the resulting sentence 'cool dog'.
#
# Function Description
#
# Complete the function transformSentence in the editor below. The function must return a string representing the resulting sentence.
#
# transformSentence has the following parameter(s): string sentence: the input sentence



import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
# #
#
# def transformSentence(sentence):
#     # Write your code here
#     sentence.strip()
#     res = ''
#     ind = 0
#     for x in sentence:
#         if(ind==0):
#             res+= x
#             ind+=1
#         elif(x == ' '):
#             res += x
#             ind+=1
#         else:
#             y = sentence[ind-1]
#             if(y==' '):
#                 res+= x
#                 ind+=1
#             elif(y.lower() < x.lower()):
#                 res += x.upper()
#                 ind+=1
#             elif(y.lower()>x.lower()):
#                 res += x.lower()
#                 ind+=1
#             else:
#                 res+= x
#                 ind+=1
#     return res
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     sentence = input()
#
#     result = transformSentence(sentence)
#
#     fptr.write(result + '\n')
#
#     fptr.close()



# bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    word_list = sentence.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()