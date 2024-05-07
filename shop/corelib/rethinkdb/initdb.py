# RETHINKDB
from rethinkdb import r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

@staticmethod
def init_database(host, port, database, password, table):
  conn = connect(host, port, database, password)
  try:
    conn = connect(host, port, database, password)
    databases = r.db_list().run(conn)
    exists = False
    for db_name in databases:
      if db_name == database:
        exists = True
        break
    if not exists:
      r.db_create(database).run(conn)
      print('Database %s created successfully'%(database))
    tables = r.db(database).table_list().run(conn)
    texists = False
    for tbl_name in tables:
      if tbl_name == table:
        texists = True
        break
    if not texists:
      r.db(database).table_create(table).run(conn)
      r.db(database).table(table).index_create('timestamp').run(conn)
      print('Table %s created successfully'%(table))
  except RqlRuntimeError as RqlRuntimeE:
    print(RqlRuntimeE)
    raise RqlRuntimeE
  except RqlDriverError as RqlDriverE:
    print(RqlDriverE)
    raise RqlDriverE
  finally:
    if conn:
      conn.close()

@staticmethod
def connect(host, port, database, password):
  return r.connect(host=host, port=port, db=database, password=password)
# import rethinkdb as r
# r.connect('192.168.11.77').repl()
# r.table('foo').delete().run()
# c = r.table('foo').changes(squash=1000000).run(changefeed_queue_size=10)
# r.table('foo').insert([{'id':0}, {'id':1}, {'id':2}, {'id':3}, {'id':4}, {'id':5}, {'id':6}]).get_field('inserted').run()
# for i in range(7): print c.next()
