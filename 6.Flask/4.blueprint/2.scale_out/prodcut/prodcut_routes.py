from flask import Blueprint, render_template

prodcut_bp = Blueprint('prodcut',__name__)

@prodcut_bp.route('/')
def user_page():
    return render_template('prodcut.html')

