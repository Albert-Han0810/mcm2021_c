from openpyxl import Workbook
from openpyxl import load_workbook
import datetime
import matplotlib.pyplot as plt
import re
import json

file_name = "image_global.xlsx"
wb = load_workbook(filename=file_name)
ws1 = wb.active


my_table = {}

for row in range(2, 3307):
    my_table[ws1['B'+str(row)].value] = {}
    temp = my_table[ws1['B'+str(row)].value]
    temp['filename'] = ws1['A'+str(row)].value
    temp['filetype'] = ws1['C'+str(row)].value

f = open('image_global.json', 'w', encoding='utf-8')

json.dump(my_table, f)

f.close()
