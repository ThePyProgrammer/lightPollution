import numpy as np

def maclaurin(x, y, inf=100):
    return (np.polyfit(x, y, inf)[:, np.newaxis] * (x ** np.arange(inf, -1, -1)[:, np.newaxis])).sum(axis=0)