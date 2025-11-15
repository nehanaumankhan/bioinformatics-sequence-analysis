# Bioinformatics Sequence Analysis

A collection of Python implementations for fundamental bioinformatics sequence analysis problems from Rosalind. This repository contains solutions for calculating various sequence distance metrics and alignment-related computations.

--
## 🧬 Algorithms Implemented
--
### 1. Hamming Distance (`hamming_distance.py`)
Calculates the number of point mutations between two equal-length DNA sequences.
- **Problem**: [ROSALIND - HAMM](https://rosalind.info/problems/hamm/)
- **Key Concept**: Counts mismatches between aligned sequences
- **Usage**: Basic sequence similarity measurement
--
### 2. FASTA Parser (`parse_sequences.py`)
Utility functions for reading and parsing FASTA format files.
- **Features**: Handles multiple sequences, extracts headers and sequences
- **Application**: Essential preprocessing for all sequence analysis tasks
--
### 3. Transition/Transversion Ratio (`transitions_transversion_ratio.py`)
Computes the ratio of transitions to transversions between two DNA sequences.
- **Problem**: [ROSALIND - TRAN](https://rosalind.info/problems/tran/)
- **Key Concept**: 
  - **Transitions**: Purine↔Purine (A↔G) or Pyrimidine↔Pyrimidine (C↔T)
  - **Transversions**: Purine↔Pyrimidine mutations
- **Biological Significance**: Transitions occur more frequently than transversions
--
### 4. Distance Matrix (`distance_matrix.py`)
Computes pairwise distance matrices for multiple sequences.
- **Problem**: [ROSALIND - PDST](https://rosalind.info/problems/pdst/)
- **Application**: Phylogenetic analysis and multiple sequence comparison
- **Output**: Matrix of normalized Hamming distances
--
### 5. Edit Distance (`edit_distance.py`)
Calculates the minimum edit operations (insertions, deletions, substitutions) required to transform one sequence into another using dynamic programming.
- **Problem**: [ROSALIND - EDIT](https://rosalind.info/problems/edit/)
- **Algorithm**: Levenshtein distance with alignment reconstruction
- **Features**: Returns both the distance and optimal alignment
--