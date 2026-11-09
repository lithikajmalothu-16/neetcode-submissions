class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number using a hash map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Create "buckets" where the index represents frequency.
        # Since max frequency can be at most len(nums), we create len(nums) + 1 empty buckets.
        #index is the value, the nums in buckets    represent their frequencies. 
        freq = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        # Step 3: Collect the top k elements by iterating backwards from the highest frequency
        #The moment our result list hits the target size (len(res) == k), we immediately return res—we have found all $k$ most frequent elements and don't need to check the remaining lower-frequency buckets
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res