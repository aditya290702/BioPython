from Bio import Entrez

Entrez.email = "adityashrivastav02@gmail.com"
handle = Entrez.efetch(db = "protein", rettype = "fasta", retmode = "text", id = record["IdList"])
result = handle.read()
handle.close()

#To iterate over Ids
for seq_id in record["IdList"]:
    print(seq_id)
    handle = Entrez.efetch((db = "nucelotide", id = seq_id, rettype= "gb", rettmode=="text"))
    result= handle.read()
    handle.close()

#save
filename = f"HsPax6-{seq_id}-nucleotide.gb"
print("saving to file:", filename)
with open(filename, 'w') as gbfile:

#append
    gbfile.write(result.rstrip() + "\n")