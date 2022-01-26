from tableaudocumentapi import Workbook

wb = Workbook('./assets/workbooks/Superstore.twbx')
ds = wb.datasources
conns = ds.connections

class ConnectionObj:
  """An object used to update datasource connection attributes"""
  def __init__(self, svr, dbn, usr, dbc, prt, qrb, sql):
    self.server = svr
    self.dbname = dbn
    self.username = usr
    self.dbclass = dbc
    self.port = prt
    self.query_band = qrb
    self.initial_sql = sql

def updateConnection(connection, ConnectionObj):
  # checks for empty connection objects
  try:
    type(connection) is not None
  except ValueError:
    print('This connection does not have a connection object!')
  # checks for missing object used to update connections
  try:
    type(ConnectionObj) is not None
  except ValueError:
    print('No ConnectionObj provided!')

  connection.server = ConnectionObj.server
  connection.dbname = ConnectionObj.dbname
  connection.username = ConnectionObj.username
  connection.dbclass = ConnectionObj.dbclass
  connection.port = ConnectionObj.port
  connection.query_band = ConnectionObj.query_band
  connection.initial_sql = ConnectionObj.initial_sql

conn1 = ConnectionObj('none', )
