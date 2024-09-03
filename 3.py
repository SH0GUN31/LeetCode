"""
The problem longest substring without repeating characters can be easily solved using
the sliding window approach.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialize the variables to store start pointer and the target
        start,max_length=0,0
        # create an index to store character index for determining the start pointer
        char_index_map = {}
        # run a loop on enumerated string to acquire indices along with respective values
        for end,char in enumerate(s):
            """
            This condition is to check the string value is already seen or not. If seen and if it
            is within our context window update the start pointer to the right side of last seen
            character. 
            """
            if char in char_index_map and char_index_map[char]>=start:
                start=char_index_map[char]+1
            # assign or update the index to the charecter at hand
            char_index_map[char]=end
            # "end" variable is used for simplified understanding of the index part of string in this approach
            # calculate the maximum between max_length and length of the window containing unique substring
            max_length = max(max_length,end-start+1)
        
        return max_length
    
s = "pwwkew"
answer = Solution().lengthOfLongestSubstring(s)
print(answer)

"""
Time Complexity:
-> O(n) where n is length of the string, we traverse through the string only once.

Space Complexity:
-> O(min(m,n)), where m is the size of character index map.
"""