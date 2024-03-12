import os


class Paths:
    base = os.path.dirname(__file__)
    frontend = os.path.join(base, "frontend")
    images = os.path.join(frontend, "images")

    @classmethod
    def image(cls, image_name):
        return os.path.join(cls.images, image_name)
