from library.connection import connection
import numpy as np
import cv2


class ekstraksi_ciri(connection):
    """
    pembuatan kelas ekstraksi ciri
    """

    def __init__(self):
        """
        constructor ekstraksi ciri
        """
        self.hello = "Hello"

    def get_rgb(self, data):
        """
        mendapatkan nilai RGB
        """
        img = None
        img = cv2.imdecode(np.fromstring(
            data.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        height, width = img.shape[:2]
        start_row, start_col = int(width*0.25), int(height*0.25)
        end_row, end_col = int(width*0.50), int(height*0.50)
        cropped = img[start_row:end_row, start_col:end_col]
        cv2.imshow("Cropped_Image", cropped)
        cv2.waitKey(0)
