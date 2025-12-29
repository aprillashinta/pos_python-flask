from app import app
from app.controller import DosenController
from flask import render_template

@app.route('/')
def index():
    return render_template(
        "dashboard.html",
        content="Admin Sistem Akademik"
    )

# @app.route('/')
# def index():
#     render_template("dashboard.html", content="Admin Sistem Akademik")
    # return 'Flask'

# GET semua dosen / POST tambah dosen
@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    from flask import request
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.save()

# GET detail dosen + mahasiswa
@app.route('/dosen/<id>', methods=['GET'])
def dosenDetail(id):
    return DosenController.detail(id)

@app.route('/admin/<name>')
def admin(name):
    return render_template("index.html", content=name)

# @app.route('/dashboard')
# def dashboard():
#     return render_template("dashboard.html", content="Admin Sistem Akademik")

# @app.route('/cv')
# def cv():
#     return render_template("cv.html")


# from app import app

# @app.route('/')
# def index():
#     return 'Hello Aprillaa'

# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET']) 
# def login():
#     if request.method == 'POST':
#         user = request.form['nama']
#         return redirect(url_for('success',name = user))
#     else:
#         return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f"welcome {name}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nama']
        return redirect(url_for('success', name=user))
    return render_template('login.html')