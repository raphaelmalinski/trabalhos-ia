# Integrantes:
- Arthur Bockmann Grossi - 00275607
- João Atz Dick - 00185410
- Raphael Malinski Vieira - 00279794

## Relatório
A estratégia de parada utilizada foi a de profundidade fixa, sendo definida a produndidade 5. A utilidade padrão é o número
de peças da cor do nosso agente no tabuleiro, então o oponente tenta minimizar o nosso número de peças e o nosso agente 
tenta maximizá-las. Para a função de avaliação foi utilizada a multiplicação por 2 da utilidade padrão das quinas do tabuleiro,
fazendo com que a IA dê prioridade para a conquista das quinas, locais estratégicos onde as peças estando lá não podem ser mais 
conquistadas. 
