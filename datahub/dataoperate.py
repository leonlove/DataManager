import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('dataoperate', __name__, url_prefix='/dataoperate')

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * from data'
    ).fetchall()
    return render_template('dataoperate/index.html', posts=posts)