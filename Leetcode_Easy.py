

# No.1672

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=[]
        for i in accounts:
            ans.append((i))
        return max(ans)




# No.1480
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        temp=0
        for i in nums:
            ans.append(i+temp)
            temp=i+temp
        return ans

'''

