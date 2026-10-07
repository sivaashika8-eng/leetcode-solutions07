# Remove Invalid Parentheses

Solution to LeetCode 301. Given a string containing letters and parentheses, remove the minimum number of parentheses so the result is valid, and return all unique valid strings.

## Problem

- Input: a string `s` (1 <= length <= 25) of lowercase letters and `(` / `)`, with at most 20 parentheses.
- Output: a list of all unique valid strings reachable with the minimum number of removals, in any order.

| Input | Output |
|-------|--------|
| `"()())()"` | `["(())()", "()()()"]` |
| `"(a)())()"` | `["(a())()", "(a)()()"]` |
| `")("` | `[""]` |

## Approach

The solution is a pruned backtracking search that never generates duplicates.

1. **Scan left to right** with a running count (`(` is +1, `)` is -1). The first time the count goes negative at index `i`, the prefix has one extra `)`, so one `)` in `s[last_j..i]` must be removed.
2. **Skip repeats in a run.** Within a run of consecutive `)`, removing any one gives the same string, so only the first of each run is tried. No result set is needed.
3. **Never revisit.** The recursion resumes at `i` and `j` only moves forward, so removals are never reordered or retried.
4. **Fix extra `(` by reversing.** Once no extra `)` remain, reverse the string and run the same logic with the roles of `(` and `)` swapped. Reversing back at the end restores the original orientation.

Because each step removes exactly one character that is provably part of an invalid prefix, only minimal removals are explored.

## Usage

```python
from remove_invalid_parentheses import Solution

print(Solution().removeInvalidParentheses("()())()"))
# ['(())()', '()()()']  (order may vary)
```

## Complexity

- **Time:** worst case is still exponential in the number of parentheses (n <= 20), since many distinct minimal answers can exist. It avoids the O(2^n) keep/remove branching of the naive DFS and never builds the same string twice. Each step costs O(n) for scanning and slicing.
- **Space:** O(n) recursion depth plus the output.

## Files

- `remove_invalid_parentheses.py`: the `Solution` class.
- `README.md`: this file.

## Testing

```python
s = Solution()
assert sorted(s.removeInvalidParentheses("()())()")) == sorted(["(())()", "()()()"])
assert sorted(s.removeInvalidParentheses("(a)())()")) == sorted(["(a())()", "(a)()()"])
assert s.removeInvalidParentheses(")(") == [""]
```
