import numpy as np


def calculate(list):
    if len(list) > 9 or len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    lt = np.array(list)

    l1 = lt.reshape((3, 3))
    meanx1 = np.mean(l1, axis=0)
    meanx2 = np.mean(l1, axis=1)
    meanl1 = meanx1.tolist()
    meanl2 = meanx2.tolist()

    l2 = l1.flatten()
    meanf = np.mean(l2)

    var1 = np.var(l1, axis=0)
    var2 = np.var(l1, axis=1)
    varf = np.var(l2)
    varl1 = var1.tolist()
    varl2 = var2.tolist()

    std1 = np.std(l1, axis=0)
    std2 = np.std(l1, axis=1)
    stdf = np.std(l2)
    stdl1 = std1.tolist()
    stdl2 = std2.tolist()

    max1 = np.amax(l1, axis=0)
    max2 = np.amax(l1, axis=1)
    maxf = np.amax(l2)
    maxl1 = max1.tolist()
    maxl2 = max2.tolist()

    min1 = np.amin(l1, axis=0)
    min2 = np.amin(l1, axis=1)
    minf = np.amin(l2)
    minl1 = min1.tolist()
    minl2 = min2.tolist()

    sum1 = np.sum(l1, axis=0)
    sum2 = np.sum(l1, axis=1)
    sumf = np.sum(l2)
    suml1 = sum1.tolist()
    suml2 = sum2.tolist()

    calculations = {
        'mean': [meanl1, meanl2, meanf],
        'variance': [varl1, varl2, varf],
        'standard deviation': [stdl1, stdl2, stdf],
        'max': [maxl1, maxl2, maxf],
        'min': [minl1, minl2, minf],
        'sum': [suml1, suml2, sumf]
    }
    return calculations


print(calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))
