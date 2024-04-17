# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import random
import smtplib
import string
from flask import abort, current_app, render_template, flash, request
from flask_login import current_user

from urllib.parse import urlencode


from shop.models.checkout import Cart
from shop.constant import SiteDefaultSettings
from shop.models.dashboard import Setting
from shop.corelib.template import template_hook
from shop.models.public import MenuItem

from flask import current_app, flash

def flash_errors(form, category="warning"):
  """Flash all errors for a form."""
  for field, errors in form.errors.items():
    for error in errors:
      flash(f"{getattr(form, field).label.text} - {error}", category)

def gen_tmp_pwd(size=8, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def send_reset_pwd_email(to_email, new_passwd):
    mailuser = current_app.config.get("MAIL_USERNAME")
    mailpwd = current_app.config.get("MAIL_PASSWORD")

    # msg = EmailMessage()
    # msg["To"] = email.utils.formataddr(("Recipient", to_email))
    # msg["From"] = email.utils.formataddr(("Admin", mailuser))
    # msg["Subject"] = "Reset Password"
    # body = render_template("account/reset_passwd_mail.html", new_passwd=new_passwd)
    # msg.set_content(body, "html")

    # with create_email_server() as s:
    #     s.login(mailuser, mailpwd)
    #     s.send_message(msg)

def jinja_global_varibles(app):
    """Register global varibles for jinja2"""

    @app.context_processor
    def inject_cart():
        current_user_cart = Cart.get_current_user_cart()
        return dict(current_user_cart=current_user_cart)

    @app.context_processor
    def inject_menus():
        top_menu = (
            MenuItem.query.filter(MenuItem.position == 1)
            .filter(MenuItem.parent_id == 0)
            .order_by(MenuItem.order)
            .all()
        )
        bottom_menu = (
            MenuItem.query.filter(MenuItem.position == 2)
            .filter(MenuItem.parent_id == 0)
            .order_by(MenuItem.order)
            .all()
        )
        return dict(top_menu=top_menu, bottom_menu=bottom_menu)

    @app.context_processor
    def inject_site_setting():
        settings = {}
        for key, value in SiteDefaultSettings.items():
            obj = Setting.query.filter_by(key=key).first()
            if not obj:
                obj = Setting.create(key=key, **value)
            settings[key] = obj
        return dict(settings=settings)

    def get_sort_by_url(field, descending=False):
        request_get = request.args.copy()
        if descending:
            request_get["sort_by"] = "-" + field
        else:
            request_get["sort_by"] = field
        return f"{request.path}?{urlencode(request_get)}"

    app.add_template_global(current_app, "current_app")
    app.add_template_global(get_sort_by_url, "get_sort_by_url")
    app.add_template_global(template_hook, "run_hook")
