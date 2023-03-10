# Importing Libraries
import pandas as pd
import numpy as np



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #bllData = pd.read_csv(r"C:\Users\sharinic\Downloads\BLL_9317029_FyrMonitor_Rev0-Tags-RICK.csv", usecols=['Specifier','NAME'])
    #realData = pd.read_csv(r"C:\Users\sharinic\Downloads\REAL.CSV", usecols=['ItemName', 'Specifier'])
    #cllData = pd.read_csv(r"C:\Users\sharinic\Documents\CLL_9317029_FyrMonitor_Rev0-Tags-RICK.csv", usecols=['Specifier','NAME'])
    #b7Alias = pd.read_csv(r"C:\Users\sharinic\Downloads\Boiler7_Matrikon_Alias_CLL_2023.02.21.csv", usecols=['AliasName'])
    #b7AliasBLL = pd.read_csv(r"C:\Users\sharinic\Documents\Boiler7_Matrikon_Alias_2023.02.21_original - Copy.csv", usecols=['AliasName'])
    #kepList = pd.read_csv(r"C:\Users\sharinic\Downloads\Global.csv")
    #print("Boiler 7 Alias")
    #print(b7Alias.iloc[:10])   #usable tag list
    #print("Boiler 7 Alias BLL")
    #print(b7AliasBLL.iloc[:10])   #usable tag list
    #print("Global Kepware List")
    #print(kepList.iloc[:10]) #rovisys alias
    #print(cllData.iloc[:10])  #rovisys alias
    #output1 = pd.merge(realData, bllData, on='Specifier', how='left')
    #output2 = pd.merge(realData, cllData, on='Specifier', how='left')
    #output3 = pd.merge(b7Alias, kepList, on='AliasName', how='left')
    #output4 = pd.merge(b7AliasBLL, kepList, on='AliasName', how='left')
    #pd.options.display.max_columns = None
    #print(output1.iloc[5490:5525])
    #output1.to_csv(r'C:\Users\sharinic\Desktop\file3.csv')
    #print(output2.iloc[5490:5525])
    #output2.to_csv(r'C:\Users\sharinic\Desktop\file4.csv')
    #print(output3)
    #output3.to_csv(r'C:\Users\sharinic\Desktop\KepwareImport.csv')
    #print(output4)
    #output4.to_csv(r'C:\Users\sharinic\Desktop\KepwareImportBLL.csv')

    importCLL = pd.read_csv(r"C:\Users\sharinic\Desktop\KepwareImport.csv", usecols=['AliasName'])
    importBLL = pd.read_csv(r"C:\Users\sharinic\Desktop\KepwareImportBLL.csv", usecols=['AliasName'])
    output5 = pd.merge(importCLL, importBLL, on='AliasName', how='left')
    pd.options.display.max_columns = None
    print(output5)

