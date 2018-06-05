import matplotlib.pyplot as pt
import numpy as np
import random as rns
from io import StringIO

thrsehold = 1
content = []
x = []
y = []

with open("data.txt") as f:
    for line in f:
        line = line.rstrip('\n')
        ln = line.split(" ")
        x.append(float(ln[0]))
        y.append(float(ln[1]))

def get_error_for_hyp(th0, th1, x, y):
    error = 0
    b = np.array([[th0],[th1]])
    data = list()
    for x1 in x:
        data.append([x1,1])
    a = np.array(data)
    c = np.dot(a,b)
    h = c.tolist()
    for v in range(0, len(y)):
        e = y[v] - h[v][0]
        e = e*e
        error = error + e

    error = error / len(y)
    return error


def converge(seed, previousError, flip, depth):
    depth = depth + 1
    print(depth)
    if depth > 900:
        print("max depth")
        print(seed, previousError)
        return seed
    net_error = get_error_for_hyp(seed, 2.5, x, y)
    print(net_error)
    if net_error <= thrsehold:
        print("found %s"%seed)
        exit()
        return seed
    else:
        if net_error > previousError:
            if flip == 0:
                flip = 1
                seed = seed - 0.01
            else :
                flip = 0
                seed =seed + 0.01
        else:
            if flip == 0:
                seed = seed + 0.01
            else:
                seed =seed - 0.01
    converge(seed, previousError, flip, depth)



def main():
    th0 = converge(5, 1000, 1, 0)
    print(th0)

if __name__ == "__main__":
    main()

