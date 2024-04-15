# 1 -

# a(n) = a + (n-1)d
def progessaoaritmetica(N, u, r):
    ret = [u]
    max = 2

    while max < N:
        list.append(u + (max - 1) * r)
        max += 1


# 2 -
def fatorial(a):
    x = 1
    while a > 1:
        x = x * a
        a -= a
    return x


# 3-mmc

def mmc(a, b):
    if a == b:
        return a

    x = a
    y = b

    while True:
        if x == y:
            break

        if x < y:
            x += a
        if x > y:
            y += b

    return x


# 4 primos entre left e right

def primos(left, right):
    ret = []
    for i in range(right-left):
        if isprimo(i + left):
            ret.append(i + left)
    return ret


def isprimo(a):
    z = 1
    while z < a - 1:
        if (a % (a-z)) == 0:
            return False
        z += 1

    return True


def simbolosfreq(filepath, freq):
    ret = []
    content = open(filepath, "r").read() #content = ficheiro
    length = len(content)

    for i in content:

        if i in ret:
            continue
        presences = count(content, i)
        if (presences/length)*100 >= freq:
            ret.append(i)

    return ret

    return content

def count(string , char):
    cnt = 0
    for i in string:
        if i == char:
            cnt += 1
    return cnt

#print(simbolosfreq("bruh.txt", 10))
