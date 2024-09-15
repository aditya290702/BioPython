from Bio.Seq import Seq
#=#from Bio import SeqIO

seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGCC")
print(len(seq))
print(seq.transcribe())
print(seq.translate())