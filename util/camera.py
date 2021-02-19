from picamera import PiCamera
from PIL import Image
from time import time, sleep
from io import BytesIO


class AstroCamera(PiCamera):

    @classmethod
    def with_settings_preset(cls):
        camera = cls(
            sensor_mode=3,  # 2592x1944
            framerate=1,
            resolution=(2592, 1944),
        )

        return camera

    def capture_astroimage(self):
        stream = BytesIO()
        self.capture(stream, 'jpeg', quality=100)
        stream.seek(0)
        img = Image.open(stream)
        img.id = str(round(time() * 1000))

        return img
