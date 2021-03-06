import re
protein = ''
file = input('Please input the file name :')
code = {'ATA': 'J', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'B', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Z',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'O', 'TAG': 'U',
        'TGC': 'C', 'TGT': 'C', 'TGA': 'X', 'TGG': 'W'}
file_gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene_name=''
result=''
a = False
gene=''
for line in file_gene:
 if line.startswith('>'):
  if a == True:
   for n in range(0,len(gene),3):
    if gene[n:n+3] in code:
     protein = protein + code[gene[n:n+3]]
   result = result+gene_name+'     '+ str(len(protein))+ '\n' + protein + '\n'
   gene = ''
   gene_name=''
   protein = ''
   a = False
  if re.findall(r'unknown', line):
   gene_name = re.findall(r'(^>.+?)_', line)
   gene_name = gene_name[0]
   a = True
 else:
  if a == True:
   gene = gene + line.strip()
file_gene.close()
result_output = open(file +".fa", 'w')
result_output.write(result)
result_output.close()
print("file is successully created")

