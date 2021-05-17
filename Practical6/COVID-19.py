import matplotlib.pyplot as plt
# set numbers of each country's population
Country = ['USA', 'India', 'Brazil', 'Russia', 'UK']
People = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
number = [People['USA'], People['India'], People['Brazil'], People['Russia'], People['UK']]
# draw the pie chart
explode = (0, 0, 0.1, 0, 0)
plt.pie(number, explode=explode,labels=Country, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('The proportion of the population in each country')
print (People)
plt.show()

