from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print("Slice 4th position to 11th position ", seq[4:12])
print("Slice Starting from 0 every third charecter ", seq[0::3])
print("Slice Starting from 1 every third charecter ", seq[1::3])
print("Reverse my Seq", seq[::-1])
print("my seq is conv to a string", str(seq))