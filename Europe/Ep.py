from flask import Blueprint, render_template

ep = Blueprint("ep",__name__, static_folder="static", template_folder="templates")

@ep.route('/Europe')
def Heurope():
    return render_template('europe.html')

@ep.route('/HpEurope')
def HpEurope():
    return render_template('')