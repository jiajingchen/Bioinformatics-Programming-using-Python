#Bioinfomatics exercise 2015.5.26
#Created and refined by Jiajing Chen:)

#create a dictionary of 20 amino acids
d={"a":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"k":9,"l":10,"m":11,"n":12,"p":13,"q":14,"r":15,"s":16,"t":17,"v":18,"w":19,"y":20}

#open FASTA data file
file= open("sequence.txt", "r")
allseq=[]

#get all the lines as a list, devided each protein sequence by ">" 
while True:
    line=file.read().split(">")[1:]
    allseq.append(line)
    if not line:
        break
#get a list of all the sequences
seq=allseq[0]

# define the class for protein: to find their type,info line and sequence lines
class Protein:
    def __init__(self,sequence):
        self.sequence=sequence
    def get_name(self):
        flag=self.sequence.find(" ")
        return(self.sequence[:flag]) 
    def get_ptype(self):
        flag=self.sequence.find(" ")
        return(self.sequence[flag+1])
    def get_infoline(self):
        flag=self.sequence.find("\n")
        return(self.sequence[:flag]) 
    def get_TaxId(self):
        flag1=self.sequence.find("TaxId:")
        flag2=self.sequence.find("\n")
        return self.sequence[(flag1+7):(flag2-2)]
    def get_sequence(self):
        flag=self.sequence.find("}")
        infoline=self.sequence[(flag+1):]
        return infoline
    #count the sequence for each amino acid and output a list of each percentage
    def count(self):
        countlist=[]
        for key in d:
            countlist.append(self.get_sequence().count(key))
        return countlist
    def percentage(self):
        countlist=self.count
        percentagelist=[]
        countsum=0.0
        for i in range(20):
            countsum+=countlist[i]
        for i in range(20):
            percentage=countlist[i]/countsum
            percentagelist.append(percentage)
        return percentagelist

#make a proteinpool(a list) for all Protein Class objects
proteinpool=[]
#initiate count list
acount,bcount,ccount,dcount=20*[0],20*[0],20*[0],20*[0]

#add all the proteins to a list of protein class 
for item in seq:
    proteinpool.append(Protein(item))
#count the sum of a,b,c,d type of protein and output lists 
def countall():
    for i in range(len(proteinpool)):
        if proteinpool[i].get_ptype()=="a":
            for j in range(20):
                acount[j]+=proteinpool[i].count()[j]
        if proteinpool[i].get_ptype()=="b":
            for j in range(20):
                bcount[j]+=proteinpool[i].count()[j]
        if proteinpool[i].get_ptype()=="c":
            for j in range(20):
                ccount[j]+=proteinpool[i].count()[j]
        if proteinpool[i].get_ptype()=="d":
            for j in range(20):
                dcount[j]+=proteinpool[i].count()[j]
countall()
#output
print acount
print bcount
print ccount
print dcount

#close file
file.close()
