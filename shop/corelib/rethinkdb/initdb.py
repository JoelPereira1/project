# RETHINKDB
from rethinkdb import r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

@staticmethod
def init_database(host, port, database, password, table):
  try:
    connection = connect(host, port, database, password)
    databases = r.db_list().run(connection)
    exists = False
    for db_name in databases:
      if db_name == database:
        exists = True
        break
    if not exists:
      r.db_create(database).run(connection)
    r.db(database).table_create(table).run(connection)
    print('Table %s created successfully'%(table))
    r.set_loop_type('asyncio')
  except Exception as e:
    raise e
  except RqlRuntimeError:
    print('aaaaaa')
  finally:
    return r
    # if conn:
    #   conn.close()

@staticmethod
def connect(host, port, database, password):
  return r.connect(host=host, port=port, db=database, password=password)
