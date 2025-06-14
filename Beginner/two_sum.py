# 1. Two Sum
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

num = [5,9,6,2,3,4]
target = 15

#Bruteforce
# def two_sum(num, target):
#     for i in range(len(num)):
#         for j in range(i +1, len(num)):
#             if num[i] + num[j] == target:
#                 return [i, j]
            
# print (two_sum([5,9,6,2,3,4], 8))


#Hashmap
def hash(num, target):
    hashmap= {}
    for i, num in enumerate(num):
        j = target - num
        if j in hashmap:
            return [hashmap[j], i]
        hashmap[num] = i
    return []

print (hash([5,9,6,2,3,4], 8))


        

        
