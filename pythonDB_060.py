import tkinter as tk
import sqlite3
from tkinter import messagebox

def HasilPrediksi(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return 'Kedokteran'
    elif fisika > biologi and fisika > inggris:
        return 'Teknik'
    elif inggris > biologi and fisika:
        return 'Bahasa'
    else:
        return 'hasil belum dapat diprediksi'

def simpan_data_ke_sqlLite(nama_Siswa, biologi, fisika, inggris, prediksi_Fakultas):
    # membuka atau membuat database SQLite
    conn = sqlite3.connect("Prediksi_KelasB.db")
    cursor = conn.cursor()

    # membuat table jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_Siswa
        (nama_Siswa TEXT,
         biologi INTEGER, 
         fisika INTEGER,
         inggris INTEGER,
         prediksi_Fakultas TEXT)
    ''')

    cursor.execute('''
        INSERT INTO nilai_Siswa
        (nama_Siswa,
         biologi,
         fisika,
         inggris,
         prediksi_Fakultas) VALUES (?,?,?,?,?)
    ''', (nama_Siswa, biologi, fisika, inggris,prediksi_Fakultas))

    conn.commit()
    conn.close()

# Fungsi Untuk Menampilkan
def show():
    nama_Siswa = entry_Siswa.get()
    biologi = int(entry_Biologi.get())
    fisika = int(entry_Fisika.get())
    inggris = int(entry_Inggris.get())

    Prediksi = HasilPrediksi(biologi, fisika, inggris)

    hasilSiswa = f"Nama Siswa: {nama_Siswa}"
    hasil1 = f"Nilai Biologi: {biologi}"
    hasil2 = f"Nilai Fisika: {fisika}"
    hasil3 = f"Nilai Bahasa Inggris: {inggris}"
    hasil3 = f"Hasil Prediksi Fakultas : {Prediksi}"

    label_hasilSiswa.config(text=hasilSiswa)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)
    label_hasil3.config(text=hasil3)

   
    frame_hasil.pack()
    simpan_data_ke_sqlLite(nama_Siswa=nama_Siswa, biologi=biologi, fisika=fisika, inggris=inggris, prediksi_Fakultas=Prediksi)
    messagebox.showinfo("Info", f"Data tersimpan")
