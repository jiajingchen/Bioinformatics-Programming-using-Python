#Bioinfomatics exercise 2015.5.25
#Created and refined by Jiajing Chen:)
import scipy.stats as stats

#create a dictionary of 20 amino acids
d={"a":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"k":9,"l":10,"m":11,"n":12,"p":13,"q":14,"r":15,"s":16,"t":17,"v":18,"w":19,"y":20}

#open FASTA data file
file= open("testseq.txt", "r")
f=open("testoutput2.txt","w")
allseq=[]

#get all the lines as a list, devided each protein sequence by ">" 
while True:
    line=file.read().split(">")[1:]
    allseq.append(line)
    if not line:
        break
#get a list of all the sequences
seq=allseq[0]
#pearson correlation
def pearson(c1,c2):
    p=stats.pearsonr(c1,c2)[0]
    return p
#distance correlation
def distance(c1,c2):
    pass
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
for item in seq:
    proteinpool.append(Protein(item))
#count the sum of each type of protein
suma,sumb,sumc,sumd=0.0,0.0,0.0,0.0  
for pro in proteinpool:
    if pro.get_ptype()=="a":
        suma+=1
    if pro.get_ptype()=="b":
        sumb+=1
    if pro.get_ptype()=="c":
        sumc+=1
    if pro.get_ptype()=="d":
        sumd+=1
print suma,sumb,sumc,sumd
#count pearson correlation coefficient
def pearsoncount():
    matchcounta,matchcountb,matchcountc,matchcountd=0,0,0,0
    for pro1 in proteinpool:
        maxp=0.0
        for pro2 in proteinpool:
            if pro2!=pro1: # do not compare to itself
                temp=pearson(pro1.count(),pro2.count())
                if temp>=maxp:
                    maxp=temp
                    match=pro2
        #foreach pro1 print the max PCC result

        #for each type,check if the max match is of the same type
        
        if match.get_ptype()==pro1.get_ptype()=="a":
            matchcounta+=1
        if match.get_ptype()==pro1.get_ptype()=="b":
            matchcountb+=1
        if match.get_ptype()==pro1.get_ptype()=="c":
            matchcountc+=1
        if match.get_ptype()==pro1.get_ptype()=="d":
            matchcountd+=1
def write():
    #print the match percentage
    f.write("\n")
    f.write("\n")
    f.write("The percentage of match of A protein is:")
    f.write(str(matchcounta/suma))
    f.write("\n")
    f.write("The percentage of match of B protein is:")
    f.write(str(matchcountb/sumb))
    f.write("\n")
    f.write("The percentage of match of C protein is:")
    f.write(str(matchcountc/sumc))
    f.write("\n")
    f.write("The percentage of match of D protein is:")
    f.write(str(matchcountd/sumd))  
           
pearsoncount()
write()


#close file
file.close()
f.close()
