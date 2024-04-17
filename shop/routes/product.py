import random
import smtplib
import string
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import current_user, login_required, login_user, logout_user

product = Blueprint('product', __name__)