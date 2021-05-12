from xml.dom.minidom import parse
import xml.dom.minidom
import re
import matplotlib.pyplot as plt
# set the counter
count_DNA = 0
count_RNA = 0
count_Protein = 0
count_Carbohydrate = 0
count_Oligosaccharide = 0

# input the file
file = xml.dom.minidom.parse("go_obo.xml")
collection = file.documentElement
terms = collection.getElementsByTagName("term")
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    is_a = term.getElementsByTagName('is_a')
    if re.findall("DNA",defstr.childNodes[0].data):
        count_DNA += len(is_a)
    if re.findall("RNA",defstr.childNodes[0].data):
        count_RNA += len(is_a)
    if re.findall("protein",defstr.childNodes[0].data):
        count_Protein += len(is_a)
# count the number of other macromolecule
    if re.findall("carbohydrate",defstr.childNodes[0].data):
        count_Carbohydrate += len(is_a)
    if re.findall("oligosaccharide",defstr.childNodes[0].data):
        count_Oligosaccharide += len(is_a)

# draw the pie chart
explode = (0, 0, 0, 0.1, 0)
number = (count_DNA, count_Protein, count_Oligosaccharide,count_RNA, count_Carbohydrate,)
labels = ("count_DNA", "count_Protein", "count_Oligosaccharide", "count_RNA", "count_Carbohydrate")
plt.pie(number, explode=explode,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('The proportion of the macromolecule number')
plt.show()

# show the result
print("the DNA number is %s" % count_DNA)
print("the Protein number is %s" % count_Protein)
print("the RNA number is %s" % count_RNA)
print("the Carbohydrate number is %s" % count_Carbohydrate)
print("the Oligosaccharide number is %s" % count_Oligosaccharide)
