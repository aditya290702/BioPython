from Bio import Entrez

Entrez.email = "aditya.shrivastav02@gmail.com"
handle = Entrez.einfo(db = "pubmed")
record = Entrez.read(handle)
print("DBInfo description", record["DbInfo"]["Description"])
print("DBInfo count", record["DbInfo"]["Count"])
handle.close()