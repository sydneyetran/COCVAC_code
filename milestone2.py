import tabula
import pandas as pd
import openpyxl
import numpy as np
import sys

wb = openpyxl.Workbook() #create openpyxl object
sheet_name = wb.sheetnames #define sheetname for object
wb.save(filename = 'alltables.xlsx') #create empty excel file with openpyxl object

n = len(sys.argv)


dframe = pd.read_excel('alltables.xlsx') #create empty panda dataframe

#dfdata = tabula.read_pdf('sept23.pdf', pages = 'all') #convert pdf to dataframe
dfdata = tabula.read_pdf(sys.argv[1], pages = 'all')

for i in range(len(dfdata)): #for all dataframes in list of panda dataframes
    new_data = dfdata[i] #take current panda dataframe
    print(new_data)
    #new_data.loc[new_data['Agency'] == "COCVAC"]
    dframe = pd.concat([dframe, new_data], ignore_index = False) #concatenate dataframe onto other dataframes


dframe.to_excel('alltables.xlsx', sheet_name = 'alltables', index = False) #convert dataframe into excel file

