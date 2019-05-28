""" You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct."""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jemCount = 0;
        
        for jewel in J:
            for stone in S:
                if stone == jewel:
                    jemCount += 1
                    
        return jemCount
        
""" Solution: For each jewel, we check to see if its present in our stone string. If the stone is a jewel, increment our jem count. Once finished, return the jem count found.

Because each letter in J is guaranteed distinct we avoid any redundant checks for duplicates. The best we can do here is an O(n^2) solution. 
"""
   
