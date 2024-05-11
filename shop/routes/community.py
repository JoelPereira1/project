import time
from datetime import datetime
import json
from flask import (
    Blueprint,
    g,
    make_response,
    abort,
    redirect,
    render_template,
    request,
    url_for,
    flash,
    jsonify,
    current_app
)
from flask_login import current_user, login_required
from shop.extensions import csrf_protect
import shop.corelib.rethinkdb.initdb as InitDatabase
import shop.corelib.rethinkdb.db_write as RethinkWrite
import shop.corelib.rethinkdb.db_read as RethinkRead
from shop.constant import SUBMIT_METHODS

community = Blueprint('community', __name__, url_prefix='/community')

# # Function to establish the changefeed cursor
# def establish_changefeed():
#   try:
#     return RethinkRead.GetChanges('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
#   except Exception as e:
#     breakpoint()
#     print("Error establishing changefeed cursor:", e)
#     return None

# # Global variable to store the cursor
# message_cursor = establish_changefeed()

# Route to fetch messages with a changefeed
@community.route('/', methods=['GET'])
def index():
  chats = RethinkRead.GetAll('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
  # global message_cursor
  # # Establish the changefeed cursor if not already established
  # if not message_cursor:
  #   establish_changefeed()

  # # Fetch messages from the changefeed cursor
  # messages = []
  # try:
  #   for change in message_cursor:
  #     breakpoint()
  #   #   messages.append(change['new_val'])
  # except Exception as e:
  #   print("Error fetching messages:", e)


  return render_template('community/index.html', chats=chats, post_url = url_for('community.add'))

  return jsonify(messages), 200

# Route to send a message
@login_required
@community.route('/chat/add', methods=['POST'])
def add():
  if current_user:
    if is_submitted(request):
      data = json.loads(request.data)
      response = data['input']['message']
      obj = { 'user_id': current_user.id, 'response': response, 'challenge_id': None, 'chat_id': None }
      result = RethinkWrite.Insert('flask_chat', 'tblchat', obj)

      if result['inserted'] >= 0:
        return make_response('success!', 200)
      return make_response('invalid chat', 401)
        # global message_cursor

        # # Ensure the changefeed cursor is established
        # # if not message_cursor:
        # #   message_cursor = establish_changefeed()

        # if message_cursor:
        #   try:
        #     messages = []
        #     for message in message_cursor:
        #       breakpoint()
        #       messages.append(message['new_val'])

        #     # message_cursor.close()
        #     return jsonify(messages), 200
        #     # return render_template('community/index.html', chats=messages), 200
        #   except Exception as e:
        #     print("Error fetching messages:", e)
        #     return jsonify({'error': 'An error occurred while fetching messages'}), 500
        #   # finally:
        #   #   # Close the changefeed cursor when done
        #   #   message_cursor.close()
        # else:
        #   return jsonify({'error': 'Changefeed cursor is not available'}), 500

  # return redirect(url_for('community'))


# import time
# from uuid import uuid4
# from datetime import datetime
# import shop.corelib.rethinkdb.initdb as InitDatabase

# from flask import (
#     Blueprint,
#     abort,
#     redirect,
#     render_template,
#     request,
#     url_for,
#     flash,
#     jsonify
# )

# from flask_login import current_user, login_required
# from shop.extensions import csrf_protect
# import shop.corelib.rethinkdb.db_write as RethinkWrite
# import shop.corelib.rethinkdb.db_read as RethinkRead
# from shop.constant import SUBMIT_METHODS

# community = Blueprint('community', __name__, url_prefix='/community')
# # Global variable to store the cursor
# message_cursor = None

# # Function to establish the changefeed cursor
# def establish_changefeed():
#   global message_cursor
#   message_cursor = RethinkRead.GetAll('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)

# @community.route('/', methods=['GET', 'POST'])
# def index():
#   global message_cursor

#   # Establish the changefeed cursor if not already established
#   if not message_cursor:
#     establish_changefeed()

#   # Fetch messages from the changefeed cursor
#   messages = []
#   for change in message_cursor:
#     messages.append(change['new_val'])

#   return jsonify(messages), 200

#   # # Rethinkdb.init_database('rethinkdb', 28015, 'blogs', 'Passw0rd!', 'tblBosts')
#   # chats = RethinkRead.GetAll('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
#   # return render_template('community/index.html', chats=chats)

# @login_required
# @community.route('/chat/add', methods=['GET', 'POST'])
# def add():
#   if is_submitted(request):
#     response = request.form.get('chat')
#     obj = { 'id': str(uuid4()), 'user_id': current_user.id, 'response': response, 'challenge_id': None, 'chat_id': None }
#     result = RethinkWrite.Insert('flask_chat', 'tblchat', obj)
#     chats = RethinkRead.GetAll('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
#     return render_template('community/index.html', chats=chats)

#   return redirect(url_for('community'))

#   # if is_submitted(request):
#   #   r.table('todos').insert({"name":form.label.data}).run(g.rdb_conn)
#   #   return redirect(url_for('index'))
#   # selection = list(r.table('todos').run(g.rdb_conn))
  # return render_template('index.html', form = form, tasks = selection)

# @login_required
# @community.route('/chat/responde', methods=['GET', 'POST'])
# def responde(chat_id):

#   if is_submitted(request):
#     response = request.form.get('chat')
#     obj = { 'id': str(uuid4()), 'user_id': current_user.id, 'response': response, 'challenge_id': None, 'chat_id': chat_id }
#     breakpoint()

#   abort(403, "This is not your order!")
#   return render_template("orders/details.html", order=order)

@staticmethod
def is_submitted(request):
  """Consider the form submitted if there is an active request and
  the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
  """
  return bool(request) and request.method in SUBMIT_METHODS