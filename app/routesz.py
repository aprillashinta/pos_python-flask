from flask import render_template, request, redirect, url_for
from app import app
from app.controller import DosenController

@app.route('/')
def home():
    return render_template('index.html', content='Home')

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method == 'POST':
        return DosenController.save()
    return DosenController.index()

@app.route('/dosen/<int:id>')
def dosen_detail(id):
    return DosenController.detail(id)

@app.route('/admin/<string:name>')
def admin(name):
    return render_template('index.html', content=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('nama')
        return redirect(url_for('success', name=user))
    return render_template('login.html')

@app.route('/success/<string:name>')
def success(name):
    return f"welcome {name}"

@app.route('/cv')
def cv():
    return render_template('cv.html')
