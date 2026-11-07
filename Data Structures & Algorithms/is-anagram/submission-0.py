class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # basic check : if lenghts don't match dont move forward
        if len(s) != len(t):
            return False
            
        countS = {}
        countT = {}

        # Bucket 1: Count letters in string s
        for char in s:
            countS[char] = countS.get(char, 0) + 1

        # Bucket 2: Count letters in string t
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        return countS == countT 

#return -> this compares the values saved in the countS and countT
