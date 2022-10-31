#Imports
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')

#Column Titles
#Time, Temp1F, Temp2F, RH (Humidity), Pressure, accelX, accelZ

df = pd.read_csv('data.TXT') #Insert filename here
df.set_index('Time (ms)', inplace = True) #Sets the time column as the index
df.drop(labels = df.index.tolist()[-1], axis = 0, inplace = True) #Drops last row of DF bc the read data may be incomplete

#Graph function that graphs requested sensor data based on the "DataTitle" argument
def graph(DataTitle = None):
    dataExists = True
    if DataTitle == "Temp1F":
        for i in range(len(df)):
            plt.scatter(df.index.tolist()[i], df['Temp1F'].tolist()[i], c = 'blue')
    elif DataTitle == "Temp2F":
        for i in range(len(df)):
            plt.scatter(df.index.tolist()[i], df['Temp2F'].tolist()[i], c = 'blue')
    elif DataTitle == "RH":
        for i in range(len(df)):
            plt.scatter(df.index.tolist()[i], df['RH'].tolist()[i], c = 'blue')
    elif DataTitle == "Pressure":
        for i in range(len(df)):
            plt.scatter(df.index.tolist()[i], df['Pressure'].tolist()[i], c = 'blue')
    elif DataTitle == "accelX":
        for i in range(len(df)):
            plt.scatter(df.index.tolist()[i], df['accelX'].tolist()[i], c = 'blue')
    elif DataTitle == "accelZ":
        for i in range(len(df)):
            plt.scatter(df.index.tolist()[i], df['accelZ'].tolist()[i], c = 'blue')
    else:
        dataExists = False
        print("Requested Data not found")
   
    if dataExists:
        plt.xlabel('Time (ms)')
        plt.ylabel(DataTitle)
        plt.show()
