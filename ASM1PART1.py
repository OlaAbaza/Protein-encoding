map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
def find_rna(DNA,protein) :
    " "
    rna=[]
    rev=[]
    com=''
    for i in range(0,len(DNA),1):
                    if(DNA[i]=='T'):
                      rna.append('U')
                    else:
                      rna.append(DNA[i])
                   

    rev=list(reversed(rna))

    for i in range(0,len(rev),1):
             if(rev[i]=='U'):
                rev[i]='A'
             elif(rev[i]=='A'):
                rev[i]='U'
             elif(rev[i]=='C'):
                rev[i]='G'
             else:
                rev[i]='C'
    
    for i in range(0,len(rna)-2,1):
        com+=rna[i]
        com+=rna[i+1]
        com+=rna[i+2]
        if(map[com]==protein):
          print(DNA[i:i+3])
        com=''
   
    for i in range(0,len(rev)-2,1):
        com+=rev[i]
        com+=rev[i+1]
        com+=rev[i+2]
        if(map[com]==protein):
          print(DNA[len(DNA)-(i+3):len(DNA)-(i)])
     
        com=''
    

           
        
print("enter the sequence:")
DNA=input()
print("enter the protein:")
protein=input()
find_rna(DNA,protein)
