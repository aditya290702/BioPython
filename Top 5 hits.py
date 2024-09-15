from Bio import Entrez


Entrez.email = "adityashrivastav02@gmail.com"
handle = Entrez.esearch(db = "nucleotide", term =["Homo sapiens[Orgn] AND pax6[Gene]"],retmax = 5)
record = Entrez.read(handle)
handle.close()

for k, v in record.items():
    print(k, v)

#Entrez.email = "adityashrivastav02@gmail.com"
#handle = Entrez.efetch(db = "protein", rettype = "fasta", retmode = "text", id = record["IdList"])
#result = handle.read()
#handle.close()

#fastaseq = result.replace("\n\n","\n")
#with open('HsPax6-protein.fasta', 'w') as f:
#    f.write(fastaseq)