import re
score = 0
persentage = 0
seq1 = ""
seq2 = ""
seq3 = ""

# open files
with open('RandomSeq.fa') as RandomSeq, open('SOD2_human.fa') as human, open('SOD2_mouse.fa') as mouse:
 for line in RandomSeq:
  if line.startswith(">"):
   name_R = re.findall(r'>(.+?)$', line)
  else:
   seq1 = line.strip()
 for line in human:
  if line.startswith(">"):
   name_h = re.findall(r'>(.+?)$', line)
  else:
   seq2 = line.strip()
 for line in mouse:
  if line.startswith(">"):
   name_m = re.findall(r'>(.+?)$', line)
  else:
   seq3 = line.strip()
 for i in range(len(seq1)):
  if seq1[i] == seq2[i]:
   score += 1
 persentage = (score / len(seq1)) * 100
 print("the score of human-Randome is : " + str(score) + '\n' + " " + "the persentage is : " + str(persentage) + "%")
 score = 0
 for n in range(len(seq1)):
  if seq1[n] == seq3[n]:
   score +=1
 persentage = (score / len(seq1)) * 100
 print("the score of mouse-Randome is : " + str(score) + '\n' + " " +"the persentage is : " + str(persentage) + "%")
 score = 0
 for n in range(len(seq2)):
  if seq2[n] == seq3[n]:
   score +=1
 persentage = (score / len(seq1)) * 100
 print("the score of mouse-human is : " + str(score) + '\n' + " " + "the persentage is : " + str(persentage) + "%")
