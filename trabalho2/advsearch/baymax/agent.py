import random
import sys

import advsearch.othello.board as board

class Node:
  def __init__(self, parent, state, move, color):
    self.parent: Node = parent
    self.state: str = state
    self.move: tuple = move
    self.color: str = color
    self.score: int = None
    if parent == None:
      self.depth: int = 0
    else:
      self.depth: int = parent.depth + 1
  
  def isRoot(self):
    return self.parent == None
  
  def hasMoves(self):
    actualBoard = board.from_string(self.state)
    return actualBoard.has_legal_move(self.color)
  
  def calculateScore(self):
    actualBoard = board.from_string(self.state)
    self.score = sum([1 for char in str(actualBoard) if char == self.color])
  
  def expand(self):
    sons = []
    actualBoard = board.from_string(self.state)
    legalMoves = actualBoard.legal_moves(self.color)
    if not legalMoves:
      return sons

    sonColor = actualBoard.opponent(self.color)
    for legalMove in legalMoves:
      generatedState = getBoardStateWithMove(actualBoard, legalMove, self.color)
      sons.append(Node(self, generatedState, legalMove, sonColor))
    
    return sons

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta

    noMove = (-1, -1) #We suppose the root node is a no move node
    rootNode = Node(None, the_board.__str__(), noMove, color)
    bestPlay = minmax_decision_ab(rootNode, 6)
    return bestPlay.move

def minmax_decision_ab(rootNode: Node, depth: int):
  INFINITY = 65 #max number of pieces for one color is 64(full 8x8 board)
  maxNode = max_node(rootNode, -INFINITY, +INFINITY, depth)
  return maxNode

def max_node(node: Node, alpha: int, beta: int, depth: int):
  INFINITY = 65
  
  if not node.hasMoves() or node.depth == depth:
    node.calculateScore()
    return node

  sucessors = node.expand()
  bestNode = sucessors[0]
  bestNode.score = -INFINITY
  # i=len(sucessors)
  for sucessor in sucessors:
    # i-=1
    minSucessor = min_node(sucessor, alpha, beta, depth)
    maxScore = max(bestNode.score, minSucessor.score)
    if minSucessor.score == maxScore:
      bestNode = sucessor
      bestNode.score = maxScore 
    alpha = max(alpha, bestNode.score)
    if alpha >= beta:
      # print(f"Podando {i} sucessores")
      break
  return bestNode

def min_node(node: Node, alpha: int, beta: int, depth: int):
  INFINITY = 65

  if not node.hasMoves() or node.depth == depth:
    node.calculateScore()
    return node

  sucessors = node.expand()
  worstNode = sucessors[0]
  worstNode.score = INFINITY
  # i = len(sucessors)
  for sucessor in sucessors:
    # i-=1
    maxSucessor = max_node(sucessor, alpha, beta, depth)
    minScore = min(worstNode.score, maxSucessor.score)
    if maxSucessor.score == minScore:
      worstNode = sucessor
      worstNode.score = minScore
    beta = min(beta, worstNode.score)
    if beta <= alpha:
      # print(f"Podando {i} sucessores")
      break
  return worstNode

def getTileColumnFromMove(move: tuple):
  return move[0]

def getTileRowFromMove(move: tuple):
  return move[1]

def getBoardStateWithMove(board: board.Board, move: tuple, color: str):
  EMPTY = '.'
  board.tiles[getTileRowFromMove(move)][getTileColumnFromMove(move)] = color
  boardState = board.__str__()
  board.tiles[getTileRowFromMove(move)][getTileColumnFromMove(move)] = EMPTY
  return boardState

def printNodes(nodeList):
  for node in nodeList:
    print(f"Parent: {node.parent}")
    print(f"Move: {node.move}")
    print(f"Score: {node.score}")
    print(f"Color: {node.color}")
    print(f"Depth: {node.depth}")
    print(f"==State==\n{node.state}")