from flask import Blueprint, render_template

na = Blueprint("na", __name__,static_folder='static', template_folder='templates')

@na.route('/NA')
def NA():
    return render_template('na.html')