#Using pandas lib to retrieve data from an excel file and define all its data in python, requires uniform filling
import pandas as pd

table = pd.read_excel(input('Enter absolute file path of excel file or place file in parent folder and enter file name: '))

#overwrites or creates file to write to
file = open(input('Enter new python file name: ')+'.py','w')

#create class named after upper left slot and define each attribute by column headers
file.write('class '+str(table.columns[0])+':\n\tdef __init__(self,'+', '.join(table.columns)+'):\n')
for i in range(len(table.columns)):
    file.write('\t\tself.'+str(table.columns[i])+' = '+str(table.columns[i])+'\n')

#define each row as class with each attribute defined by data in row
for i in range(len(table.index)):
    attrList = []
    for j in range(len(table.columns)):
        if j > 1:
            attrList.append(str(table.iloc[i,j]))
    if i > 0:
      file.write('\n'+str(table.iloc[i,0])+' = '+table.columns[0]+'(\''+'\', \''.join(attrList)+'\')')