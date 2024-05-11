import time
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
from shop.models.challenge import Challenge, ChallengeImage

challenge = Blueprint('challenge', __name__, url_prefix='/challenge')

@login_required
@challenge.route('/')
def index():
  challenge = Challenge.query.order_by(Challenge.id.desc()).first()
  if challenge:
    challenge_images = Challenge.get_images_for_challenge(challenge.id)
    return render_template('challenge/index.html', challenge=challenge, challenge_images=challenge_images)
  flash('No Challenge', 'warning')
  return redirect(url_for('public.home'))
