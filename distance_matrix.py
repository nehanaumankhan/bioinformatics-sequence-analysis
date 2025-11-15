"""
P-DISTANCE: 
Dp(s,t) = Number of differing positions in s and t / size of s (or t) 
where s and t are sequences of equal length.
DISTANCE MATRIX (nxn):
A distance matrix is an n x n matrix that contains the pairwise distances between a set of n sequences. 
The entry at row i and column j represents the distance between sequence i and sequence j.
"""
# Function to parse sequences from a FASTA file
def parse_fasta_file(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        seq_id = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):  # Sequence ID line
                seq_id = line[1:]  # Remove ">"
                sequences[seq_id] = ""
            else:  # Sequence line
                sequences[seq_id] += line
    return sequences

# Function to compute the p-distance between two sequences
def p_distance(s1, s2):
    mismatches = sum(a != b for a, b in zip(s1, s2))
    return mismatches / len(s1)

# Function to compute the distance matrix for a set of sequences
def distance_matrix(sequences):
    seq_ids = list(sequences.keys())
    n = len(seq_ids)
    matrix = [[0.0]*n for _ in range(n)]    
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = p_distance(sequences[seq_ids[i]], sequences[seq_ids[j]])
    return matrix, seq_ids

# Function to print matrix nicely
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:.5f}" for val in row))

# ===== Main Program =====
file_path = "globin.fasta"  
sequences = parse_fasta_file(file_path)
matrix, seq_ids = distance_matrix(sequences)
print_matrix(matrix)