class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n=len(nums)
        x =0
        while x<n-2:
            y=x+1
            z =n-1
            while(y<z):
                Sum =nums[x]+nums[y]+nums[z]
                if Sum ==0:
                    res.append([nums[x],nums[y],nums[z]])
                    x+=1
                elif Sum>0:
                    z -=1
                else:
                    y+=1
            x +=1
        return res
nums = [-1,0,1,2,-1,-4]
t = Solution()
print(t.threeSum(nums))