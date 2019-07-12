#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        for i in range(len(nums)-1,0,-1): # 倒序循环，从最后一个元素循环到第一个元素。不能用正序循环，因为正序循环删除元素后后续的列表的长度和元素下标同时也跟着变了，len(alist)是动态的。
            
            
            if nums[i] == nums[i-1]:
                nums.pop(i) # 将index=i处的元素删除并return该元素。如果不想保存这个被删除的值只要不把alist.pop(i)赋值给变量就好，不影响程序运行。
        return len(nums)
