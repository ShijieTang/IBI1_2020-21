import re
seq ='ATGCGACTACGATCGAGGGCC'
gene = {'ATG':'M', 'CGA':'R', 'CTA':'L', 'TCG':'S', 'AGG':'R', 'GCC':'A'}
protein = ' '
for n in range(0,len(seq),3):
 if seq[n:n+3] in gene:
  protein = protein + gene[seq[n:n+3]]
print(protein)
