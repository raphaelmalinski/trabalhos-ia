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
        raise NotImplementedError


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    PUZZLE_SIZE=3
    ACTIONS = ["acima", "esquerda", "abaixo", "direita"]
    EMPTY_MARK = '_'
    
    def isRightEdge(emptyPosition):
      return emptyPosition%PUZZLE_SIZE == PUZZLE_SIZE - 2

    def isLeftEdge(emptyPosition):
      return emptyPosition%PUZZLE_SIZE == 0

    def isBottomRow(emptyPosition):
      return emptyPosition > (PUZZLE_SIZE*PUZZLE_SIZE) - (PUZZLE_SIZE)

    def isTopRow(emptyPosition):
      return emptyPosition < PUZZLE_SIZE - 1
    
    emptyPosition = estado.find(EMPTY_MARK)
    actionsList = []

    if(not isTopRow(emptyPosition=emptyPosition)):
      #TEM AÇÃO ACIMA
      newState = estado
      newState[emptyPosition] = newState[emptyPosition - 3]
      newState[emptyPosition - 3] = newState[emptyPosition]
      actionsList.append((ACTIONS[1], newState))

    if(not isBottomRow(emptyPosition=emptyPosition)):
      #TEM AÇÃO ABAIXO
      newState = estado
      newState[emptyPosition] = newState[emptyPosition + 3]
      newState[emptyPosition + 3] = newState[emptyPosition]
      actionsList.append((ACTIONS[3], newState))

    if(not isRightEdge(emptyPosition=emptyPosition)):
      #TEM AÇÃO DIREITA
      newState = estado
      newState[emptyPosition] = newState[emptyPosition + 1]
      newState[emptyPosition + 1] = newState[emptyPosition]
      actionsList.append((ACTIONS[4]), newState)


    if(not isLeftEdge(emptyPosition=emptyPosition)):
      #TEM AÇÃO ESQUERDA
      newState = estado
      newState[emptyPosition] = newState[emptyPosition - 1]
      newState[emptyPosition -1] = newState[emptyPosition]
      actionsList.append((ACTIONS[2]), newState)
  
    return actionsList


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
