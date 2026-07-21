class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        base = s.count('1')  

        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best_gain = 0
        for i in range(1, len(runs) - 1):
            char, length = runs[i]
            if char == '1':  
                left_zeros  = runs[i-1][1]  
                right_zeros = runs[i+1][1]  
                best_gain = max(best_gain, left_zeros + right_zeros)

        return base + best_gain