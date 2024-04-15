import math
import matplotlib
import os
import numpy as np
from matplotlib import pyplot as plt


class pair:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt


def print_histogram_and_stuff(filepath):
    arrayprobs = []
    arrayvalorproprio = []

    totalcount = 0
    print(filepath)
    content = open("test/" + filepath, "rb").read()  # content = ficheiro
    lista = []
    cnt = 0

    # init the list
    while cnt < 256:
        lista.append(pair(cnt, 0))
        cnt += 1
    # deve funcionar ig
    for i in content:
        lista[i].cnt += 1
        totalcount += 1

    for x in range(256):
        if lista[x].cnt != 0:
            arrayprobs.append(lista[x].cnt / totalcount)
            arrayvalorproprio.append(-1 * math.log2(lista[x].cnt / totalcount))

    print("probabilidades e valores proprios:")
    print(arrayprobs)
    print(arrayvalorproprio)

    entropia = 0
    for i in range(len(arrayprobs) - 1):
        entropia += arrayprobs[i] * arrayvalorproprio[i]
    print("entropia:", entropia)

    x = []
    y = []
    for i in range(256):
        x.append(i)
        y.append(lista[i].cnt)
    print(x)

    x = np.array(x)
    y = np.array(y)

    plt.bar(x, y)
    plt.title(filepath)
    plt.xlabel(f"char     entropy ={entropia}")
    plt.ylabel(f"count")

    plt.show()


def main():
    # folder path
    dir_path = r'C:\Users\ferra\PycharmProjects\CD1\test\\'
    list = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            list.append(path)

    for path in list:
        print_histogram_and_stuff(path)


main()
#print_histogram_and_stuff("alice29.txt")
