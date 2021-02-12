
'''
def sez(x):
    sum=0
    for i in range (1,10):
        sum=x+i
    return sum 


print (sez(1))
'''

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    ans = []
    for i in nums: 
        for j in nums:
            if (i !=j && i >j):
                ans.append(j)
            j=i+1
        i=i+1
    return ans
                
