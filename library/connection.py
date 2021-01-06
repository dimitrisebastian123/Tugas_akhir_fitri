import mysql.connector
import numpy as np


class connection:
    """
    membuat kelas koneksi
    """

    def __init__(self):
        """
        membuat konstruktor untuk kelas koneksi
        """
        self.connect = None
        self.cursor = None
        self.np = np

    def open_database(self):
        self.connect = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='db_kain'
        )
        self.cursor = self.connect.cursor()

    def close_database(self):
        """
        menutup database
        """
        self.connect.close()
        self.cursor.close()

    def save_weight(self, bobot_awal, bobot_akhir):
        """
        menyimpan akurasi
        """
        print('bobot awal')
        print(bobot_awal)
        print('bobot akhir')
        print(bobot_akhir)
