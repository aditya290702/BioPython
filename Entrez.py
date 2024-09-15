from Bio import Entrez
Entrez.email = "aditya.shrivastav02@gmail.com"

handle = Entrez.einfo()
record = Entrez.read(handle)
print("I have access to the following databases", record["DbList"])
handle.close()