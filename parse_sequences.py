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

# Example usage:
fasta_file_path = "globin.fasta"
sequences = parse_fasta_file(fasta_file_path)
for seq_id, sequence in sequences.items():
    print(f">{seq_id}\n{sequence}")

    