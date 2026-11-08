class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        # 1. Create a dictionary where every new key automatically starts with a blank list []
        ans = defaultdict(list)
        
        # 2. Loop through every single word in the input list
        for s in strs:
            # 3. Create a counting bucket of 26 zeros (one for each letter 'a' through 'z')
            count = [0] * 26
            
            # 4. Count how many times each letter appears in the current word
            for c in s:
                #Subtracting ord('a') is just a clean mathematical trick to map any lowercase letter to its exact position in the alphabet (0 through 25) so it fits neatly into our counting slot
                count[ord(c) - ord('a')] += 1
            
            # 5. Using the tuple version of our 26-number count as the dictionary key, 
            # and append the original word into its matching group list 
            # tuple is hashable whereas list isn't
            ans[tuple(count)].append(s)
            
        # 6. Extract all the grouped lists from our dictionary and return them
        return list(ans.values())