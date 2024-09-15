from Bio.Seq import Seq
from Bio import SeqIO

prot = Seq("EVRNAK")
Dna = Seq("ATGC")
print("Protein and Dna :", prot + Dna)