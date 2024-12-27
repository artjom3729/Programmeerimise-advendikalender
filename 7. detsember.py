from collections import Counter

letters = "HNT"
input_str = "ILBHCNDLET"

def smallest_substring_with_all_letters(input_str, letters):
    required = Counter(letters)
    window_counts = Counter()
    
    l, r = 0, 0
    formed = 0
    required_length = len(required)
    min_length = float('inf')
    min_window = ""
    
    while r < len(input_str):
        char = input_str[r]
        window_counts[char] += 1
        
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        while l <= r and formed == required_length:
            char = input_str[l]
            
            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_window = input_str[l:r+1]
            
            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1
            
            l += 1
        
        r += 1
    
    return min_window


result = smallest_substring_with_all_letters(input_str, letters)
print(result) # Expected output: HCNDLET
