#open FASTA data file
file= open("mitochondrialproteinsofarabidopsis.txt", "r")
f=open("OUTPUT.txt","w")
allseq=[]

#get all the lines as a list, devided each protein sequence by ">" 
while True:
    line=file.read().split(">")[1:]
    allseq.append(line)
    if not line:
        break
#get a list of all the sequences
seq=allseq[0]

# define the class for protein: to find sequence lines,length and K pos,frame
class Protein:
    def __init__(self,sequence):
        self.sequence=sequence
    def get_name(self):
        flag=self.sequence.find(" ")
        return self.sequence[0:flag]
    def get_length(self):
        return len(self.get_sequence())
    def get_sequence(self):
        flag=self.sequence.find("\n")
        sheerseq=self.sequence[(flag+1):]
        new=[]
        for i in range(len(sheerseq)):
            if sheerseq[i]!="\n":
                new.append(sheerseq[i])        
        return new
    
    def get_length(self):
        return len(self.get_sequence())
    def get_k_pos(self):
        kpos=[]
        for i in range(len(self.get_sequence())):
            if self.get_sequence()[i]=="K":
                kpos.append(i)
        return kpos
    def get_frame(self):
        framepool=[]
        for i in self.get_k_pos():
            frame=27*[0]
            #get 13 letters before K
            if i>=13:
                for j in range(14):
                    frame[j]=self.get_sequence()[i-13+j]
            if i<13:
                for j in range(0,i):
                    frame[13-i+j]=self.get_sequence()[0+j]
            # get 13 letters after K
            l=len(self.get_sequence())-i
            if l>13:
                for j in range(14):
                    frame[13+j]=self.get_sequence()[i+j]
            if l<=13:
                for j in range(l):
                    frame[13+j]=self.get_sequence()[i+j]            
            # replace 0 with "-"
            for i in range(27):
                if frame[i]==0:
                    frame[i]="-"
            # join the str in the list and return a string 
            newframe="".join(frame)
            framepool.append(newframe)
        return framepool #append all the kframe in a list


proteinpool=[]    
for item in seq:
    proteinpool.append(Protein(item))


for pro in proteinpool:

    for frame in pro.get_frame():
        f.write("\n")
        f.write(frame)



#close file
file.close()
f.close()
