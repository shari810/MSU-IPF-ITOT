# Importing Libraries
import pandas as pd
import numpy as np
from keytotext import pipeline

########### Load the base pre-trained T5 model
########### It will download three files: 1. config.json, 2. tokenizer.json, 3. pytorch_model.bin (~850 MB)
#nlp = pipeline("k2t-base")

########### Configure the model parameters
#config = {"do_sample": True, "num_beams": 4, "no_repeat_ngram_size": 3, "early_stopping": True}

########### Provide list of keywords into the model as input
#print(nlp(['Ronaldo', 'football', 'Portuguese'], **config))

#dictionary of abr to word
#for each abr
    #parse segments of each and look for matching abv
    #store string
    #append to string
    #at end of loop at string to description column


Dict = {"HTR": 'Heater', "CV": 'Control Valve', "ERR": 'Error', "LIM": 'Limit', "AIR": 'Air', "BIAS": 'Bias',
        "VAL": 'Value', "NEG": 'Negative', "POS": 'Positive', "FLW": 'Flow',
        "TMP": 'Temperature', "IN": 'Inlet', "OUT": 'Outlet', "MAX": 'Maximum', "MIN": 'Minimum', 'PCT': 'Percentage',
        "COMP": 'Component' }

print(Dict)

importCLL = pd.read_csv(r"C:\Users\sharinic\Desktop\KepwareImport.csv")
nlp = pipeline("k2t-base")
config = {"do_sample": True, "num_beams": 10, "no_repeat_ngram_size": 0, "early_stopping": False, "repetition_penalty": 1}

rowNum = 0
for row in importCLL.Address.iloc[:10]: #use importCLL.Address.iloc[:10]  for small batch testing. Each sentence can take a full second to genereate.
    #print(row)
    #: str_obj.find(sub, start, end)
    descripStr = ""
    wordList = ['power plant', 'energy', 'electricity', 'boiler', 'steam generator']
    for key in Dict:
        #print(str(row))
        #print(key)
        if( str(row).find(key) != -1):  #Dict[key] gets value

            #print(Dict[key])
            #descripStr = descripStr + (Dict[key] + " ")   //add on to the string
            wordList.append(Dict[key])
            #print(descripStr)
    #importCLL.Description[rowNum] = descripStr  //this causes an error [DO NOT USE]
    #importCLL.at[rowNum,'Description'] = descripStr
    importCLL.at[rowNum, 'Description'] = nlp(wordList, **config)
    #print(descripStr)
    rowNum+=1
    print(wordList)
#print(importCLL.Description[0])
for row in importCLL.Description.iloc[:10]:
      print(row)
#importCLL.to_csv(r'C:\Users\sharinic\Desktop\kepwithdesc.csv')