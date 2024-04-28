import time
from rethinkdb import r
import shop.corelib.rethinkdb.initdb as InitDatabase

# Module DbRead
@staticmethod
def GetAll(database, table, ref_col, ref_id, order_col, limit = False, limit_num = 3, limit_col = None):
  conn = InitDatabase.connect('localhost', 28015, database, 'Passw0rd!')
  cursor = r.table(table).changes().run(conn, timeout=1.0)

  # Process the data in batches
  for change in cursor:
    print(change)

    # Wait for a short period before checking for new data again
    time.sleep(0.1)
  # cursor = r.table(table).run(conn)
  # cursor = r.table(table).get(1).changes(include_initial=True, include_states=True).run(conn)
  # my_array= []
  # for change in r.table(table).changes(include_initial=True, include_offsets=True).run(conn):
  #   # delete item at old_offset before inserting at new_offset
  #   if change.old_offset != None:
  #     my_array.pop(change.old_offset)
  #   if change.new_offset != None:
  #     my_array.insert(change.new_offset, change.new_val);
  # return cursor
  # if limit:
  #   return print() if limit_col == None else r.table(table).filter(r.row['%s'%(ref_col)] > ref_id).order_by(order_col).limit(limit_num).changes() #r.table(table).orderBy(order_col).limit(limit_num).changes()
  # elif ref_col:
  #   r.table(table).filter(r.row['%s'%(ref_col)] > ref_id).order_by(order_col).changes()
  # else:
  #   r.table(table).order_by(order_col).changes()

    # r.db("Test").table('Users').getAll(r.args(r.db('Test').table('Users').get("0ab43d81-b883-424a-be56-32f9ff98f7d2")('friends'))).changes()

  # Subscribe to changes on the documents with the two lowest ids
  # EventMachine.run {
  #   r.table(table).order_by(:index => 'id').limit(2).changes
  #     .em_run(conn, FeedPrinter)
  # }