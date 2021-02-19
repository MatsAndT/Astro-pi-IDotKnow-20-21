from picamera import PiCamera
from PIL import Image
from time import time, sleep
from io import BytesIO


class AstroCamera(PiCamera):

    @classmethod
    def with_settings_preset(cls):
        """Creates AstroCamera with our settings preset"""
        camera = cls(
            sensor_mode=3,  # 2592x1944
            framerate=1,
            resolution=(2592, 1944),
        )

        return camera

    def capture_astroimage(self):
        """Capture image and return as PIL.Image"""
        stream = BytesIO()
        self.capture(stream, 'jpeg', quality=100)
        stream.seek(0)
        img = Image.open(stream)
        img.id = str(round(time() * 1000))

        return img
