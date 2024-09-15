from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

Records = []
Ids = []
pathToFile = "ls_orchid.fasta"
for seq_records in SeqIO.parse(pathToFile, "fasta"):
    Records.append(seq_records)
    Ids.append(seq_records.id.split("|")[1])
    print(seq_records)
    print(str(seq_records.seq))
    print((len(seq_records)))