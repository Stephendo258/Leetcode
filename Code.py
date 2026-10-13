// 49- Group Anagrams

from collections import defaultdict
from typing import List 

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(List)

        for word in strs: 
            counts = [0]*26

            for char in word:
                index = ord(char) - ord("a")
                counts[index] += 1
            
            key = tuple(counts)
            groups[key].append(word)
        
        return list(groups.values())

// Valid Sudoku

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                digit = board[r][c]

                if digit == ".":
                    continue

                keys = (
                    ("row", r, digit),
                    ("col", c, digit),
                    ("box", r // 3, c // 3, digit),
                )

                for key in keys:
                    if key in seen:
                        return false

                seen.update(keys)        

            return True       

// Longest Consecutive Sequence
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        best = 0

        for start in values: 
            if start - 1 in values:
                continue
            
            end = start
            while end in values:
                end += 1

                best = max(best, end - start)

            return best

// 4 SumII
from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],        
        nums3: List[int],        
        nums4: List[int],        
    ) -> int:

    pair_count = defaultdict(int)

    for a in nums1:
        for b in nums2:
            pair_count[a + b] += 1

    answer = 0

    for c in nums3:
        for d in nums4:
            needed = -(c + d)
            anser += pair_count.get(needed,0)

    return answer

// RandomizedSet
import random

class RandomizedSet:
    def _init_(self):
        self.values = [] # List
        self.position = {} # Dict 
 
    def insert(self, val: int) -> bool:
        if val in self.position:
            return false
        
        self.position[val] = len(self.values)
        self.values.append(val)
        return true

    def remove(self, val: int) -> bool:
        if val not in self.position:
            return false
        
        index = self.position[val]
        last = self.values[-1]

        self.values[index] = last
        self.position[last] = index

        self.values.pop()
        del self.postion[val]

        return true 

    def getRandom(self) -> int:
        return random.choice(self.values)