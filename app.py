"""The app module, containing the app factory function."""
from shop.app import create_app
from flask_socketio import SocketIO, send, emit
from threading import Thread
from flask import g
import shop.corelib.rethinkdb.initdb as InitDatabase
import shop.corelib.rethinkdb.db_read as RethinkRead

app = create_app()
socketio = SocketIO(app)
global thread
global thread1
thread = None
thread1 = None

@app.before_request
def before_request():
  InitDatabase.connect('localhost', 28015, 'flask_chat', 'Passw0rd!')

@app.teardown_request
def teardown_request(exception):
  try:
    g.db_conn.close()
  except AttributeError:
    pass

def watch_chats():
  print('Watching db for new chats!')
  feed = RethinkRead.GetChanges('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
  for chat in feed:
    chat['new_val']['created'] = str(chat['new_val']['created'])
    socketio.emit('new_chat', chat)

def watch_challenge():
  print('Watching db for new chats!')
  feed = RethinkRead.GetChanges('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
  for chat in feed:
    chat['new_val']['created'] = str(chat['new_val']['created'])
    socketio.emit('new_challenge', chat)

if __name__ == 'app':
  # app.run(host="0.0.0.0", debug=True, reload=True, port=8088)
   # Set up rethinkdb changefeeds before starting server
  if thread is None:
    thread = Thread(target=watch_chats)
    # thread1 = Thread(target=watch_challenge)
    thread.start()
    # thread1.start()
  socketio.run(app, host='0.0.0.0',  debug=True, reload=True, port=8088)