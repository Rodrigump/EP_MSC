from Individuo import Individuo

class Populacao:

    def __init__ (self, hab, n): #construtor
        self.hab = hab #numero de habitantes da populacao
        self.n = n #numero de cromossomos de cada individuo
        self.p = [] #lista de habitantes

        for i in range(hab): #gera os individuos aleatoriamente e os insere na populacao
            novo = Individuo(i, n)
            novo.setRandomGenoma()
            novo.calcFitness()
            self.p.append(novo)

    def getInfoIndividuo (self, id):
        print('Individuo ', self.p[id].id)
        print('Genoma ', self.p[id].genoma)
        print('Fitness ', self.p[id].fitness)
        print('\n')

    def getInfoPopulacao(self): #imprime id, genoma e fitness dos individuos da populacao
        for i in range(self.hab):
            self.getInfoIndividuo(i)

    def getBestIndividuo (self): #retorna o id do melhor individuo
        aux = self.n * 10
        ret = 0
        for i in range(self.hab):
            if(self.p[i].fitness <= aux):
                aux = self.p[i].fitness
                ret = i
        return ret

    def getWorstIndividuo (self): #retorna o id do pior individuo
        aux = -1
        ret = 0
        for i in range(self.hab):
            if(self.p[i].fitness >= aux):
                aux = self.p[i].fitness
                ret = i
        return ret

    def getMediaPopulacao (self): #retorna a media dos fitnesses da populacao
        soma = 0
        for i in range(self.hab):
            soma = soma + self.p[i].fitness 
        
        return (soma/self.hab)

    #metodos de cruzamento em breve