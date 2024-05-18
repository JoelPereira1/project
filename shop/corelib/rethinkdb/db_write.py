from rethinkdb import r
import shop.corelib.rethinkdb.initdb as InitDatabase
from uuid import uuid4
from datetime import datetime
from settings import DBConfig

# Module BbWrite:
def Insert(database, table, obj):
  conn = InitDatabase.connect(DBConfig.rethinkdb_uri, DBConfig.rethinkdb_port, database, DBConfig.rethinkdb_pwd)
  obj['id'] = str(uuid4())
  obj['created'] = datetime.now(r.make_timezone('00:00'))
  result = r.table(table).insert(obj, return_changes = True).run(conn)
  return result