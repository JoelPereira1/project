from rethinkdb import r
import shop.corelib.rethinkdb.initdb as InitDatabase
from uuid import uuid4
from datetime import datetime

# Module BbWrite:
def Insert(database, table, obj):
  conn = InitDatabase.connect('localhost', 28015, database, 'Passw0rd!')
  obj['id'] = str(uuid4())
  obj['created'] = datetime.now(r.make_timezone('00:00'))
  result = r.table(table).insert(obj, return_changes = True).run(conn)
  return result