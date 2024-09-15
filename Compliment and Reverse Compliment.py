from Bio.Seq import Seq
from Bio import SeqIO

seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print("seq compliment", seq.complement())
print("reverse compliment", seq.reverse_complement())

