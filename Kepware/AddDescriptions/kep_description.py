# Importing Libraries
import pandas as pd
import numpy as np


#dictionary of abr to word
#for each abr
    #parse segments of each and look for matching abv
    #store string
    #append to string
    #at end of loop at string to description column


Dict = {"HTR": 'Heater', "CV": 'Control Valve', "ERR": 'Error', "LIM": 'Limit', "AIR": 'Air'}

print(Dict)

importCLL = pd.read_csv(r"C:\Users\sharinic\Desktop\KepwareImport.csv")
rowNum = 0
for row in importCLL.Address:
    #print(row)
    #: str_obj.find(sub, start, end)
    descripStr = ""
    for key in Dict:
        #print(str(row))
        #print(key)
        if( str(row).find(key) != -1):  #Dict[key] gets value

            #print(Dict[key])
            descripStr = descripStr + (Dict[key] + " ")
            #print(descripStr)
    #importCLL.Description[rowNum] = descripStr
    importCLL.at[rowNum,'Description'] = descripStr
    #print(descripStr)
    rowNum+=1
#print(importCLL.Description[0])
for row in importCLL.Description:
      print(row)
importCLL.to_csv(r'C:\Users\sharinic\Desktop\kepwithdesc.csv')