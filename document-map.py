from tableaudocumentapi import Workbook
from tabulate import tabulate

# describe the workbook file and object
sourceWB = Workbook('./assets/workbooks/Superstore.twbx')
wbPath = sourceWB.filename
wbName = sourceWB.filename.rsplit('/', 1)[-1]

print(f'\n *** Analyzing Tableau workbook {wbName} ***\n')
print(f'The file is located at {wbPath}')
print(f'The workbook object is of type: {type(sourceWB)} \n')

# describe datasources
datasources = sourceWB.datasources
dsList = {}
for index, datasource in enumerate(datasources):
  # tabulate() requires a list of lists containing the object typed as a string as it cannot iterate over class objects
  dsList.index = str(datasource)
  # for connection in datasource.connections:


print(f'There are {len(datasources)} datasources in this workbook')
print(f'The datasources object is of type: {type(datasources)}')
print(tabulate(dsList, headers=['Datasources', 'Connections'], showindex=True, tablefmt='fancy_grid'), '\n')


# describe datasource connections
for datasource in datasources:
  if (len(datasource.connections) > 0):
    print(datasource.connections)
    print('\n --------------- \n')
    for connection in datasource.connections:
      table = {
        'Property': ['server', 'dbname', 'username', 'dbclass', 'port', 'query_band', 'initial_sql'],
        'Value': [connection.server, connection.dbname, connection.username, connection.dbclass, connection.port, connection.query_band, connection.initial_sql]
      }
      
      print('connection', 'type:', type(connection), '\n', connection)
      print(tabulate(table, headers='keys', showindex=True, tablefmt='fancy_grid'))

    print('\n ---------------')
