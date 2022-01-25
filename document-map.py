from tableaudocumentapi import Workbook
from tabulate import tabulate
from colorama import init, deinit, Fore, Back, Style
import textwrap

# On Windows, colorama init() filters out stdout and stderr replaces them with standard Win32 calls
init()

# describe the workbook file and object
sourceWB = Workbook('./assets/workbooks/Superstore.twbx')
wbPath = sourceWB.filename
wbName = sourceWB.filename.rsplit('/', 1)[-1]

# to be used when text needs to be wrapped to fit inside of table cells
wrapper = textwrap.TextWrapper(width=33)

print(Fore.BLUE + f'\n *** Analyzing Tableau {wbName} ***\n')
print(Fore.RESET + f'The file is located at {wbPath}')
print(f'The workbook object is of type: {type(sourceWB)} \n')

# describe datasources
print(Fore.RED + f'\n *** Datasources ***\n')
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


print(Fore.RESET + f'There are {len(datasources)} datasources in this workbook')
print(f'The datasources object is of type: {type(datasources)}')
print(Fore.RED+ tabulate(dsList, headers=['Datasources', 'Connections'], showindex=True, tablefmt='fancy_grid'), '\n')


# describe datasource connections
print(Fore.YELLOW + f'\n *** Connection Details ***\n')
for datasource in datasources:
  print(Fore.RESET + 'Datasource ' + Fore.RED + f'{datasource} ' + Fore.RESET + f'has a total of {len(datasource.connections)} connections')
  if len(datasource.connections) < 1:
    print('Connection type cannot be described...\n')
  for connection in datasource.connections:
    connList = {
      'Property': ['server', 'dbname', 'username', 'dbclass', 'port', 'query_band', 'initial_sql'],
      'Value': [connection.server, connection.dbname, connection.username, connection.dbclass, connection.port, connection.query_band, connection.initial_sql]
    }
    print('connection type:', type(connection), connection, '\n')
    print('Connection details:')   
    print(Fore.YELLOW + tabulate(connList, headers='keys', showindex=True, tablefmt='fancy_grid'), '\n')

  fieldList = []
  for field in datasource.fields.values():
    fieldObj = {
      'Name': field.name,
      'Datatype': field.datatype,
      'Calculation': wrapper.fill(field.calculation) if field.calculation else '', # long text must be wrapped so it fits in table cells
      'Default Aggregation': field.default_aggregation,
      'Description': wrapper.fill(field.description) if field.description else '' # long text must be wrapped so it fits in table cells
    }

    fieldList.append(fieldObj)
  print(Fore.RESET + 'Field Details')
  print(Fore.CYAN + tabulate(fieldList, headers='keys', showindex=True, tablefmt='fancy_grid'))

  print(Fore.RESET + '\n ------------------------------------------------------------------------------\n')

# Stops colorama filtering stdout and stderr on Win32
deinit()
