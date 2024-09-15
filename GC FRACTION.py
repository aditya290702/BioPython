from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
# gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
# print(gc,"%")
print("GC FRACTION IS =", gc_fraction(seq))
print("GC percent is", gc_fraction(seq)*100)