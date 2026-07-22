from bisect import bisect_left, bisect_right

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')

        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j
        R = len(runs)

        run_of = [0] * n
        for ri, (c, rs, re) in enumerate(runs):
            for p in range(rs, re + 1):
                run_of[p] = ri

        bridges = []
        for i in range(1, R - 1):
            c,  bs, be  = runs[i]
            lc, ls, le  = runs[i - 1]
            rc, rs, re  = runs[i + 1]
            if c == '1' and lc == '0' and rc == '0':
                bridges.append((ls, le, rs, re))
        B = len(bridges)

        b_le = [b[1] for b in bridges]
        b_ls = [b[0] for b in bridges]
        b_rs = [b[2] for b in bridges]
        b_re = [b[3] for b in bridges]

        INF = float('inf')
        SZ = n + 2

        seg = [-INF] * (2 * SZ)
        def upd(pos, v):
            pos += SZ
            if v > seg[pos]: seg[pos] = v
            pos >>= 1
            while pos: seg[pos] = max(seg[2*pos], seg[2*pos+1]); pos >>= 1
        def qry(r):
            res = -INF; l, r = SZ, r + SZ + 1
            while l < r:
                if l & 1: res = max(res, seg[l]); l += 1
                if r & 1: r -= 1; res = max(res, seg[r])
                l >>= 1; r >>= 1
            return res

        q = len(queries)
        ans = [total_ones] * q
        order_desc = sorted(range(q), key=lambda i: queries[i][0], reverse=True)

        b_by_ls = sorted(range(B), key=lambda i: bridges[i][0], reverse=True)
        bp = 0

        for qi in order_desc:
            ql, qr = queries[qi]
            while bp < B and bridges[b_by_ls[bp]][0] >= ql:
                bi = b_by_ls[bp]
                ls, le, rs, re = bridges[bi]
                upd(re, (le - ls + 1) + (re - rs + 1))
                bp += 1
            v = qry(qr)
            if v > 0:
                ans[qi] = max(ans[qi], total_ones + v)

        for qi in range(q):
            ql, qr = queries[qi]

            lo = bisect_left(b_le, ql)
            for bi in range(lo, B):
                ls, le, rs, re = bridges[bi]
                if ls >= ql:
                    break
                left_g  = le - ql + 1
                right_g = min(re, qr) - rs + 1
                if right_g > 0:
                    ans[qi] = max(ans[qi], total_ones + left_g + right_g)

            hi = bisect_right(b_rs, qr) - 1
            for bi in range(hi, -1, -1):
                ls, le, rs, re = bridges[bi]
                if re <= qr:
                    break
                if ls < ql:
                    continue
                left_g  = le - max(ls, ql) + 1
                right_g = qr - rs + 1
                if left_g > 0:
                    ans[qi] = max(ans[qi], total_ones + left_g + right_g)

        return ans