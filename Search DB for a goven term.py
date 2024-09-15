from Bio import Entrez

Entrez.email = "aditya.shrivastav02@gmail.com"
handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)
print("DBInfo description", record["DbInfo"]["Description"])
print("DBInfo count", record["DbInfo"]["Count"])
handle.close()

handle = Entrez.esearch(db = "pubmed" ,term= "autism machine learning")
record = Entrez.read(handle)
print("Search results,record idlist",record["IdList"])
handle.close()

#retrieve another article

handle = Entrez.efetch(db="pubmed", id="37920379")
print("Pubmed Article Info")
print(handle.read())