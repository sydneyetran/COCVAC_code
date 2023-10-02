import tabula
import pandas as pd
import openpyxl
#import numpy as np
import sys

wb = openpyxl.Workbook() # create openpyxl object
sheet_name = wb.sheetnames # define sheetname for object
wb.save(filename = 'alltables.xlsx') # create empty excel file with openpyxl object

n = len(sys.argv) #take argument in command line

dframe = pd.read_excel('alltables.xlsx') #create empty pandas dataframe
first_data = tabula.read_pdf(sys.argv[1], pages = '1') #read first page of pdf
dframe = pd.concat([dframe, first_data[0]], ignore_index = False) # concatenate first page dataframe with empty pandas dataframe

dfdata = tabula.read_pdf(sys.argv[1], pages = 'all') # read all pdf pages and turn into list of pandas dataframes

# source: https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/
def createrange(v1, v2): #create list of consecutive numbers
    return list(range(v1, v2 + 1))
v1, v2 = 1, len(dfdata)

dfdata = tabula.read_pdf_with_template(input_path="sept23.pdf", template_path="mytemplate.json", pages = createrange(v1, v2))
# read pdf and convert pdf data into list of pandas dataframes for each page

for i in range(1, len(dfdata)): #for all dataframes in list of panda dataframes
    new_data = dfdata[i] #take current panda dataframe
    dframe = pd.concat([dframe, new_data], ignore_index = False) #concatenate dataframe onto other dataframes


# source: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html
newdf = dframe.loc[(dframe.Agency == "COCVAC")] #filter dataframe to only have COCVAC info


newdf.to_excel('alltables.xlsx', sheet_name = 'alltables', index = False) #convert dataframe into excel file

