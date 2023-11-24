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

# Buat Jendela Halaman
root = tk.Tk()
root.title("Prediksi Fakultas Pilihan")
root.geometry("500x500")
root.resizable(False, False)

# Label Judul
label_judul = tk.Label(root, text="Prediksi Fakultas Pilihan", font=("Times", 14, "bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n", pady=10, padx=10)
frame_input.pack()

# Label Nama siswa
label_nama_Siswa = tk.Label(frame_input, text="Nama Siswa: ")
label_nama_Siswa.grid(row=0, column=0, pady=10)
entry_Siswa = tk.Entry(frame_input)
entry_Siswa.grid(row=0, column=1)

# Label Nilai Biologi
label_Biologi = tk.Label(frame_input, text="Nilai Biologi: ")
label_Biologi.grid(row=1, column=0, pady=10)
entry_Biologi = tk.Entry(frame_input)
entry_Biologi.grid(row=1, column=1)

# Label Fisika
label_Fisika = tk.Label(frame_input, text="Nilai Fisika: ")
label_Fisika.grid(row=2, column=0, pady=10)
entry_Fisika = tk.Entry(frame_input)
entry_Fisika.grid(row=2, column=1)

# Label Inggris
label_Inggris = tk.Label(frame_input, text="Nilai Inggris: ")
label_Inggris.grid(row=3, column=0, pady=10)
entry_Inggris = tk.Entry(frame_input)
entry_Inggris.grid(row=3, column=1)

# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(root, labelanchor="n", padx=10, pady=10)
frame_hasil.pack_forget()

# Label Hasil
label_hasilSiswa = tk.Label(frame_hasil, text="")
label_hasilSiswa.pack()

label_hasil1 = tk.Label(frame_hasil, text="")
label_hasil1.pack()

label_hasil2 = tk.Label(frame_hasil, text="")
label_hasil2.pack()

label_hasil3 = tk.Label(frame_hasil, text="")
label_hasil3.pack()

label_hasil4 = tk.Label(frame_hasil, text="")
label_hasil4.pack()

# Jalankan Aplikasi
root.mainloop()