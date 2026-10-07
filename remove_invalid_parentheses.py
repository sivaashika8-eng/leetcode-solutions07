from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []

        def remove(s, last_i, last_j, par):
            count = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    count += 1
                elif s[i] == par[1]:
                    count -= 1
                if count >= 0:
                    continue
                # Prefix is invalid at i: remove one par[1] in s[last_j..i],
                # skipping repeats in a run so each result is generated once.
                for j in range(last_j, i + 1):
                    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                        remove(s[:j] + s[j + 1:], i, j, par)
                return

            # No more invalid prefixes in this direction
            rev = s[::-1]
            if par[0] == '(':
                remove(rev, 0, 0, [')', '('])  # now fix extra '(' by scanning reversed
            else:
                res.append(rev)

        remove(s, 0, 0, ['(', ')'])
        return res