Projeto - Técnico de Futebol
Já pensou em gerenciar seu próprio time de futebol? Com este trabalho você terá a oportunidade de adicionar seus próprios jogadores customizados à equipe, trocar jogadores, definir o esquema tático e montar o time dos sonhos!

Contratar jogador

Para selecionar esta função o usuário deve inserir o número 1 no teclado

Esta função recebe a seguinte estrutura de input:

nome posicao habilidade

Caso algum desses campos não esteja de acordo com as especificações a seguir, o jogador não deve ser adicionado à Equipe!

Cada jogador deve ser identificado por um campo único, que é o seu nome (apenas 1 nome por jogador) e portanto, não é possível adicionar dois jogadores com o mesmo nome. Caso o usuário tente fazer isso, deve ser apresentada a seguinte mensagem:

“Jogador informado já está no time”

A verificação de jogadores repetidos não deve diferenciar nomes pela presença de letras maiúsculas ou minúsculas. Dessa maneira, o nome ronaldo pode ser escrito de diversas maneiras, porém se refere ao mesmo jogador.

Ex.: “Ronaldo” = “ronaldo” = “roNalDO”

Caso o nome do jogador seja maior que 8 caracteres, seu nome deve ser cortado para que contenha apenas 8 caracteres.

Ex.: Alexandre = Alexandr

Caso o nome do jogador não seja válido, deve-se finalizar a operação de contratação do jogador e solicitar uma nova operação.

Há 4 categorias de posição: goleiro, defensor, meia e atacante. Caso o usuário insira alguma posição diferente das citadas, deve-se apresentar a mensagem abaixo, finalizar a operação de contratação de jogador e solicitar uma nova operação :

“A posição informada não existe” 

O campo habilidade refere-se à habilidade do jogador e deve estar dentro do intervalo 10>= habilidade >=0. Caso contrário, deve-se apresentar a mensagem abaixo, finalizar a operação de contratação de jogador e solicitar uma nova operação.

“A habilidade do jogador deve estar entre 0 e 10”

Trocar Jogador

Para selecionar esta função o usuário deve inserir o número 2 no teclado

Esta função recebe a seguinte estrutura de input:

nome posicao habilidade x nome posicao habilidade

Na troca de jogadores, o primeiro jogador será removido do time, enquanto o segundo será adicionado.

Caso o primeiro jogador não  tenha sido contratado com sucesso ou tenha sido contratado com sucesso, porém qualquer uma de suas especificações seja informada de maneira incorreta (inclusive posição escrita de maneira incorreta ou habilidade fora do padrão), deve ser apresentada a seguinte mensagem

“Jogador não está no time”

Caso algum dos campos do segundo jogador (aquele que será adicionado ao time) não esteja de acordo com as especificações apresentadas na função anterior “Adiciona Jogador”, a respectiva mensagem deve ser apresentada e a lista deve permanecer inalterada. Dessa maneira:

Segundo jogador não pode já existir no time:

 “Jogador informado já está no time”

Posição e Habilidade de ambos os jogadores não pode sair da especificação.

“A posição informada não existe” 

“A habilidade do jogador deve estar entre 0 e 10”


Definir Esquema Tático

Para selecionar esta função o usuário deve inserir o número 3 no teclado

Esta função recebe a seguinte estrutura de input:

qtd_defensores qtd_meias qtd_atacantes

Os 3 campos são números que representam a quantidade de jogadores em cada posição. A quantidade de jogadores em cada posição está limitada entre, no mínimo 2 e, no máximo 4, ou seja: 4>= qtd >=2 e a soma desses campos deve totalizar 10. Caso o input do usuário não siga essas regras, a formação não deve ser alterada e devem ser apresentadas as seguintes mensagens, para cada um dos casos:

“Cada posição deve conter entre 2 e 4 jogadores”

“A soma das posições deve totalizar 10 jogadores”


Montar o Time

Para selecionar esta função o usuário deve inserir o número 4 no teclado 

Esta função só pode ser selecionada após a função “Definir Esquema Tático” ter sido acionada com sucesso. Caso contrário, apresenta-se a mensagem:

“O Esquema Tático deve ser estabelecido antes de montar o time”

À medida que se adicionam jogadores à equipe, é possível ter mais jogadores que atuam em determinada posição do que a quantidade de jogadores limite, estabelecida na formação. Neste caso, os jogadores selecionados para formar o time devem ser aqueles com maior habilidade. Em caso de empate, deve ser selecionado aquele que foi adicionado à equipe primeiro. (Obs.: A quantidade de goleiros no time é sempre igual a 1). Os jogadores devem ser adicionados ao time em ordem decrescente de habilidade e, em caso de empate, respeitando a ordem de contratação.

Caso não haja jogadores suficientes em determinada(s) posição(ões) para compor o time, deve-se apresentar a seguinte mensagem:

“Estão faltando jogadores no time:”

E, nas linhas seguintes, deve-se apresentar a quantidade de jogadores que faltam APENAS nas posições em que realmente faltarem jogadores

1 goleiro

x defensores

y meias

z atacantes

Caso o time tenha sido montado com sucesso, o mesmo deve ser apresentado conforme apresentado na imagem a seguir:




Regras de desenho do campo de futebol (16x40 - sem contar com as bordas):

O campo nome de cada jogador possui uma quantidade de espaços variável, a depender da quantidade de jogadores em cada posição da formação. Esta quantidade de espaços é obtida dividindo-se igualmente a quantidade de colunas do campo pela quantidade de jogadores na respectiva posição (Ex.: 40 colunas / 4 jogadores na posição = 10 espaços por jogador) (No caso de 3 jogadores, a quantidade de espaços é dada por 39/3 = 13 e o espaço sobressalente é inserido ao canto mais à direita do campo).

Caso o nome possua menos que 8 caracteres, o restante do espaço livre deve ser completado com caracteres de espaço (“ “), o mais igualmente distribuídos, à esquerda e à direita do nome, possível. Caso haja uma quantidade ímpar de espaços, o espaço adicional deve ser inserido à direita do nome do jogador.

O nome dos jogadores deve aparecer em campo, da esquerda para a direita, na ordem em que foram adicionados ao time.

O espaçamento entre os caracteres “o”, abaixo do nome dos jogadores, também depende da quantidade de jogadores na respectiva posição. Há 3 formas de espaçamento, que são apresentados a seguir:
2 jogadores: “|{9*””}o{19*” ”}o{10*” ”}|”

3 jogadores: “|{5*””}o{12*” ”}o{12*” ”}o{8*" "}|”

4 jogadores: “|{4*””}o{9*” ”}o{9*” ”}o{9*" "}o{5*””}|”

No caso do goleiro, seu nome deve ser posicionado no intervalo contido entre os caracteres “|”, mais internos ao campo, que contém uma quantidade fixa de 10 espaços. O nome deve ser posicionado o mais centralizado possível e, para nomes com uma quantidade ímpar de caracteres, o espaço adicional deve ser inserido à direita do nome.


Finalizar o Programa
Para selecionar esta função o usuário deve inserir o número 5 no teclado

Esta função finaliza o programa
