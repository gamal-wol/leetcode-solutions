"""
LeetCode Problem: Merge Strings Alternately
Problem Link: https://leetcode.com/problems/merge-strings-alternately/
Solved: November 23, 2025
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings by alternating characters from each string.
        If one string is longer, append the remaining characters.
        
        Args:
            word1: First input string
            word2: Second input string
            
        Returns:
            Merged string with alternating characters
            
        Time Complexity: O(n + m) where n, m are lengths of word1, word2
        Space Complexity: O(n + m) for the result string
        """
        result = []
        max_len = max(len(word1), len(word2))
        
        for i in range(max_len):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
                
        return ''.join(result)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    word1 = "abc"
    word2 = "pqr"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Output: '{solution.mergeAlternately(word1, word2)}'")
    print()
    
    # Test case 2
    word1 = "ab"
    word2 = "pqrs"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Output: '{solution.mergeAlternately(word1, word2)}'")
    print()
    
    # Test case 3
    word1 = "abcd"
    word2 = "pq"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Output: '{solution.mergeAlternately(word1, word2)}'")
