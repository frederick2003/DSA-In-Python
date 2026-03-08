def lengthOfLongestSubstring(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    char_set = set()
    count = 1
    longest = 0
    l = 0
    r = 1
    char_set.add(s[l])
    while r <= n - 1:
        left = s[l]
        right = s[r]
        if right not in char_set:
            char_set.add(right)
            r += 1
            count += 1
            longest = max(longest, count)
        else:
            while s[r] in char_set and l < r:
                char_set.remove(s[l])
                l += 1
                count -= 1
    return longest