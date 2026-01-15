from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        sequences = []
        for n in nums:
            if n-1 in nums:
                continue
            else:
                length = 1
                while True:
                    if n+1 in nums:
                        length += 1
                        n += 1

                    else:
                        break
                sequences.append(length)
        if sequences == []:
            return 0
        return max(sequences)