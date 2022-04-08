
'''
#Program to write excel - openpyxl library - https://worldweather.wmo.int/en/json/full_city_list.txt
# open the https://worldweather.wmo.int/en/json/full_city_list.txt file and read
# create the excel file using openpyxl


OR we can use following code instead of download

import reuqests
data = requests.get("https://worldweather.wmo.int/en/json/full_city_list.txt")
print(data.text)
'''

import csv #importing csv package
from openpyxl import Workbook #importing openpyxl package
wb = Workbook() #creating a workbook
ws = wb.active #move to the active worksheet
f = open('worldweather.txt', 'r') #opening up the text file
data = csv.reader(f, delimiter=';') #iterate over the lines of file
for row in data:
    ws.append(row)
wb.save('worldweather.xlsx')
f.close()
