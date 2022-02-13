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

    for i in range(len(sucessores)):
      nodos.append(Nodo(sucessores[i][1], nodo, sucessores[i][0], nodo.custo + 1))

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
    def pathFromRootNode(actualNode, solutionSteps=[]):
      if(actualNode.pai == None):
        return solutionSteps.append((actualNode.acao, actualNode.estado))

      pathFromRootNode(actualNode.pai, solutionSteps)
      solutionSteps.append((actualNode.acao, actualNode.estado))
      return solutionSteps
      


    OBJETIVO = "12345678_"
    nodo_raiz = Nodo(estado, None, "", 0)
    visitados = []
    fronteira = [nodo_raiz]

    while len(fronteira) > 0:
      v = fronteira.pop(0)
      if v.estado == OBJETIVO:
        return pathFromRootNode(v)

      if v.estado not in visitados:
        visitados.append(v.estado)
        sucessores = expande(v)
        fronteira.extend(sucessores)
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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def h_haming(estado):
    """
    Recebe um estado e retorna a distancia de hamming
    """
	OBJETIVO = "12345678_"
	h = sum( OBJETIVO[i] != estado[i] for i in range(len(estado)) )\
	
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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
