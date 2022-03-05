import random
import sys

from queue import LifoQueue
import advsearch.othello.board as board

class Node:
  def __init__(self, parent, state, move, color):
    self.parent: Node = parent
    self.state: str = state
    self.move: tuple = move
    self.color: str = color
  
  def expand(self):
    actualBoard = board.from_string(self.state)
    legalMoves = actualBoard.legal_moves(self.color)
    if not legalMoves:
      return [Node(None, None, (-1, -1), None)]
    
    sons = []
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

    root = Node(None, the_board.__str__(), (), color)
    sonsList = root.expand()
    printNodes(sonsList)
    return random.choice(sonsList).move


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
    print(f"Color: {node.color}")
    print(f"==State==\n{node.state}")