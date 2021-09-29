import np


class LatLong:
    def __init__(self, img):
        self.h, self.w = img.h, img.w

    def LongfromX(self, x):
        return 360 * x / self.w - 180

    def LatfromY(self, y):
        return - np.arctan(np.sinh((y / self.h) * 2 * np.pi - np.pi)) * 180 / np.pi

    def XfromLong(self, long):
        return (x + 180) * self.w / 360

    def YfromLat(self, lat):
        y = (np.arcsinh(np.tan(lat * np.pi / 180)) + np.pi) * \
            self.h / (2 * np.pi)

__all__ = ["LatLong"]