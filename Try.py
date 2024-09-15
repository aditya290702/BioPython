from Bio.Seq import Seq
from Bio import SeqIO

def main():

    seq = Seq("GATC")
    for index, letter in enumerate(seq) :
            print("Index Value =", index, "Value = ", letter)
    print(seq[0], seq[1])

    new = Seq(" AAAATTCCGGAAA")
    print(new.count("AA"))
    print(len(new))

if __name__=="__main__":
    main()
