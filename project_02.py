import json
import matplotlib.pyplot as plt
import csv
from sys import builtin_module_names
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

with open('airlines_dataset.json','rb') as f:
    text= f.read()
    text=text.decode('utf-8')
    airline_data=json.loads(text)

cancellations=[]
code=[]
for d in range(len(airline_data)):
    if airline_data[d]['Time']['Year']==2016:
        code.append(airline_data[d]['Airport']['Code'])
        cancellations.append(airline_data[d]['Statistics']['Flights']['Cancelled'])

data=pd.read_csv('studentdata.csv')
df=pd.DataFrame(data)
x=list(df.iloc[:,0])
y=list(df.iloc[:,1])
data_1=pd.read_csv('extrastudentdata.csv')
fd=pd.DataFrame(data_1)
xx=list(fd.iloc[:,0])
yy=list(fd.iloc[:,1])

plt.plot(x,y, c='b', marker='x', label='Students over the age of 11')
plt.plot(x, yy, c='r', marker='s', label='Students under the age of 11')
plt.legend(loc='upper right')
plt.title("Number of Students over the age of 11")
plt.xlabel("Year")
plt.ylabel("Number of Students")
plt.tight_layout
plt.show()

fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.barh(code,cancellations, color='b')
plt.xlabel("# of Canceled flights")
plt.ylabel("Airport Code")
plt.title('Number of canceled flights per airport for the year 2016')
plt.tight_layout()
plt.show()

