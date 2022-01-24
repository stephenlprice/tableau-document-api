from tableaudocumentapi import Workbook
from tabulate import tabulate

sourceWB = Workbook('./assets/workbooks/Superstore.twbx')

print('\n', sourceWB.filename, '\n')
print('type:', type(sourceWB), '\n', sourceWB)
print('\n --------------- \n')

datasources = sourceWB.datasources

print('datasources', 'type:', type(datasources), '\n')
for datasource in datasources:
  print('datasource:', datasource)
print('\n --------------- \n')

print(datasource.connections)

for datasource in datasources:
  print(datasource.connections)
  print('\n --------------- \n')
  for connection in datasource.connections:
    print('connection', 'type:', type(connection), '\n', connection)
  print('\n ---------------')
print('\n --------------- \n')

# print('datasources ', 'type: ', type(datasources), '\n', tabulate(datasources), '\n \n --------------- \n')







# for connections in datasources:
#   print('connections: ', connections) 
