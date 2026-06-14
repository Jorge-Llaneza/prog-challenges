from bisect import bisect_left

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordDict.sort()

        checklist = [False] * len(s)

        return self.wordBreakWithChecklist(s, wordDict, checklist, 0)
    

    def wordBreakWithChecklist(self, s, wordDict, checklist, current_index):


        first_char_matchs = get_string_lengths_starting_with(wordDict, s[current_index])

        for match in first_char_matchs:
            
            if current_index + len(match) > len(s):
                continue

            if checklist[current_index + len(match) - 1]:
                continue

            comparison_failed = False
            for i in range(len(match)):
                if s[i+ current_index] != match[i]:
                    comparison_failed = True
                    break
            if comparison_failed:
                continue
            
            #we have a total match

            checklist[current_index + len(match) - 1] = True

            if current_index + len(match) == len(s):
                return True

            wordBroken = self.wordBreakWithChecklist(s, wordDict, checklist, current_index + len(match))
            if wordBroken:
                return True

        return False
        

# Ai generated helper function, I am too tired to program a binary search rigth now (already know how to do that)
def get_string_lengths_starting_with(sorted_strings, letter):
    """
    Finds all strings starting with `letter` in a sorted list
    and returns a list of their lengths.
    """
    if not sorted_strings or not letter:
        return []
    
    # Ensure we are looking for a single lowercase/uppercase target consistently
    letter = letter[0] 
    
    # Use binary search to find the first index where a string could start with this letter
    start_idx = bisect_left(sorted_strings, letter)
    
    lengths = []
    
    # Scan forward from the starting index until the prefix changes
    for i in range(start_idx, len(sorted_strings)):
        if sorted_strings[i].startswith(letter):
            lengths.append(sorted_strings[i])
        else:
            # Because the list is sorted, as soon as a string doesn't start with 
            # our letter, we know no other strings after it will either.
            break
            
    return lengths

# Example Executions
sol = Solution()

# Example 1
print(sol.wordBreak("leetcode", ["leet", "code"])) 
# Expected Output: True

# Example 2
print(sol.wordBreak("applepenapple", ["apple", "pen"])) 
# Expected Output: True

# Example 3
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) 
# Expected Output: False

print(sol.wordBreak("ccbb", ["bc","cb"])) 
# Expected Output: False


# Example 2
print(sol.wordBreak("ddadddbdddadd", ["dd","ad","da","b"])) 
# Expected Output: True