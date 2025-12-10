from app import app
from app.controller import DosenController
from flask import render_template

@app.route('/')
def index():
    return 'Flask'

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


# from app import app

# @app.route('/')
# def index():
#     return 'Hello Aprillaa'
