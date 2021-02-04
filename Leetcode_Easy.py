

# No.1672
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=[]
        for i in accounts:
            ans.append((i))
        return max(ans)
'''



# No.1480
class Solution:
     def runningSum(self, nums: List[int]) -> List[int]:
         ans=[]
         temp=0
         for i in nums:
             ans.append(i+temp)
             temp=i+temp
         return ans


# No.136 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        for i in range (1,len(nums),2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            if nums[i+2] == len(nums):
                return nums[-1]

# No. 771 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count =count +1
        return count