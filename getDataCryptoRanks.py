import requests
import pandas as pd
from bs4 import BeautifulSoup

##class CryptoRank():

def saveDataFramtoExcel(data_Frame, file_name):
    ##save dataframe to excel sheet
    data_Frame.to_excel(file_name,index=False)

def getDataFromCryptorank(url,element_name,element_class):
    # define variables
    html_parser = 'html.parser'
    th_name='th'
    tr_name='tr'
    td_name='td'
    fileName='./OutputData/cryptoRanks.xlsx'

    # Send a GET request to the website
    response = requests.get(url)
   # Create BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, html_parser)

   # Find the table class
    table = soup.find(element_name, class_=element_class) #'sc-9c013256-0 jpxjvC')

   # Extract the table column headers = names
    column_names = [th.text for th in table.find_all(th_name)]

   # Create an empty dictionary to save the table data
    data = {column: [] for column in column_names} 

# Extract the table rows
    rows = table.find_all(tr_name)[1:]  # find all records = rows = tr HTML and skip the header row : I do not need the column name 

# Extract the data from each row
    for row in rows:
        cells = row.find_all(td_name) 
        for i, cell in enumerate(cells):
            data[column_names[i]].append(cell.text.strip())

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    print(df)
    
    # Save the DataFrame to an Excel file
    # call save datafram in excel function: saveDataFramtoExcel
    saveDataFramtoExcel(df,fileName) 

# Define parameters to call the function
#url = 'https://cryptorank.io/all-coins-list/'
#element_name='table'
#element_class='sc-9c013256-0 jpxjvC' 

# execute my function: getDataFromCryptorank 
#getDataFromCryptorank(url,element_name,element_class)


# Get Data from a new website Define parameters to call the function
url = 'https://cryptorank.io/exchanges?sort=fullName&direction=desc'
element_name='table'
element_class='sc-9c013256-0 jpxjvC' 

# execute my function: getDataFromCryptorank 
getDataFromCryptorank(url,element_name,element_class)