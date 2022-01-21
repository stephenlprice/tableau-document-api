from tableaudocumentapi import Workbook

sourceWB = Workbook('./assets/workbooks/superstore.twb')

print('*** sourceWB ', 'type: ', type(sourceWB), ' *** ', sourceWB)

datasources = sourceWB.datasources

print('sourceWB.datasources: ', datasources)

# connections = datasources.connections

# if (type())
# for connections in sourceWB.datasources:
#   print('sourceWB.datasources.connections: ', sourceWB.datasources.connections) 
