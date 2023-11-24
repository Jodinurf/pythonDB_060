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
