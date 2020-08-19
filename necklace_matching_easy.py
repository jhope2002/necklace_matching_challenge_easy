# Challenge #383 [Easy] Necklace matching

def same_necklace(necklace_one, necklace_two):
    if necklace_one == necklace_two:
        return True
    if necklace_one == "" or necklace_two == "":
        return False    
    else:        
        necklace_two_shifted = necklace_two
        for i in range(len(necklace_one) - 1):
            necklace_two_shifted = necklace_two_shifted[1:] + necklace_two_shifted[0]                        
            if necklace_one == necklace_two_shifted:
                return True
    return False                       


#print(same_necklace("nicole", "icolen")) # Returns True
#print(same_necklace("nicole", "lenico")) # Returns True
#print(same_necklace("nicole", "coneli")) # Returns False
#print(same_necklace("aabaaaaabaab", "aabaabaabaaa")) # Returns True
#print(same_necklace("abc", "cba")) # Returns False
#print(same_necklace("xxyyy", "xxxyy")) # Returns False
#print(same_necklace("xyxxz", "xxyxz")) # Returns False
#print(same_necklace("x", "x")) # Returns True
#print(same_necklace("x", "xx")) # Returns False
#print(same_necklace("x", "")) # Returns False
#print(same_necklace("", "")) # Returns True


# Optional Bonus 1

def repeats(string):    
    repeats = 1 # The original form is counted as 1 repeat automatically
    string_shifted = string
    for i in range(len(string) - 1): # Minus 1 prevents string_shifted from becoming being the original form
        string_shifted = string_shifted[1:] + string_shifted[0]
        if string == string_shifted:
            repeats += 1
    return repeats


#print(repeats('abc')) # Returns 1
#print(repeats('abcabcabc')) # Returns 3
#print(repeats('abcabcabcx')) # Returns 1
#print(repeats('aaaaaa')) # Returns 6
#print(repeats('a')) # Returns 1
#print(repeats('')) # Returns 1