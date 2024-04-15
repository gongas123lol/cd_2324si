import random
import string
import math
import os

# Implemente uma fonte de símbolos genérica, a qual gera ficheiros com N símbolos, de acordo com a Função Massa
# de Probabilidade (FMP) do alfabeto de M símbolos: p(x) = {p(x1), p(x2), . . . , p(xM)}. A implementação deverá
# apresentar os valores de entropia: da fonte; da sequência gerada. Comente os resultados obtidos.

alfabet = [(50, 'a'), (50, 'b')]
alphabet_pairs = [(1 / 26, char) for char in 'abcdefghijklmnopqrstuvwxyz']


def FMP(alfabeto, length, delimyesno):
    entropiaalfabeto = 0
    for x in alfabeto:
        p_x = x[0] / 100
        entropiaalfabeto -= p_x * math.log2(p_x)

    print("Entropia do alfabeto:", entropiaalfabeto / math.log2(100))
    # slots de 100.000 -> logo a probabilidade, em unidades, será multiplicada por 1000
    cnt = 0
    arr = []
    for item in alfabeto:
        arr.append((cnt + 1, cnt + item[0] * 1000))
        cnt += item[0] * 1000

    result = ""
    entropycalc = ""
    for i in range(length):
        rn = random.randrange(1, 100000)
        if delimyesno and len(result):
            result += ","
        for item in arr:
            if item[0] < rn <= item[1]:
                result += alfabeto[arr.index(item)][1]
                entropycalc+= alfabeto[arr.index(item)][1]

    print("entropia do resultado:",calculate_entropy(entropycalc))
    return result


# FMP(alphabet_pairs, 10000)

# assumindo que um pin é apenas consistido por numeros
def generate_pin(length):
    pin_prob = [(10, char) for char in '1234567890']
    return FMP(pin_prob, length, 0)


def generate_euromilhoes():
    output = "numeros: "
    euromilhoes_prob = [(2, str(i)) for i in range(1, 51)]
    estrelas_prob = [(10, char) for char in '1234567890']
    output += FMP(euromilhoes_prob, 5, 1)
    output += " estrelas: "
    output += FMP(estrelas_prob, 2, 1)
    return output


def generate_passsword(length):
    usable_chars = string.ascii_letters + string.digits + string.punctuation
    # print(len(usable_chars))
    password_prob = [(100 / 94, char) for char in usable_chars]

    return FMP(password_prob, length, 0)


def calculate_entropy(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    total_chars = len(input_string)

    entropy = 0
    for count in char_count.values():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)

    return entropy

def write_passwords_to_file(filepath, count):
    with open(filepath, "w") as file:
        for i in range(count):
            password = generate_passsword(8)
            file.write(f"{password}\n")


#write_passwords_to_file("passwords.txt", 1000)

print("pin:" + generate_pin(6))
print(generate_euromilhoes())
print("password:" + generate_passsword(8))
