from Bio.Seq import Seq
from Bio import SeqIO

contigs =[Seq("ATG"), Seq("ATCCG"), Seq("TTGCA")]
spacer = Seq("N" * 10)
print("Join Illustration", spacer.join(contigs))