import unittest
import solucao as solucao


class TestaSolucao(unittest.TestCase):
    def test_sucessor(self):
        """
        Testa a funcao sucessor para o estado "2_3541687"
        :return:

        """
        # a lista de sucessores esperados é igual ao conjunto abaixo (ordem nao importa)
        
        INPUTS = ["_23541687", "2_3541687", "23_541687", "235_41687", "2354_1687", "23541_687", "235416_87", "2354168_7", "23541687_"]
        
        OUTPUTS = [
            {("direita", "2_3541687"), ("abaixo", "523_41687")},#_23541687
            {("abaixo", "2435_1687"), ("esquerda", "_23541687"), ("direita", "23_541687")},#2_3541687
            {("abaixo", "23154_687"), ("esquerda", "2_3541687")},#23_541687
            {("abaixo", "235641_87"), ("direita", "2354_1687"), ("acima", "_35241687")},#235_41687
            {("abaixo", "2354816_7"), ("esquerda", "235_41687"), ("direita", "23541_687"), ("acima", "2_5431687")},#2354_1687
            {("abaixo", "23541768_"), ("esquerda", "2354_1687"), ("acima", "23_415687")},#23541_687
            {("direita", "2354168_7"), ("acima", "235_16487")},#235416_87
            {("esquerda", "235416_87"), ("direita", "23541687_"), ("acima", "2354_6817")},#2354168_7
            {("esquerda", "2354168_7"), ("acima", "23541_876")}#23541687_
            ]

        for i in range(len(INPUTS)):
          sucessores = solucao.sucessor(INPUTS[i])  # obtem os sucessores chamando a funcao implementada
          self.assertEqual(len(OUTPUTS[i]), len(sucessores))     # verifica se foram retornados 3 sucessores
          for s in sucessores:                     # verifica se os sucessores retornados estao entre os esperados
              self.assertIn(s, OUTPUTS[i])

    def test_expande(self):
        """
        Testa a função expande para um Node com estado "185432_67" e custo 2
        :return:
        """
        pai = solucao.Nodo("185432_67", None, "abaixo", 2)  # o pai do pai esta incorreto, mas nao interfere no teste
        # a resposta esperada deve conter nodos com os seguintes atributos (ordem dos nodos nao importa)
        resposta_esperada = {
            ("185_32467", pai, "acima", 3),
            ("1854326_7", pai, "direita", 3),
        }

        resposta = solucao.expande(pai)  # obtem a resposta chamando a funcao implementada
        self.assertEqual(2, len(resposta))  # verifica se foram retornados 2 nodos
        for nodo in resposta:
            # verifica se a tupla com os atributos do nodo esta' presente no conjunto com os nodos esperados
            self.assertIn((nodo.estado, nodo.pai, nodo.acao, nodo.custo), resposta_esperada)

    def test_bfs(self):
        """
        Testa o BFS em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.bfs("2_3541687")))
        print("Atencao! O BFS passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.bfs("185423_67"))

    def test_astar_hamming(self):
        """
        Testa o A* com dist. Hamming em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.astar_hamming("2_3541687")))
        print("Atencao! O A* Hamming passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.astar_hamming("185423_67"))

    def test_astar_manhattan(self):
        """
        Testa o A* com dist. Manhattan em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.astar_manhattan("2_3541687")))
        print("Atencao! O A* Manhattan passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.astar_manhattan("185423_67"))

    def test_dfs(self):
        """
        Testa o DFS apenas em um estado sem solucao pq ele nao e' obrigado
        a retornar o caminho minimo
        :param estado: str
        :return:
        """
        # nao ha solucao a partir do estado 185423_67
        self.assertEqual(None, solucao.dfs("185423_67"))
    
    def test_action_order(self):
        """
        Testa se BFS e A* retornam a sequencia de acoes na ordem correta
        """
        estado = "1235_6478"
        solucao_otima = ['esquerda', 'abaixo', 'direita', 'direita']
        self.assertEqual(solucao_otima, solucao.bfs(estado))
        self.assertEqual(solucao_otima, solucao.astar_hamming(estado))
        self.assertEqual(solucao_otima, solucao.astar_manhattan(estado))

if __name__ == '__main__':
    unittest.main()
