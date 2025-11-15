'''
Given two strings s and t of equal length, the Hamming distance between s and t, 
denoted dH(s,t), is the number of corresponding symbols that differ in s and t
'''

def hamming_distance(s, t):
    distance = 0

    for a, b in zip(s, t): # zip -> pairs up corresponding characters of s and t
        if a != b:
            distance += 1
    return distance

# Example usage:
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

print(hamming_distance(s, t))   # Output: 7