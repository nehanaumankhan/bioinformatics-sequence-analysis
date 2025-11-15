"""
EDIT DISTANCE ALGORITHM

APPROACH:
We use dynamic programming to compute the minimum number of edit operations (substitutions,
insertions, deletions) required to transform one string into another.

THE EDIT COST MATRIX:
* edit_cost[i][j] -> the minimum edit distance between the first i characters  of string s and the first j characters of string t.
* Rows -> characters of string s (plus empty string)
* Columns -> correspond to characters of string t (plus empty string)
* Each cell stores the cumulative cost to align the prefixes up to that point

OPERATIONS:
* SUBSTITUTION: change one residue to another (cost: 1 if different, 0 if same)
* INSERTION: add one residue into a sequence (cost: 1)
* DELETION: remove one residue from a sequence (cost: 1)

EDIT DISTANCE: The minimum number of edits required to transform one string into the other.
"""

def edit_distance(s, t):
    m, n = len(s), len(t)   # dimensions of matrix are (m+1) x (n+1); +1 for empty string
    
    # Initializing teh edit_cost matrix with zeros
    edit_cost = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row: mutation between empty string and string t[0:j] requires j insertions
    for i in range(m + 1):
        edit_cost[i][0] = i  
    
    # Initialize first column: mutation between s[0:i] and empty string requires i deletions
    for j in range(n + 1):
        edit_cost[0][j] = j  
    
    # Filling the edit cost matrix using dynamic programming approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                # exact matching residues = diagonal value is carried forward
                edit_cost[i][j] = edit_cost[i - 1][j - 1]
            else:
                # residues that don't match = min(insertion, deletion, substitution) 
                edit_cost[i][j] = min(
                    edit_cost[i - 1][j] + 1,      # Deletion from s
                    edit_cost[i][j - 1] + 1,      # Insertion into s  
                    edit_cost[i - 1][j - 1] + 1   # Substitution
                )
    
    # The bottom-right cell contains the edit distance between complete strings
    return edit_cost[m][n]

# Example usage:
s = "PLEASANTLY"
t = "MEANLY"
result = edit_distance(s, t)
print(f"Edit distance: {result}")  