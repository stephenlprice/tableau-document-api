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
dsList = []
for datasource in datasources:
  ds = str(datasource) # datasource class object typed to a string
  conn = [] # list of connections
  if len(datasource.connections) > 0:
    for connection in datasource.connections:
      if connection:
        conn.append(connection.dbclass) # not every datasource has a name but it will have connection information
      else:
        conn.append('none')
  else:
    conn.append('none')

  dsList.append([ds, conn]) # list all datasources along with a list of corresponding connections


print(f' *** There are {len(datasources)} datasources in this workbook ***')
print(f'The datasources object is of type: {type(datasources)}')
print(tabulate(dsList, headers=['Datasources', 'Connections'], showindex=True, tablefmt='fancy_grid'), '\n')


# describe datasource connections
print('******* Connections ******')
for datasource in datasources:
  print(f'***** Datasource: {datasource} length: {len(datasource.connections)} *******')
  for connection in datasource.connections:
    connList = {
      'Property': ['server', 'dbname', 'username', 'dbclass', 'port', 'query_band', 'initial_sql'],
      'Value': [connection.server, connection.dbname, connection.username, connection.dbclass, connection.port, connection.query_band, connection.initial_sql]
    }
    print('******* Each Connection ******')
    print('connection', 'type:', type(connection), '\n', connection)
    print(tabulate(connList, headers='keys', showindex=True, tablefmt='fancy_grid'))

  print('\n ---------------')
