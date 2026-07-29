from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        mid = ""
        half_chars = []

        for c in sorted(freq):
            if freq[c] % 2 == 1:
                mid = c
            for _ in range(freq[c] // 2):
                half_chars.append(c)

        half = half_chars

        def count_perms(counts, cap):
            vals = [v for v in counts.values() if v > 0]
            if not vals:
                return 1
            total = sum(vals)
            result = 1
            for i, v in enumerate(vals):
                result = comb(total - sum(vals[:i]), v)
                if result >= cap:
                    return cap
            # need full multinomial
            result = 1
            remaining = total
            for v in vals:
                result = result * comb(remaining, v)
                remaining -= v
                if result >= cap:
                    return cap
            return result

        cur_cnt = Counter(half)
        total_perms = count_perms(cur_cnt, k + 1)
        if total_perms < k:
            return ""

        result = []
        k_left = k

        for pos in range(len(half)):
            for c in sorted(cur_cnt):
                if cur_cnt[c] == 0:
                    continue
                cur_cnt[c] -= 1
                sub = {ch: cur_cnt[ch] for ch in cur_cnt if cur_cnt[ch] > 0}
                p = count_perms(sub, k_left + 1)
                if p >= k_left:
                    result.append(c)
                    break
                else:
                    k_left -= p
                    cur_cnt[c] += 1

        half_str = "".join(result)
        return half_str + mid + half_str[::-1]