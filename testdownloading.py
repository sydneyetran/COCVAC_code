# Import libraries
# source: https://www.geeksforgeeks.org/downloading-files-web-using-python/
import requests
from bs4 import BeautifulSoup
 
# URL from which pdfs to be downloaded
url = "https://ocgov.net/departments/emergency-services/911-summary-report//"
 
# Requests URL and get response object
response = requests.get(url)
 
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
 
# Find all hyperlinks present on webpage
links = soup.find_all('a')
 
i = 0
 
# From all links check for pdf link and
# if present download file
for link in links:
    if (('.pdf' in link.get('href'))):
        print("link is: " + link.get('href'))
        i += 1
        print("Downloading file: ", i)
 
        # Get response object for link
        print('https://ocgov.net' + (link.get('href')))
        try:
            response = requests.get('https://ocgov.net' + (link.get('href')))
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
 
        # Write content in pdf file
        if (i > 1):
            pdf = open("pdf"+str(i)+".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File ", i, " downloaded")
 
print("All PDF files downloaded")