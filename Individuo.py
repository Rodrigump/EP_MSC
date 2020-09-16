import random

class Individuo:

    def __init__ (self, id, n): #construtor
        self.id = id #id do individuo na populacao
        self.genoma  = [] #conjunto de cromossomos
        self.fitness = -1 #fitness (o quao bom ele eh) do individuo
        self.n = n #numero de cromossomos no genoma

    def calcFitness (self): #funcao que calcula o fitness do individuo
        ret = 0
        for i in range(self.n):
            ret = ret + self.genoma[i]

        self.fitness = ret
        return ret 

    def setRandomGenoma (self): #funcao que gera o genoma aleatoriamente (apenas para 1a populacao)
        aux = []
        for i in range(self.n):
            aux.append(random.randint(0,9))

        self.genoma = aux

    def setParentsGenoma (self, g): #funcao que atribui o genoma resultante do cruzamento dos pais
        self.genoma = g