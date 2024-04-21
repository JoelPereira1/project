import shop.corelib.rethinkdb.initdb as InitDatabase

# Module DbRead
@staticmethod
def GetAll(database, table, ref_col, ref_id, order_col, limit = False, limit_num = 3, limit_col = None):
  r = InitDatabase.init_database(database, table)
  if limit:
    return print() if limit_col == None else r.table(table).filter(r.row['%s'%(ref_col)] > ref_id).orderBy(order_col).limit(limit_num).changes() #r.table(table).orderBy(order_col).limit(limit_num).changes()
  else:
    r.table(table).filterfilter(r.row['%s'%(ref_col)] > ref_id).orderBy(order_col).changes()