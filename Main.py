from Populacao import Populacao

pop = Populacao(10, 10) #10 individuos com 10 cromossomos cada

pop.getInfoPopulacao()

h = pop.getBestIndividuo() #id do melhor individuo

a = pop.getMediaPopulacao() #fitness medio

l = pop.getWorstIndividuo() #id do pior individuo

print('Melhor fitness:', float(pop.p[h].fitness))
print('Media fitness:', a)
print('Pior fitness:', float(pop.p[l].fitness))