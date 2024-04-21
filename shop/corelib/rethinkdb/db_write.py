import shop.corelib.rethinkdb.initdb as InitDatabase

# Module BbWrite:
def Insert(database, table, obj):
  r = InitDatabase.init_database(database, table)
  result = r.table(table).insert(obj).run()
  return result