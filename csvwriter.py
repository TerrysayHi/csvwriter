# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:29:42 2018

@author: zeyi_
"""

#output mutiple dataframes into same csv file 
import pandas as pd
df1=pd.DataFrame([[1,2,3],[2,3,4]],columns=['a','c','l'])
df2=pd.DataFrame([[5,2,3,'afi'],[78,3,4,93]],columns=['ab','p','d','l'])
list_output=[df1,df2]

import csv
file_path="C:/Users/zeyi_/Desktop/test/mydata2.csv"
with open(file_path,"w", newline='') as datacsv:
    csvwriter = csv.writer(datacsv,dialect=("excel"))
    for df_sub in list_output:
        csvwriter.writerow(list(df_sub))
        for index,row in df_sub.iterrows():
            csvwriter.writerow(row)
        csvwriter.writerow([""])
        csvwriter.writerow([""])