from flask import Blueprint, render_template

other = Blueprint('other', __name__, static_folder='static', template_folder='templates')

@other.route('/Others')
def Others():
    return render_template('others.html')
