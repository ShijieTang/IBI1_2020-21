from xml.dom.minidom import parse
import xml.dom.minidom
import re
import matplotlib.pyplot as plt

# Define the variable 
count_DNA = 0
count_RNA = 0
count_Protein = 0
count_Carbohydrate = 0
count_Oligosaccharide = 0
son_namelist = []

# Input the file and extract "term"
file = xml.dom.minidom.parse("go_obo.xml")
collection = file.documentElement
terms = collection.getElementsByTagName("term")

# Write a function to count the number.
def counter(x):
 print("============= "+ x +" =============")
 n = 0
 son_namelist1 = ["orignal"]
 son_namelist2 = []
 terms = collection.getElementsByTagName("term")
 fathers_id = []
 son_name = []
 global son_namelist
 son_namelist = []
 print(x + " parents are being sought ...")
 for term in terms:
     defstr = term.getElementsByTagName('defstr')[0]
     is_a = term.getElementsByTagName('is_a')
     father_id = term.getElementsByTagNameNS('*','id')[0]
     if re.findall(x, defstr.childNodes[0].data):
         fathers_id.append(father_id.childNodes[0].data)
 print("Parents have been found")
 print("The number is : " + str(len(fathers_id)))
 print("")
 print(x+ " sons are being sought ...")
 for term in terms:
     if term.getElementsByTagNameNS('*','is_a') == []:
         continue
     else:
         son_id = term.getElementsByTagNameNS(term.namespaceURI,'id')[0].childNodes[0].data
         is_a = term.getElementsByTagNameNS(term.namespaceURI,'is_a')
         for iterm in is_a:
             if iterm.childNodes[0].data in fathers_id:
                     son_name = son_id
                     son_namelist.append(son_name)
                     break
 print("The primary sons have been found")
 print("The number is : " + str(len(son_namelist)))
 print("")
 print("Other sons are been finding ...")
 while len(son_namelist1) != len(son_namelist2):
     n +=1
     print("Counting ... " + '\n'+ "## Please be patient, Thank you! (^-^) ##")
     print("Checking version is : " + str(n))
     son_namelist1 = list(son_namelist)
     for term in terms:
         if term.getElementsByTagNameNS(term.namespaceURI,'is_a') == []:
             continue
         else:
             is_a = term.getElementsByTagNameNS(term.namespaceURI,'is_a')
             for iterm in is_a:
                 if iterm.childNodes[0].data in son_namelist:
                     son_id = term.getElementsByTagNameNS(term.namespaceURI,'id')[0].childNodes[0].data
                     son_namelist.append(son_id)
                     break
     son_namelist = list(set(son_namelist))
     son_namelist2 = son_namelist
     print("The number now is : "+ str(len(son_namelist)))
     print("")
 print("Congratulations! Search is finished.")
 print("The "+x+" number is %s" % len(son_namelist))
 return son_namelist

# Get the number of specific items
x = "DNA"
counter(x)
count_DNA = len(son_namelist)
x = "RNA"
counter(x)
count_RNA = len(son_namelist)
x = "protein"
counter(x)
count_Protein = len(son_namelist)
x = "carbohydrate"
counter(x)
count_Carbohydrate = len(son_namelist)
x = "oligosaccharide"
counter(x)
count_Oligosaccharide = len(son_namelist)

# Show the result
print("Here is the result: ")
print("The DNA number is %s" % count_DNA)
print("The Protein number is %s" % count_Protein)
print("The RNA number is %s" % count_RNA)
print("The Carbohydrate number is %s" % count_Carbohydrate)
print("The Oligosaccharide number is %s" % count_Oligosaccharide)
        
# Draw the pie chart
explode = (0, 0, 0, 0.1, 0)
number = (count_DNA, count_Protein, count_Oligosaccharide,count_RNA, count_Carbohydrate,)
labels = ("count_DNA", "count_Protein", "count_Oligosaccharide", "count_RNA", "count_Carbohydrate")
plt.pie(number, explode=explode,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('The proportion of the macromolecule number')
plt.show()
