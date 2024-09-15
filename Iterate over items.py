from Bio import Entrez


Entrez.email = "adityashrivastav02@gmail.com"
handle = Entrez.esearch(db = "protein", term =["Homo sapiens[Orgn] AND pax6[Gene]"], usehistory ="y")
record = Entrez.read(handle)
handle.close()

for k, v in record.items():
    print(k, v)

Entrez.email = "adityashrivastav02@gmail.com"
handle = Entrez.efetch(db = "protein", rettype = "fasta", retmode = "text", id = record["IdList"])
result = handle.read()
handle.close()

fastaseq = result.replace("\n\n","\n")
with open('HsPax6-protein.fasta', 'w') as f:
    f.write(fastaseq)

#To iterate over Ids
for seq_id in record["IdList"]:
    print(seq_id)
    handle = Entrez.efetch((db == "nucelotide", id == seq_id, rettype == "gb", rettmode=="text"))
    result= handle.read()
    handle.close()

#save
filename = f"HsPax6-{seq_id}-nucleotide.gb"
print("saving to file:", filename)
with open(filename, 'w') as gbfile:

#append
    gbfile.write(result.rstrip() + "\n")