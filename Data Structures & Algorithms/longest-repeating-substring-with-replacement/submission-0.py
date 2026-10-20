class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        
        freq_dict = {}
        l = 0
        freq = 0
        long = 0

        for r in range (0, len(s)):
            if s[r] in freq_dict:
                freq_dict[s[r]] += 1
            else:
                freq_dict[s[r]] = 1

            freq = max(freq, freq_dict[s[r]])
            window = r-l+1

            if window - freq < k:
                continue
            elif window - freq > k:
                l += 1
            elif window - freq == k:
                long = max(long, window)

        return long
            







        