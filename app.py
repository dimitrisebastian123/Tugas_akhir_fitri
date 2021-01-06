from flask import Flask, render_template, request as req
from flaskwebgui import FlaskUI
from library import library
app = Flask(__name__)
ui = FlaskUI(app)
libs = library()


@app.route('/', methods=['GET', 'POST'])
def index():
    if req.method == "GET":
        return render_template('content/index.html')
    else:
        return render_template('content/index.html')


@app.route('/ekstraksi_ciri', methods=['GET', 'POST'])
def ekstraksi_ciri():
    if req.method == 'GET':
        return render_template('content/extract.html')
    else:
        data = req.files['file']
        libs.ekstraksi_ciri.get_rgb(data)
        return render_template('content/extract.html')


@app.route('/pelatihan', methods=['GET', 'POST'])
def pelatihan():
    if req.method == 'GET':
        return render_template('content/pelatihan.html')
    else:
        data = req.form
        libs.lvq.params(
            data["epoch"],
            data["lr"],
            data["min_lr"],
            data["steps"]
        )
        libs.lvq.pelatihan()
        return render_template('content/pelatihan.html')


@app.route('/pengujian', methods=['GET', 'POST'])
def pengujian():
    if req.method == 'GET':
        return render_template('content/pengujian.html')
    else:
        return render_template('content/pengujian.html')


@app.errorhandler(404)
def not_founds(e):
    return render_template('content/404.html'), 404


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
