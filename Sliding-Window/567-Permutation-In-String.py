from collections import defaultdict
def checkInclusion(s1, s2):
    # Set up the a character frequency count for s1
    s1_freq = defaultdict(int)
    for c in s1:
        s1_freq[c] += 1
    
    # tThis dictionary will hold the character frequency count (CFC) for the current substring
    substring_freq = defaultdict(int)

    # Set the window size to the length of string s1
    k = len(s1)

    # Initialise a left pointer
    left = 0
    for right in range(len(s2)):
        # Add the current character to the CFC for the current substring
        substring_freq[s2[right]] += 1

        # If the window size is equal to k
        if right - left + 1 == k:

            # Check if a permuation of s1 can create the current window
            if substring_freq == s1_freq:
                return True
            # If the frequency of the char to be removed is 1 remove that key from the dict
            if substring_freq[s2[left]] == 1:
                del substring_freq[s2[left]]
            # Otherwise just decrement its count 
            else:
                substring_freq[s2[left]] -= 1
            # Push the left pointer
            left += 1
    # Return False if no permuation is available.
    return False