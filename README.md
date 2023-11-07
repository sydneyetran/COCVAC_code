## About the Project
This repository is a part of a larger senior seminar/ thesis project at Hamilton College. We are collaborating with the [Central Oneida County Volunteer Ambulance Corps](https://www.cocvac.org/) to scrape 911 call data, analyse it, and display reports in a UI in order to understand where future EMS resources should be devoted.


## Learn More
This code is only a small part of our entire project. To learn more, visit our [Thesis Repository](https://github.com/cocvac-hamilton2023/thesis_ui) for our user interface.

### Daily Python Script

Our plan is to turn our current Python code into an executable and run it everyday to complete the following two tasks: 

#### Scraping 911 Call Data PDFs

[911 call data for Oneida County](https://ocgov.net/departments/emergency-services/911-summary-report/) is stored online. Everyday, a new PDF containing the previous day's call data is uploaded online. We want to scrape these PDFs everyday so that we can work with them locally.

#### Converting PDFs to Excel

Once we have the PDFs, we need to convert the PDF data into a tabular form so that the data can be used later in Power BI. We are able to do this by using 4 libraries: Tabula, Pandas, Openpyxl, and Sys. Sys allows us to take the PDF file as an argument when running the code from the terminal. Tabula is used to read the PDF information. We use a template with Tabula so that no data is lost or missed in the conversion process. The Tabula objects are described as a list of Pandas Dataframes. We convert the Pandas dataframes into an Excel file. Openpyxl allows us to create an empty excel file that is later edited when we add our 911 call data to the different cells. This is where the dataframe data is stored and at the end of this process, we have all of our 911 call data for the day stored in an Excel workbook.

### Folder Storage

Once the Excel Workbook with a day's 911 call data is created, it is added to a folder for 911 call data. This folder is stores Excel Worksheets. A new workbook is stored for each day of 911 call data.
