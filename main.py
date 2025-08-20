import requests;
from bs4 import BeautifulSoup
import numpy as np

def readIn(urlInput):
    response = requests.get(url=urlInput)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    table_data = []
    for row in table.find_all("tr"):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
        table_data.append(row_data)

    np_table_data = np.array(table_data)
    return np_table_data[1:]


def printOut(np_table_data):


    left = np_table_data[:, 0].astype(int)
    right = np_table_data[:, 2].astype(int)


    sorted = np.lexsort((right, left))
    np_table_data = np_table_data[sorted]

    temp_array = np.empty(([max(right)+1, max(left)+1]), dtype=str)

    secret_message = np.full_like(temp_array, fill_value = " ", dtype=str)


    for x in np_table_data:
        secret_message[int(x[2])][int(x[0])] = x[1]

    
    
    for x in secret_message[::-1]:
        for y in x:
            print(y, end='')
        print()
        
def runProgram(url):
    printOut(readIn(url))
    

