import pandas as pd
import numpy as np
import sys
data = pd.read_csv('energydata_complete.csv', sep=",", header=0)
print(list(data.columns.values))
file = open("answers.txt","w")
for i in range(1,29):
    #i = int(sys.argv[1])
    print(i)
    col = data.iloc[:,[i]].values
    col = col.astype(float)
    k=data[i].quantile(q=.25).values
    q75, q25 = np.percentile(col, [75 ,25])
    iqr = q75 - q25
    ansI = [len(col),min(col)[0],max(col)[0],np.mean(col),np.std(col),q25,np.median(col),q75,iqr];
    #file.write("%s\n" % str(ansI))
file.close()