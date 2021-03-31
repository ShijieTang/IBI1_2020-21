import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data.csv")
covid_data.loc[0:10,]
covid_data.loc[covid_data["location"] == "Afghanistan", "total_cases"]
world_new_cases = covid_data.loc[covid_data["location"] == "World","new_cases"]
world_new_deaths = covid_data.loc[covid_data["location"] == "World","new_deaths"]
world_date = covid_data.loc[covid_data["location"] == "World","date"]
world_new_cases.mean()
world_new_cases.median()
plt.boxplot(world_new_cases, vert= True, whis= 1.5, patch_artist= True)
plt.show()
plt.plot(world_date,world_new_cases,'b',world_date,world_new_deaths,'g')
plt.xticks(world_date,rotation=-90)
plt.show()

#About the question:
a = covid_data.loc[covid_data["total_cases"] <= 10, ["date","location"]]
#get the country which is eligible on 2020-03-31
b = a.loc[a["date"] == "2020-03-31", "location"]
#get the country which is eligible on 2020-03-30
c = a.loc[a["date"] == "2020-03-30", "location"]
#get the result
result = pd.merge(b+c)
print(result)
