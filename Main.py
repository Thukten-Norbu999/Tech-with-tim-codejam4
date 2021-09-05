from flask import Flask,render_template
from Asia.As import asia
from Europe.Ep import ep
from NA.Na import na
from Others.others import other

app = Flask(__name__)
app.register_blueprint(asia,url_prefix="")
app.register_blueprint(ep,url_prefix="")
app.register_blueprint(na,url_prefix="")
app.register_blueprint(other, url_prefix="")


@app.route('/Home')
@app.route('/')
def choose():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)