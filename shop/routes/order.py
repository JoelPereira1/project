import time
from datetime import datetime

from flask import (
    Blueprint,
    abort,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import current_user, login_required, login_user, logout_user
from shop.constant import OrderStatusKinds, PaymentStatusKinds, ShipStatusKinds
from shop.extensions import csrf_protect
from shop.models.order import Order, OrderPayment

order = Blueprint('order', __name__)

@login_required
@order.route('/order/')
def index():
  return redirect(url_for("account.index"))

@login_required
@order.route('/order/<string:token>')
def show(token):
  order = Order.query.filter_by(token=token).first()
  if not order.is_self_order:
    abort(403, "This is not your order!")
  return render_template("orders/details.html", order=order)

@order.route('/order/<int:id>')
def create_payment(token, payment_method):
  order = Order.query.filter_by(token=token).first()
  if order.status != OrderStatusKinds.unfulfilled.value:
    abort(403, "This Order Can Not Pay")
  payment_no = str(int(time.time())) + str(current_user.id)
  customer_ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
  payment = OrderPayment.query.filter_by(order_id=order.id).first()
  if payment:
    payment.update(
      payment_method=payment_method,
      payment_no=payment_no,
      customer_ip_address=customer_ip_address
    )
  else:
    payment = OrderPayment.create(
      order_id=order.id,
      payment_method=payment_method,
      payment_no=payment_no,
      status=PaymentStatusKinds.waiting.value,
      total=order.total,
      customer_ip_address=customer_ip_address
    )
  if payment_method == "alipay":
    breakpoint()
    # redirect_url = zhifubao.send_order(order.token, payment_no, order.total)
    # payment.redirect_url = redirect_url
  return payment

@login_required
@order.route('/order/<int:id>')
def ali_pay(token):
  payment = create_payment(token, "alipay")
  return redirect(payment.redirect_url)

@login_required
@order.route('/order/pay/<string:token>/testpay')
def test_pay_flow(token):
    payment = create_payment(token, "testpay")
    payment.pay_success(paid_at=datetime.now())
    return redirect(url_for("order.payment_success"))

@login_required
@order.route('/order/payment_success')
def payment_success():
    payment_no = request.args.get("out_trade_no")
    if payment_no:
        res = zhifubao.query_order(payment_no)
        if res["code"] == "10000":
            order_payment = OrderPayment.query.filter_by(
                payment_no=res["out_trade_no"]
            ).first()
            order_payment.pay_success(paid_at=res["send_pay_date"])
        else:
            print(res["msg"])

    return render_template("orders/checkout_success.html")

@login_required
@order.route('/order/cancel/<string:token>')
def cancel_order(token):
    order = Order.query.filter_by(token=token).first()
    if not order.is_self_order:
        abort(403, "This is not your order!")
    order.cancel()
    return render_template("orders/details.html", order=order)

@login_required
@order.route('/order//receive/<string:token>')
def receive(token):
  order = Order.query.filter_by(token=token).first()
  order.update(
    status=OrderStatusKinds.completed.value,
    ship_status=ShipStatusKinds.received.value,
  )
  return render_template("orders/details.html", order=order)

