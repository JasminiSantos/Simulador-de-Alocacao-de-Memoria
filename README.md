# Simulador de Alocação de Memória

1. Alocação da matriz de memória para simulação: O usuário deverá informar o número de
linhas e colunas para a alocação inicial da memória. Deve-se garantir que o número de linhas
e colunas sejam maiores que zero.
2. Visualização de memória: O sistema deverá apresentar, de forma gráfica, a ocupação da
memória. Um exemplo de ocupação de uma matriz de memória de tamanho 5x20 é
apresentado abaixo, onde as regiões apresentadas como um ‘X’ estão ocupadas.
3. Alocação first fit: Esta estratégia de alocação encontra o primeiro espaço em memória cujo
tamanho seja igual ou maior que o desejado e então realiza a alocação. No exemplo acima,
caso uma alocação de tamanho 3 seja requisitada, ela seria realizada nas posições (0, 17),
(0,18) e (0,19).
4. Alocação best fit: Esta estratégia busca um espaço disponível que seja o mais adequado
para o tamanho requisitado. Isto é, caso uma alocação de tamanho ‘n’ seja requisitada, um
espaço de tamanho ‘n’ será buscado. Caso ele exista, a alocação será realizada. Caso
contrário, um espaço de tamanho (n+1) será buscado e assim por diante, até que um espaço
seja encontrado ou que seja determinado que nenhum espaço esteja disponível. No exemplo
acima, caso uma alocação de tamanho 3 seja requisitada, ela deverá ocorrer nas posições (2,
6), (2,7) e (2,8).
5. Alocação worst fit: O algoritmo de alocação worst fit realiza a alocação de memória na
região com maior espaço livre contanto que ela seja suficientemente grande para comportar
o tamanho requisitado. No exemplo acima, caso uma alocação de tamanho 2 seja requisitada,
ela ocorrerá nas posições (0,17), (0,18), (0,19) e (1,0).
6. Desalocação: O usuário deverá informar as coordenadas de início e fim para realizar a
desalocação de memória. Deve-se garantir que todas as coordenadas informadas sejam
válidas antes de realizar a desalocação.
