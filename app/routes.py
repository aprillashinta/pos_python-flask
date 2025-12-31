from app import app
from app.controller import DosenController
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    return render_template('dashboard.html', content='Home')

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method == 'GET':
        return DosenController.index()
    return DosenController.save()

@app.route('/dosen/<id>', methods=['GET'])
def dosen_detail(id):
    return DosenController.detail(id)

@app.route('/admin/<name>')
def admin(name):
    return render_template('index.html', content=name)

@app.route('/success/<name>')
def success(name):
    return f"welcome {name}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nama']
        return redirect(url_for('success', name=user))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", content="Admin Sistem Akademik")

@app.route('/cv')
def cv():
    return render_template("cv.html")

@app.route('/cv2')
def cv2():
    return render_template("cv2.html")