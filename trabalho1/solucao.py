from queue import Queue, LifoQueue, PriorityQueue
import time

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado : str = estado
        self.pai : Nodo = pai
        self.acao : str = acao
        self.custo : int = custo
    
    def __lt__(self, other):
        return (self.custo < other.custo)

    def __gt__(self, other):
        return (self.custo > other.custo)

    def isSolved(self):
      OBJETIVO = "12345678_"
      return self.estado == OBJETIVO

    def getPath(self):
      path = list()
      node = self
      while not node.pai == None:
        path.append(node.acao)
        node = node.pai
      path.reverse()
      return path

    def isSolvable(self):
      #Check the number of inversions
      #Reference: https://tutorialspoint.dev/algorithm/algorithms/check-instance-8-puzzle-solvable
      EMPTY_MARK = "_"
      inversions = 0
      stateList = list(self.estado)
      emptyPosition = self.estado.find(EMPTY_MARK)
      stateList.pop(emptyPosition)

      for index, element in enumerate(stateList):
        for subsequent in stateList[index+1:]:
          if subsequent < element:
            inversions+=1

      return (inversions%2==0)


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    def isRightEdge(emptyPosition):
      return emptyPosition%PUZZLE_SIZE == PUZZLE_SIZE - 1

    def isLeftEdge(emptyPosition):
      return emptyPosition%PUZZLE_SIZE == 0

    def isBottomRow(emptyPosition):
      return emptyPosition >= (PUZZLE_SIZE*PUZZLE_SIZE) - (PUZZLE_SIZE)

    def isTopRow(emptyPosition):
      return emptyPosition <= PUZZLE_SIZE - 1
    
    def swap(estado, pos1, pos2):
      newState = list(estado)
      temp = newState[pos1]
      newState[pos1] = newState[pos2]
      newState[pos2] = temp
      return "".join(newState)
    
    PUZZLE_SIZE = 3
    ACTIONS = ["acima", "esquerda", "abaixo", "direita"]
    EMPTY_MARK = '_'

    emptyPosition = estado.find(EMPTY_MARK)
    actionsList = []

    if(not isTopRow(emptyPosition)):
      #TEM AÇÃO ACIMA
      actionsList.append((ACTIONS[0], swap(estado, emptyPosition, emptyPosition-PUZZLE_SIZE)))

    if(not isBottomRow(emptyPosition)):
      #TEM AÇÃO ABAIXO
      actionsList.append((ACTIONS[2], swap(estado, emptyPosition, emptyPosition+PUZZLE_SIZE)))

    if(not isRightEdge(emptyPosition)):
      #TEM AÇÃO DIREITA
      actionsList.append((ACTIONS[3], swap(estado, emptyPosition, emptyPosition+1)))

    if(not isLeftEdge(emptyPosition)):
      #TEM AÇÃO ESQUERDA
      actionsList.append((ACTIONS[1], swap(estado, emptyPosition, emptyPosition-1)))
  
    return actionsList


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    sucessores = sucessor(nodo.estado)
    nodos = []

    for suc in sucessores:
      nodos.append(Nodo(suc[1], nodo, suc[0], nodo.custo + 1))

    return nodos

def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    tempo_inicial = time.time() # em segundos
    nodo_raiz = Nodo(estado, None, "", 0)
    if not nodo_raiz.isSolvable(): return None
    visitados = {}
    fronteira = Queue()
    fronteira.put(nodo_raiz)
    qtd_nos_expandidos = 0

    while not fronteira.empty():
      v = fronteira.get()
      if v.isSolved():
        tempo_final = time.time() # em segundos
        print(f"BFS: {tempo_final - tempo_inicial} segundos")
        print(f"Custo: {v.custo}")
        print(f"Nós expandidos: {qtd_nos_expandidos}")
        return v.getPath()

      if v.estado not in visitados:
        visitados[v.estado] = True
        sucessores = expande(v)
        qtd_nos_expandidos += 1
        for sucessor in sucessores:
          fronteira.put(sucessor)

    return None     #return None if it has no solution

