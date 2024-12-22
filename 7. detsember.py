from collections import Counter

letters = "HNT"
sisend = "ILBHCNDLET"

def smallest_substring_with_all_letters(sisend, letters):
    required = Counter(letters)
    window_counts = Counter()
    
    l, r = 0, 0
    formed = 0
    required_length = len(required)
    min_length = float('inf')
    min_window = ""
    
    while r < len(sisend):
        char = sisend[r]
        window_counts[char] += 1
        
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        while l <= r and formed == required_length:
            char = sisend[l]
            
            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_window = sisend[l:r+1]
            
            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1
            
            l += 1
        
        r += 1
    
    return min_window

result = smallest_substring_with_all_letters(sisend, letters)
print(result)