import numpy as np


def calcula_hipotese(theta_0, theta_1, dados_x):
    return list(map(lambda x: theta_0 + theta_1 * x, dados_x))


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    dados_x, dados_y = data[:,0], data[:,1]
    dados_x_hipotese = calcula_hipotese(theta_0, theta_1, dados_x)

    return np.square(np.subtract(dados_x_hipotese, dados_y)).mean()


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    dados_x, dados_y = data[:,0], data[:,1]
    dados_x_hipotese = calcula_hipotese(theta_0, theta_1, dados_x)

    derivada_theta_0 = 2 * np.subtract(dados_x_hipotese, dados_y).mean()
    derivada_theta_1 = 2 * np.multiply(np.subtract(dados_x_hipotese, dados_y), dados_x).mean()

    novo_theta_0 = theta_0 - alpha * derivada_theta_0
    novo_theta_1 = theta_1 - alpha * derivada_theta_1

    return novo_theta_0, novo_theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    lista_thetas_0, lista_thetas_1 = [], []
    novo_theta_0, novo_theta_1 = theta_0, theta_1
    for _ in range(num_iterations):
        novo_theta_0, novo_theta_1 = step_gradient(novo_theta_0, novo_theta_1, data, alpha)
        lista_thetas_0.append(novo_theta_0)
        lista_thetas_1.append(novo_theta_1)

    return lista_thetas_0, lista_thetas_1
