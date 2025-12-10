from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, db
from flask import request

# GET semua dosen
def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest([], "Terjadi kesalahan")

def formatArray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    return {
        "id": data.id,
        "nidn": data.nidn,
        "nama": data.nama,
        "phone": data.phone,
        "alamat": data.alamat
    }

# GET detail dosen + mahasiswa bimbingan
def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], "Tidak ada data dosen")

        mahasiswa = Mahasiswa.query.filter(
            (Mahasiswa.dosen_satu == id) |
            (Mahasiswa.dosen_dua == id)
        )

        datamahasiswa = formatMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen, datamahasiswa)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest([], "Terjadi kesalahan")

def singleDetailMahasiswa(dosen, mahasiswa):
    return {
        "id": dosen.id,
        "nidn": dosen.nidn,
        "nama": dosen.nama,
        "phone": dosen.phone,
        "alamat": dosen.alamat,
        "mahasiswa": mahasiswa
    }

def singleMahasiswa(mhs):
    return {
        "id": mhs.id,
        "nim": mhs.nim,
        "nama": mhs.nama,
        "phone": mhs.phone
    }

def formatMahasiswa(datas):
    array = []
    for i in datas:
        array.append(singleMahasiswa(i))
    return array

# POST tambah dosen
def save():
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosen = Dosen(
            nidn=nidn,
            nama=nama,
            phone=phone,
            alamat=alamat
        )

        db.session.add(dosen)
        db.session.commit()

        return response.success({}, "Data Berhasil Ditambah")
    except Exception as e:
        print(e)
        return response.badRequest([], "Gagal menambah data")
