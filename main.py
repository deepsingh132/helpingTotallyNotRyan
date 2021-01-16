import pandas as pd
import matplotlib.pyplot as plt

#include Latest LHD Build File

df=pd.read_excel("LHD Build Full Scores - Jan 15 12 50 PM ET.xlsx") 
sumList=df['sum'].values.tolist()
nameList=df['display name'].values.tolist()

#print(nameList + sumList)

#plt.hist(sumList)
#plt.hist(nameList)
df.plot(kind='hist', bins=8, facecolor='green', alpha=0.8)
plt.title("Sums of all Hackers till 15th Jan")
plt.ylabel('No of Hackers')
plt.xlabel('Sum')
plt.show()