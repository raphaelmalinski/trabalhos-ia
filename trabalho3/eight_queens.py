import random

# Auxiliary functions =====
def generateRandomIndividuals(n):
    """
    Gera invididuas randomicos
    :param n:list - numero de individuos gerados
    :return:list - individuas gerados
    """
    individuals = []
    for nI in range(n):
      individuals.append([random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8)])
    return individuals

def tournament2(p, k):
    """
    Executa uma seleção na população p entre k participantes
    :param p:list - população
    :param k:int - numero de participantes
    :return:list - 2 vencedores
    """
    winners=[]
    for i in range(2):
      competitors =[]
      for c in range(k):
        competitors.append(random.choice(p))
      winners.append(tournament(competitors))
    return winners

# =========================
def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    collisions = 0
    for col, row in enumerate(individual):
      for itCol in range(col+1, len(individual)): #We only check for collisions upwards, so we prevent from counting the same collision 2 times
        itRow = individual[itCol]
        if row == itRow or abs(col-itCol) == abs(row-itRow):
          collisions += 1
    return collisions

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    best = (99, None) #(conflicts, participant)
    for participant in participants:
      participantConflicts = evaluate(participant)
      if participantConflicts < best[0]:
        best = (participantConflicts, participant)
    
    return best[1]

def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    children1 = parent1[0:index] + parent2[index:]
    children2 = parent2[0:index] + parent1[index:]
    return children1, children2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random.random() < m:
      randomIndex = random.randint(0, len(individual) - 1)
      individual[randomIndex] = random.randint(1, 8)

    return individual



def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    p = generateRandomIndividuals(n)
    for generation in range(g):
      g_p = []
      if e:
        g_p.append(tournament(p))
      while len(p) < n:
        winners = tournament2(p, k)
        winnersC = crossover(winners[0], winners[1], random.randint(0,7))
        winnersM = []
        winnersM.append(mutate(winnersC[0], m))
        winnersM.append(mutate(winnersC[1], m))
        g_p.append(winnersM)
      p.append(g_p)
    return tournament(p)
