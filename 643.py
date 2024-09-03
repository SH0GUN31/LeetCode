""" 
The problem Maximum average subarry 1 can be easily solved by the sliding
window approach.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # initialize the sum of first k elements
        current_sum = float(sum((nums[:k])))
        # initialize variable to store maximum sum
        max_sum = current_sum
        # iterate over the remaining elements of the list
        for i in range(k,len(nums)):
            # as we slide the window add next element and subtract first element
            current_sum += nums[i] - nums[i-k]
            # store the maximum sum
            max_sum = max(max_sum,current_sum)
        # return the average
        return max_sum/k
    
nums = [1,12,-5,-6,50,3] 
k = 4
solution = Solution()
answer = solution.findMaxAverage(nums=nums,k=k)
print(answer)

"""
Time Complexity:
    -> Initializing the sum for the first window takes O(k).
    -> Sliding the window accross the rest of the array takes O(n-k).
    -> The overall time complexity becomes O(n), where n is len(nums).
    
Space Complexity:
    -> The algorithm takes constant amount of extra space regardless of input size.
    -> Therefore, space complexity becomes O(1).
"""