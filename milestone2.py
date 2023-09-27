import tabula
import pandas as pd
import openpyxl

wb = openpyxl.Workbook()
sheet_name = wb.sheetnames
wb.save(filename = 'alltables.xlsx')

dframe = pd.read_excel('alltables.xlsx') #create empty dataframe

dfdata = tabula.read_pdf('sept23.pdf', pages = 'all') #convert pdf to dataframe

for i in range(len(dfdata)):
    new_data = dfdata[i]
    dframe = pd.concat([dframe, new_data], ignore_index = False) #concatenate dataframes
#print(dframe)

dframe.to_excel('alltables.xlsx', sheet_name = 'alltables', index = False) 
dframe.to_csv('alltables.csv', index = False)

#dframe to csv file

# wbook = openpyxl.load_workbook('alltables.xlsx')

# ws = wbook.active
# ws.move_range("F406:J441", rows = 0, cols = -5)
# wbook.save('alltables.xlsx')
    

