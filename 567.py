"""
The problem Permutation in a string is a classic case of sliding window pattern problem.
Although it is not a straight forward problem but easy to understand once you get the concept.
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # len(s1) should be smaller or equal to len(s2)
        if len(s1)>len(s2):
            return False
        
        """
        let us start by initializing the lists by 26 zeros corresponding to
        26 alphabets in english language.
        """
        s1_count = [0]*26
        s2_count = [0]*26
        """
        Now we create our first window by adding letter counts at their 
        corresponding indices for the window size of len(s1). 
        """
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1
        # loop over the range excluding previously considered window
        for i in range(len(s1),len(s2)):
            # check first to see if the first windows of s1 and s2 match
            if s1_count==s2_count:
                return True
            # add the count of incoming element in the new window
            s2_count[ord(s2[i])-ord('a')]+=1
            # subtract the count of outgoing element from the window
            s2_count[ord(s2[i-len(s1)])-ord('a')]-=1

        # check for the last window and return
        return s1_count==s2_count

s1 = "abc"
s2 = "cbadefabc"
answer = Solution().checkInclusion(s1,s2)
print(answer)

"""
Time Complexity:
-> It is O(n), where n is length of s2, because we iterate over s2 once.
Space Complexity:
-> It is O(1), this is beacause the space for storing 26 alphabet representations is constant.
"""