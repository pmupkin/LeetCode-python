#这道题实际上是找到大于给的排列组合，中的最小的排列组合序列，可以理解为给你一个数字，找到比他大
#但是又是比他大的数字中的最小值，而切组成这个数字的只能是给你提供的数字
#解题思想是，从后向前遍历，找到第一个不满足降序的元素，就比如说532，就是降序，254，就不是降序，此时5的位置就是找到的索引值
#如果找了一遍后，发现是一个完全降序，那么意味着这个排列组合是最大的，直接返回
#如果不是，那么将（比如说1254）2和它后面的字符串中比2大的第一个交换（这意味这2后面全是降序，第一个比二大，那么就是比二大的最小值）
#交换后，将索引2到最后的字符串从小到大排序，即可得到结果
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.sort()
            return 

        while j > i and nums[i-1] >= nums[j]:
            j -= 1
        nums[j] ,nums[i-1] = nums[i-1], nums[j]
        
        #排序子序列,实际上是反转
        l, r = i, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

        return 
        
            
            