import random
# import numpy.random as npr
from math import sin, sqrt
from statistics import mean

NUM_OF_BITS = 10


class Ga:
    def __init__(self, pop_size, crossover_rate, mutation_rate, generations, elitism):
        self.pop_size = pop_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.elitism = elitism
        self.all_x = []
        self.fitness = [0 for i in range(self.pop_size)]
        self.population_double = []
        self.dict_pop_fit = {}
        self.papa = []
        self.mama = []
        self.best_individual = 1
        # number of bits = 10
        # 2^10 = 1024 possibilities in the x axis
        # 512 - upper bound
        self.granularity = pow(2, NUM_OF_BITS)
        self.step = 512.0 / self.granularity

        # Getting all x
        self.get_all_x()

    def calc_function(self, x):
        return abs(x * sin(sqrt(abs(x)))) * (-1)

    def get_all_x(self):
        self.all_x.extend(range(0, self.granularity))

    def get_bin(self, decimal):
        return bin(decimal)[2:].zfill(10)

    def get_decimal(self, binary):
        return int(binary, 2)*self.step

    def get_str_bin(self, n):
        return format(n, 'b').zfill(10)

    def get_int(self, n):
        # float to int
        return int(n/self.step)

    def get_initial_population(self):
        self.population_double = random.sample(self.all_x, self.pop_size)
        for i in range(self.pop_size):
            self.population_double[i] = self.get_decimal(self.get_bin(self.population_double[i]))

    def evaluate(self):
        for i in range(self.pop_size):
            self.fitness[i] = self.calc_function(self.population_double[i])
            # capturando o index do menor fitness da lista e retornando o individuo correspondente
            self.best_individual = self.population_double[self.fitness.index(min(self.fitness))]

    def final_wheel(self):
        # lista de fitness convertida para absolute
        abs_fitness = [abs(n) for n in self.fitness]
        # somatorio dos fitness
        sum_fitness = float(sum(abs_fitness))
        # lista de pesos, fitness / total
        weigth_fitness = [w / sum_fitness for w in abs_fitness]
        # vetor aleatorio de individuos probabilisticamente selecionados
        # random.choises (populacao, "vetor pesos", tamanho)
        self.papa = random.choices(self.population_double, weights = weigth_fitness, k = self.pop_size//2)
        self.mama = random.choices(self.population_double, weights = weigth_fitness, k = self.pop_size//2)

    def cross(self):
        n = 0
        for i in range (len(self.papa)):
            # para cada item da lista, verifica se um cruzamento deve ocorrer
            if random.random() <= self.crossover_rate:
                half_1 = self.get_bin(self.get_int(self.papa[i]))
                half_2 = self.get_bin(self.get_int(self.mama[i]))
                sons = self.simple_cross(half_1, half_2)
                self.population_double[n] = sons[0]
                self.population_double[n+1] = sons[1]
                n += 2


    def simple_cross(self, papa, mama):
        # cuts: quantidade de cortes
        # trades: quantidade de trocas
        cuts = 1
        trades = 1

        # parts: vetor de numeros aleatorios
        # que indicam onde os cortes serao feitos
        parts = random.sample(range(1, len(papa)), cuts)
        parts.sort()

        # choose: vetor de numeros aleatorios
        # que indicam os indices que serao trocados
        choose = random.sample(range(0, len(parts) + 1), trades)

        # iteracao que cria um filho
        papa_half = []
        for i in range(len(parts) + 1):
            papa_half.append(0)
            if i == 0:
                papa_half[i] = papa[:parts[0]]
            elif i == len(parts):
                papa_half[i] = papa[parts[i - 1]:]
            else:
                papa_half[i] = papa[parts[i - 1]:parts[i]]

        mama_half = []
        for i in range(len(parts) + 1):
            mama_half.append(0)
            if i == 0:
                mama_half[i] = mama[:parts[0]]
            elif i == len(parts):
                mama_half[i] = mama[parts[i - 1]:]
            else:
                mama_half[i] = mama[parts[i - 1]:parts[i]]

        papa_copy = papa_half.copy()

        for i in range(len(choose)):
            papa_half[choose[i]] = mama_half[choose[i]]
            mama_half[choose[i]] = papa_copy[choose[i]]

        # retorna um float
        return self.get_decimal("".join(papa_half)), self.get_decimal("".join(mama_half))



    def mutate(self):
        for i in range (self.pop_size):
            # para cada item da lista, verifica se uma mutacao deve ocorrer
            if random.random() <= self.mutation_rate:
                # converter o item float de indice i para inteiro
                # depois para binario, e depois para uma lista
                # -> Strings em python sao inalteraveis
                xmen = list(self.get_bin(int(self.get_int(self.population_double[i]))))
                # inteiro aleatorio de 0 < NUM_OF_BITS
                index = random.randrange(NUM_OF_BITS)
                # invertendo o bit, operacao ^= (ou exclusivo) nao funcionou ;<
                xmen[index] = str(1 - int(xmen[index]))
                # setando o binario mutante para float
                self.population_double[i] = self.get_decimal("".join(xmen))

    def run_generation(self):
        self.get_initial_population()

        # Lists used for graph visualization
        series_generations = []
        series_avg_fitness = []
        series_best_fitness = []

        for i in range(self.generations):
            self.evaluate()

            series_generations.append(i + 1)
            series_avg_fitness.append(mean(self.fitness))
            series_best_fitness.append(self.fitness[self.population_double.index(self.best_individual)])

            self.final_wheel()
            self.cross()
            self.mutate()

            if self.elitism:
                index = random.randrange(self.pop_size)
                self.population_double[index] = self.best_individual

        self.evaluate()

        return self.best_individual, series_generations, series_avg_fitness, series_best_fitness