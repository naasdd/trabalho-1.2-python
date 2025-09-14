Para o trabalho da M1 iremos recriar o clássico jogo de campo minado, famoso jogo que vinha com a instalação do Windows:



A área de jogo consiste num campo retangular composto de quadrados Cada quadrado pode ser revelado quando selecionado, e se o quadrado selecionar tiver uma mina, o jogo acaba. Se, por outro lado, o quadrado não contiver uma mina, uma de duas coisas poderá acontecer:

Um número aparece, indicando a quantidade de quadrados adjacentes que contêm minas;
Nenhum número aparece. Neste caso, o jogo revela automaticamente os quadrados que se encontram adjacentes ao quadrado vazio, já que não podem conter minas;

O jogo é ganho quando todos os quadrados que não têm minas são revelados.



	 
	O objetivo deste trabalho é fazer uma versão desse jogo no Python utilizando o console como saída. O mapa do jogo pode ter qualquer tamanho de N x M.
	A cada rodada, o mapa do jogo deve ser desenhado,
