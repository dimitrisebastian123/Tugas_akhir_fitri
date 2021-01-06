from library.ekstraksi_ciri import ekstraksi_ciri
from library.lvq_kelas import lvq_proses


class library():
    """
    pembuatan library untuk semua kelas library
    """

    def __init__(self):
        """
        constructor in class
        """
        self.ekstraksi_ciri = ekstraksi_ciri()
        self.lvq = lvq_proses()


if __name__ == "__main__":
    library
