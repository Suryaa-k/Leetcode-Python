from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = sorted(Counter(word).values(), reverse=True)
        return sum(freq * ((i // 8) + 1) for i, freq in enumerate(freqs))