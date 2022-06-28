from openpyxl import load_workbook
from bs4 import BeautifulSoup


# Function to remove tags
def remove_tags(html):
  
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
  
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


if __name__ == '__main__':

    wb = load_workbook(filename='osticket_ct.xlsx')
    for ws in wb.worksheets:
        for index, row in enumerate(ws.rows, start=1):
            # print(row[3].value)
            # print( remove_tags(row[3].value) ) 
            # print(index, ws.cell(row=index, column=4).value)
            x1 = remove_tags(row[3].value)
            ws.cell(row=index, column=4).value = x1

    # Save a new file
    wb.save(filename='osticket_ct_fixed.xlsx')
    wb.close()