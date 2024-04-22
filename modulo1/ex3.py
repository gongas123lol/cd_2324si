import math
import matplotlib
import os
import numpy as np
from matplotlib import pyplot as plt

#3-A-
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
#..........................................................
#3-b-

def calculate_symbol_frequency(text):
    text = text.replace('\n', '')
    frequencies = {}
    total_characters = 0

    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
        total_characters += 1

    for char, occurrences in frequencies.items():
        frequencies[char] = (occurrences / total_characters) * 100

    return frequencies


def calculate_pair_frequency(text):
    text = text.replace('\n', '')
    pair_frequencies = {}
    total_pairs = 0

    for i in range(len(text) - 1):
        pair = text[i:i + 2]
        if pair in pair_frequencies:
            pair_frequencies[pair] += 1
        else:
            pair_frequencies[pair] = 1
        total_pairs += 1

    for pair, occurrences in pair_frequencies.items():
        pair_frequencies[pair] = (occurrences / total_pairs) * 100

    return pair_frequencies


def analyze_file(file_path):
    codecs = ['utf-8', 'iso-8859-1']
    for codec in codecs:
        try:
            with open(file_path, 'r', encoding=codec) as file:
                text = file.read()
                symbol_frequency = calculate_symbol_frequency(text)
                pair_frequency = calculate_pair_frequency(text)
                return symbol_frequency, pair_frequency
        except UnicodeDecodeError:
            continue

def print_top5(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:5]


# Input files
english_file = 'ListaPalavrasEN.txt'
portuguese_file = 'ListaPalavrasPT.txt'


print("ListaPalavrasEN.txt")
symbol_frequency_english, pair_frequency_english = analyze_file(english_file)
print("5 most frequent symbols:")
print(print_top5(symbol_frequency_english))
print("5 most frequent symbol pairs:")
print(print_top5(pair_frequency_english))

print("ListaPalavrasPT.txt")
symbol_frequency_portuguese, pair_frequency_portuguese = analyze_file(portuguese_file)
print("5 most frequent symbols:")
print(print_top5(symbol_frequency_portuguese))
print("5 most frequent symbol pairs:")
print(print_top5(pair_frequency_portuguese))

