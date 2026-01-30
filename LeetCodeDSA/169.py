import math
from typing import List
def majorityElement(nums):
    pass    
print(majorityElement(nums = [2,2,1,1,1,2,2]))


def findGCD(s):
    count_vowel = 0
    count_consonant = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'o' or i == 'u':
            count_vowel += 1
        elif i.isalpha():
            count_consonant += 1
            print(i)
    return math.floor(count_vowel / count_consonant)if count_consonant > 0 else 0, count_consonant
print(findGCD(s= "io"))