def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    tempo_inicial = time.time() # em segundos
    nodo_raiz = Nodo(estado, None, "", 0)
    if not nodo_raiz.isSolvable(): return None
    visitados = {}
    fronteira = LifoQueue()
    fronteira.put(nodo_raiz)
    qtd_nos_expandidos = 0

    while not fronteira.empty():
      v = fronteira.get()
      if v.isSolved():
        tempo_final = time.time() # em segundos
        print(f"DFS: {tempo_final - tempo_inicial} segundos")
        print(f"Custo: {v.custo}")
        print(f"Nós expandidos: {qtd_nos_expandidos}")
        return v.getPath()

      if v.estado not in visitados:
        visitados[v.estado] = True
        sucessores = expande(v)
        qtd_nos_expandidos += 1
        for sucessor in sucessores:
          fronteira.put(sucessor)

    return None     #return None if it has no solution

def h_hamming(estado):
    """
    Recebe um estado e retorna a distancia de hamming
    """
    OBJETIVO = "12345678_"
    h = sum( OBJETIVO[i] != estado[i] for i in range(len(estado)))
    
    return h

def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    tempo_inicial = time.time() # em segundos
    nodo_raiz = Nodo(estado, None, "", 0)
    if not nodo_raiz.isSolvable(): return None
    visitados = {}
    fronteira = PriorityQueue()
    fronteira.put((0,nodo_raiz))
    qtd_nos_expandidos = 0

    while not fronteira.empty():
      v = fronteira.get()[1]
      if v.isSolved():
        tempo_final = time.time() # em segundos
        print(f"A* Hamming: {tempo_final - tempo_inicial} segundos")
        print(f"Custo: {v.custo}")
        print(f"Nós expandidos: {qtd_nos_expandidos}")
        return v.getPath()

      if v.estado not in visitados:
        visitados[v.estado] = True
        sucessores = expande(v)
        qtd_nos_expandidos += 1
        for nodo in sucessores:
          fronteira.put((nodo.custo + h_hamming(nodo.estado), nodo))

    return None     #return None if it has no solution

def get_manhattan_distance(p, q):
    """ 
    Retorna a distância Manhattan entre os pontos p e q
    """
    distance = 0
    for p_i, q_i in zip(p, q):
        distance += abs(p_i - q_i)
    
    return distance

def h_manhattan(estado):
    """
    Recebe um estado e retorna a distancia de Manhattan
    """
    COORD = {'1': (0, 2), '2': (1, 2), '3': (2, 2), '4': (0, 1), '5': (1, 1), '6': (2, 1), '7': (0, 0), '8': (1, 0), '9': (2,0)}
    h = 0
    for i in range(len(estado)):
        if estado[i] != '_':
            h += get_manhattan_distance(COORD[estado[i]], COORD[str(i + 1)])
    
    return h

def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    tempo_inicial = time.time() # em segundos
    nodo_raiz = Nodo(estado, None, "", 0)
    if not nodo_raiz.isSolvable(): return None
    visitados = {}
    fronteira = PriorityQueue()
    fronteira.put((0,nodo_raiz))
    qtd_nos_expandidos = 0

    while not fronteira.empty():
      v = fronteira.get()[1]
      if v.isSolved():
        tempo_final = time.time() # em segundos
        print(f"A* Manhattan: {tempo_final - tempo_inicial} segundos")
        print(f"Custo: {v.custo}")
        print(f"Nós expandidos: {qtd_nos_expandidos}")
        return v.getPath()

      if v.estado not in visitados:
        visitados[v.estado] = True
        sucessores = expande(v)
        qtd_nos_expandidos += 1
        for nodo in sucessores:
          fronteira.put((nodo.custo + h_manhattan(nodo.estado), nodo))

    return None     #return None if it has no solution
