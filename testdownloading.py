# Import libraries
# source: https://www.geeksforgeeks.org/downloading-files-web-using-python/
import requests
from bs4 import BeautifulSoup
import os
import tabula
import pandas as pd
import openpyxl
import sys
import re
import shutil
from pathlib import Path

# path = 'thesispdfs'
# os.mkdir(path)

# URL from which pdfs to be downloaded
url = "https://ocgov.net/departments/emergency-services/911-summary-report//"
my_dir = "C:/Users/mmonroe/Desktop/COCVAC_code"
print(my_dir)
#text_file = open("C:/Users/sydneytran/thesis/downloadedpdfs.txt","r+") # open text file to keep track of downloaded pdfs
text_file = open(str(my_dir) + "/downloadedpdfs.txt","r+") # open text file to keep track of downloaded pdfs
#text_file_contents = text_file.read()

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0

# source: https://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# From all links check for pdf link and
# if present download file

new_downloads = []

for link in links:
    if (('.pdf' in link.get('href'))):
        #print("link is: " + link.get('href'))

        i += 1
        #print("Downloading file: ", i)

        # Get response object for link
        #print('https://ocgov.net' + (link.get('href')))
        try:
            response = requests.get('https://ocgov.net' + (link.get('href')))
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"



        # Write content in pdf file
        if (i > 1):
            print(i)
            with open(str(my_dir) + "/downloadedpdfs.txt") as f:
                contents = f.readlines()
            #print(contents)
            current_file = contents
            print(current_file)
            print("\n" + link.get('href'))
            if (link.get('href') + "\n" not in current_file):
                text_file.write(link.get('href') + "\n")
                new_downloads.append(link.get('href'))
                #print("the href wasn't in text file")
                #pdf = open("/Users/sydneytran/thesis/thesispdfs/" + "pdf" + str(i) + ".pdf", 'wb')
                #pdf = open("/Users/sydneytran/thesis/thesispdfs/" + link.get('href').split('/')[-1], 'wb')
                pdf = open(str(my_dir) + "/thesispdfs/" + link.get('href').split('/')[-1], 'wb')
                pdf.write(response.content)
                pdf.close()
                #print("File ", i, " downloaded")

print("new downloads: ")
print(new_downloads)

print("All PDF files downloaded")
directory = str(my_dir) + "/thesispdfs"
all_files = []

re_pattern = re.compile('.+?(\d+)\.([a-zA-Z0-9+])')
files_ordered = sorted(all_files, key = numericalSort)
files_ordered = sorted(all_files, key=lambda x: int(re_pattern.match(x).groups()[0]))
print(files_ordered)

k = 1
for file in new_downloads:
    wb = openpyxl.Workbook()  # create openpyxl object
    sheet_name = wb.sheetnames  # define sheetname for object
    print("file: ")
    print(file)
    file = file.split('/')
    print("file name minus excel")
    print(file[5])
    wb.save(filename=file[5] + ".xlsx")  # create empty excel file with openpyxl object

    #n = len(sys.argv)  # take argument in command line

    dframe = pd.read_excel(file[5] + ".xlsx")  # create empty pandas dataframe
    first_data = tabula.read_pdf(str(my_dir) + "/thesispdfs/" + file[5], pages="1")  # read first page of pdf
    dframe = pd.concat(
        [dframe, first_data[0]], ignore_index=False
    )  # concatenate first page dataframe with empty pandas dataframe

    dfdata = tabula.read_pdf(
        my_dir + "/thesispdfs/" + file[5], pages="all"
    )  # read all pdf pages and turn into list of pandas dataframes

    # source: https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/
    def createrange(v1, v2):  # create list of consecutive numbers
        return list(range(v1, v2 + 1))


    v1, v2 = 1, len(dfdata)

    dfdata = tabula.read_pdf_with_template(
        input_path=str(my_dir) + "/thesispdfs/" + file[5], template_path="mytemplate.json", pages=createrange(v1, v2)
    )
    # read pdf and convert pdf data into list of pandas dataframes for each page

    for i in range(1, len(dfdata)):  # for all dataframes in list of panda dataframes
        new_data = dfdata[i]  # take current panda dataframe
        dframe = pd.concat(
            [dframe, new_data], ignore_index=False
        )  # concatenate dataframe onto other dataframes


    # source: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html
    newdf = dframe.loc[
        (dframe.Agency == "COCVAC")
    ]  # filter dataframe to only have COCVAC info


    newdf.to_excel(
        file[5] + ".xlsx", sheet_name="alltables", index=False
    )  # convert dataframe into excel file
    shutil.move(file[5] + ".xlsx", str(my_dir) + "/thesispdfs/thesisexcels")  # move excel file into thesisexcels folder
    k += 1
