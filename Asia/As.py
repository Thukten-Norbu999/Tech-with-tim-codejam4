from flask import Blueprint,render_template
asia = Blueprint("asia", __name__, static_folder="static",template_folder="template" )

@asia.route("/Asia")
def Hasia():
    return render_template('asia.html')

@asia.route('/Ahelpline')
def Ahelpline():
    return render_template('asia.html')