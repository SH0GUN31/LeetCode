"""
The problem Max consecutive ones can be easily solved by looping over the array once.
It can be classified under sliding window pattern.
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize variables to store counts
        count,max_count = 0,0
        # traverse through the array for matching ones and zeros
        for i in nums:
            if i==1:
                # increment the count when one
                count+=1
                # retain the maximum of counts to obtain max_count
                max_count=max(count,max_count)
            else:
                # when zero, reset the counter
                count=0
        # return maximum ones observed
        return max_count
    
nums = [1,0,1,1,0,1]
solution = Solution()
answer = solution.findMaxConsecutiveOnes(nums)
print(answer)