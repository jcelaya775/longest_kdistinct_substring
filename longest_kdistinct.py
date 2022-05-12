class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    @time complexity: O(n)
    @space complexity: O(1)
    """

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        start = 0
        maxLen = 0
        charCounts = [0 for i in range(256)]

        # grow window
        for end in range(len(s)):
            charCounts[ord(s[end])] += 1

            # shrink window
            while start < len(s) and charCounts[ord(s[end])] > k:
                charCounts[ord(s[start])] -= 1
                start += 1

            # print(f"start: {start}, end: {end}")
            if (end - start + 1) > maxLen:
                print(f"start: {start}, end: {end}")
            maxLen = max(end - start + 1, maxLen)

        return maxLen


s = Solution()
print(s.length_of_longest_substring_k_distinct(
    "dfecebaasdsdfouafadtyuooo", 2))  # 14
