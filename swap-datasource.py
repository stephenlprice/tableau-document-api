from tableaudocumentapi import Workbook

sourceWB = Workbook('./assets/workbooks/superstore.twb')

print('sourceWB ', 'type: ', type(sourceWB), '\n', sourceWB, '\n \n --------------- \n')

datasources = sourceWB.datasources

print('datasources ', 'type: ', type(datasources), '\n', datasources, '\n \n --------------- \n')



# connections = datasources.connections

# if (type())
# for connections in sourceWB.datasources:
#   print('sourceWB.datasources.connections: ', sourceWB.datasources.connections) 
