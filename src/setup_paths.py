import os


class Paths:
    base = os.path.dirname(__file__)
    frontend = os.path.join(base, "frontend")
    images = os.path.join(frontend, "__image")
    gif = os.path.join(images, "gif_elements")
    sales = os.path.join(images, "sales_elements")

    @classmethod
    def image(cls, image_name):
        return os.path.join(cls.images, image_name)

    @classmethod
    def getGif(cls, gif_name):
        return os.path.join(cls.gif, gif_name)

    @classmethod
    def getSalesElements(cls, element_name):
        return os.path.join(cls.sales, element_name)


if __name__ == '__main__':
    print(Paths.getGif("email.gif"))
