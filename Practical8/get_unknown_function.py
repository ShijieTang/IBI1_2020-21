import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene_name=' '
result=' '
a = False
gene = ''
for line in file:
# find the DNA we want
# a is used to signal whether the fuction of gene is unknown
 if line.startswith('>'):
  if a == True:
   result = result+ (gene_name+'     '+ str(len(gene))+ '\n' + gene + '\n')
   gene = ''
   gene_name = ''
   a = False
  if re.findall(r'unknown', line):
   gene_name = re.findall(r'^>(.+?)_', line)
   gene_name = gene_name[0]
   a = True
 else:
  if a == True:
   gene = gene +line.strip()
file.close()
# write the result in a new file named "unknow_function.fa"
result_output = open('unknown_function.fa','w')
result_output.write(result)
result_output.close()

