from openpyxl import Workbook
from openpyxl import load_workbook
import datetime
import matplotlib.pyplot as plt

import json
file_name = 'dataset.xlsx'
wb = load_workbook(filename=file_name)
ws1 = wb.active


gbl_arr = []

gbl_table = {}

for row in range(2, 4370):
    gbl_arr.append(ws1['A'+str(row)].value)
    gbl_table[ws1['A'+str(row)].value] = {}
    temp = gbl_table[ws1['A'+str(row)].value]
    temp['detection_date'] = str(ws1['B'+str(row)].value)
    temp['notes'] = str(ws1['C'+str(row)].value)
    temp['lab_status'] = str(ws1['D'+str(row)].value)
    temp['lab_comments'] = str(ws1['E'+str(row)].value)
    temp['submission_date'] = str(ws1['F'+str(row)].value)
    temp['latitude'] = str(ws1['G'+str(row)].value)
    temp['longitude'] = str(ws1['H'+str(row)].value)

f = open('dataset.json', 'w', encoding='utf-8')

json.dump(gbl_table, f)

f.close()

