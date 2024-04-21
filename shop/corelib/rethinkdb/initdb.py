# RETHINKDB
from rethinkdb import r

@staticmethod
def init_database(database, table):
  try:
    r.connect('rethinkdb', 28015).repl()
    r.db(database).table_create(table).run()
    print('Table %s created successfully'%(table))
  except:
    pass
  finally:
    return r
    # if conn:
    #   conn.close()
