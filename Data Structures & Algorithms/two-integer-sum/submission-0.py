class Solution:
    def twoSum(self, nums:List[int],Target: int)->List[int]:
        seen = {}
        #enumerate provides us with key and value
        for i, j in enumerate(nums):
            diff = Target - j
            if diff in seen:
                #returning in a list both the indices
                return [seen[diff],i]
                #the value being saved alongside the key 
                # number j was found at index i.
            seen[j] =i 