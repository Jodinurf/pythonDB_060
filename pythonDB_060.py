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
