
def hebb_split(entradas):
    split_1 = entradas.split("\n")
    split_2 = []
    for i in range(len(split_1)):
        floats = [float(x) for x in split_1[i].split()]
        target = floats[-1]
        floats.pop()
        tupleAux = (floats, target)
        split_2.append(tupleAux)
    return split_2

def perceptron_split(entradas):
    split_1 = entradas.split("\n")
    split_2 = []
    alpha_theta = []
    for i in range(len(split_1)):
        floats = [float(x) for x in split_1[i].split()]
        if(i < len(split_1) - 2):
            target = floats[-1]
            floats.pop()
            tupleAux = (floats, target)
            split_2.append(tupleAux)
        else:
            alpha_theta.append(floats[0])
    return split_2, alpha_theta[0], alpha_theta[1]

if __name__ == "__main__":
    #([([1, 1, 1], 1), ([1, -1, 1], -1), ([-1, 1, 1], -1), ([-1, -1, 1], -1)])
    entrada = "1 1 1 1\n1 -1 1 -1\n-1 1 1 -1\n-1 -1 1 -1"
    print (entrada)

    funciona = hebb_split(entrada)
    print(funciona)

    # ([([1, 1, 1], 1), ([1, -1, 1], -1), [-1, 1, 1], -1), ([-1, -1, 1], -1)], 1, 0)
    entrada = "1 1 1 1\n1 -1 1 -1\n-1 1 1 -1\n-1 -1 1 -1\n1\n0"

    funciona = perceptron_split(entrada)
    print(funciona)


