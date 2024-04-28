import time
from uuid import uuid4
from datetime import datetime

from flask import (
    Blueprint,
    abort,
    redirect,
    render_template,
    request,
    url_for,
    flash
)

from flask_login import current_user, login_required, login_user, logout_user
from shop.constant import OrderStatusKinds, PaymentStatusKinds, ShipStatusKinds
from shop.extensions import csrf_protect
import shop.corelib.rethinkdb.db_write as RethinkWrite
import shop.corelib.rethinkdb.db_read as RethinkRead
from shop.constant import SUBMIT_METHODS

community = Blueprint('community', __name__, url_prefix='/community')

@community.route('/', methods=['GET', 'POST'])
def index():
  # Rethinkdb.init_database('rethinkdb', 28015, 'blogs', 'Passw0rd!', 'tblBosts')
  chats = RethinkRead.GetAll('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
  # n = 7
  # for i in range(n):
  #   # n is excluded
  #   obj = {'id': i, 'customer_id': 3, 'response': 'Hi', 'daily_id': 3, 'chat_id': 3}
  #   print(obj)
  #   RethinkBbWrite.Insert('blogs', 'tblBosts', obj)
  return render_template('community/index.html', chats=chats)

@login_required
@community.route('/chat/add', methods=['GET', 'POST'])
def add():
  if is_submitted(request):
    response = request.form.get('chat')
    obj = { 'id': str(uuid4()), 'user_id': current_user.id, 'response': response, 'challenge_id': None, 'chat_id': None }
    result = RethinkWrite.Insert('flask_chat', 'tblchat', obj)
    chats = RethinkRead.GetAll('flask_chat', 'tblchat', None, None, 'id', limit = False, limit_num = 6, limit_col = None)
    return render_template('community/index.html', chats=chats)

  return redirect(url_for('community'))

  # if is_submitted(request):
  #   r.table('todos').insert({"name":form.label.data}).run(g.rdb_conn)
  #   return redirect(url_for('index'))
  # selection = list(r.table('todos').run(g.rdb_conn))
  # return render_template('index.html', form = form, tasks = selection)

@login_required
@community.route('/chat/responde', methods=['GET', 'POST'])
def responde(chat_id):

  if is_submitted(request):
    response = request.form.get('chat')
    obj = { 'id': str(uuid4()), 'user_id': current_user.id, 'response': response, 'challenge_id': None, 'chat_id': chat_id }
    breakpoint()

  abort(403, "This is not your order!")
  return render_template("orders/details.html", order=order)

@staticmethod
def is_submitted(request):
  """Consider the form submitted if there is an active request and
  the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
  """
  return bool(request) and request.method in SUBMIT_METHODS