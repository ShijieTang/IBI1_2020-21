import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene_name=' '
result=' '
a = False
gene = ' '
for line in file:
 if line.startswith('>'):
  if a == True:
   result = result+ (gene_name+'     '+ str(len(gene))+ '\n' + gene + '\n')
   gene = ' '
   gene_name = ' '
   a = False
  if re.findall(r'unknown', line):
   gene_name = re.findall(r'^>(.+?)_', line)
   gene_name = gene_name[0]
   a = True
 else:
  if a == True:
   gene = gene +line.strip()+'\n'
file.close()
result_output = open('unknown_function(1).fa','w')
result_output.write(result)
result_output.close()

