from numpy.lib.scimath import sqrt
from library.connection import connection
import numpy as np


class lvq_proses(connection):
    """
    kelas lvq
    """

    def __init__(self):
        """
        constructor
        """
        self.bobot = None
        self.epoch = 0
        self.lr = 0.0
        self.min_lr = 0.0
        self.steps = 0.0
        self.target = 4
        self.akurasi = 0
        self.error = 0
        self.bobot_awal = None

    def reset_params(self):
        """
        reset Parameter
        """
        self.bobot = None
        self.bobot_awal = None
        self.epoch = 0
        self.lr = 0.0
        self.min_lr = 0.0
        self.steps = 0.0

    def define_bobot(self):
        bobot = []
        """
        mendefinisikan bobot awal
        """
        self.open_database()
        for i in range(self.target):
            self.cursor.execute(
                "select * from tb_ekstraksi_ciri where target = %d limit 1" % (i))
            data = self.cursor.fetchone()
            bobot.append(np.array(list(data)[2:5]))
        self.close_database()
        return bobot

    def params(self, epoch, learning_rate, minimum_learning_rate, steps):
        self.reset_params()
        self.bobot = self.define_bobot()
        self.bobot_awal = self.define_bobot()
        self.epoch = epoch
        self.lr = learning_rate
        self.min_lr = minimum_learning_rate
        self.steps = steps

    def pelatihan(self):
        """
        proses pelatihan
        """
        bobot_awal = None
        bobot_awal = self.bobot
        print("bobot awal ")
        print(self.bobot_awal)
        bobot_akhir = None
        akurasi = 0
        error = 0
        data = None
        lr = float(self.lr)
        dump = None
        self.open_database()
        self.cursor.execute(
            "select * from tb_ekstraksi_ciri order by rand() limit 10")
        dump = self.cursor.fetchall()
        self.close_database()

        for k in range(int(self.epoch)):
            for i in dump:
                data = np.array(list(i)[2:5])
                kelas = []
                for j in self.bobot:
                    val = (data-j)**2
                    res = sqrt(np.sum(val))
                    kelas.append(res)
                out = min(kelas)
                win = kelas.index(out)
                if win is i[5]:
                    akurasi += 1
                    print(
                        f"{self.bobot[win]} = {self.bobot[win]} + ({lr}*({data}-{self.bobot[win]}))")
                    self.bobot[win] = self.bobot[win] + \
                        (lr*(data-self.bobot[win]))
                else:
                    error += 1
                    print(
                        f"{self.bobot[win]} = {self.bobot[win]} -  ({lr}*({data}-{self.bobot[win]}))")
                    self.bobot[win] = self.bobot[win] - \
                        (lr*(data-self.bobot[win]))
                bobot_akhir = self.bobot
                print(bobot_akhir)
        self.save_weight(self.bobot_awal, bobot_akhir)
