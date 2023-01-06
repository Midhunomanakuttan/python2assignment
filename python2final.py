import pandas as pd
import numpy as np
from matplotlib import image as mpimg
import matplotlib.pyplot as plt
df = pd.read_csv('GrowLocations.csv')
df.columns = ['Serial', 'Longitude','Latitude','Type','SensorType','Code','BeginTime','EndTime']
# printing the dataframe
# print(df)
#df.to_csv('cleanheader_data.csv', index=False)
column_headers = list(df.columns.values)
print("The Column Header :", column_headers)
# removing the rows with zero longitude and latitude values
df2 = df.loc[(df['Latitude'] != 0) & (df['Longitude'] != 0)]
#print(df2)
# remove the rows with latitude range
df3 = df2.loc[(df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985)]
#remove the rows with longitude range
df3 = df2.loc[(df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848)]
#df3.to_csv('clean_data.csv', index=False)
#removing the duplicate rows
df4 = df3.drop_duplicates(subset=["Serial"], keep='first')
df4.to_csv('noduplicate_data.csv', index=False)
df = pd.read_csv('noduplicate_data.csv')
ruh_m = plt.imread('C:/Users/CEX/PycharmProjects/Python2assignment/map7.png')
#plt.title("plotting grow data")
#plt.imshow(ruh_m)
# plt.show()
limit = [-10.592, 1.6848, 50.681, 57.985]
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(df.Longitude, df.Latitude, zorder=1, alpha=0.2, c='b', s=50)
ax.set_title('Plotting of Grow Sensor location')
ax.set_xlim(limit[0], limit[1])
ax.set_ylim(limit[2], limit[3])
ax.imshow(ruh_m, zorder=0, extent=limit, aspect='equal')
plt.show()
