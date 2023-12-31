- Nome do Projeto: 
    Donkey Kong
- Descrição do projeto:
    Projeto parte da disciplina de Programação Orientada a Objetos (POO), onde o objetivo escolhido é o desenvolvimento de um jogo inspirado no Donkey Kong.
    O objetivo do jogo é ajudar o Mário a salvar a Pauline das mãos do Donkey Kong. Para isso, será preciso enfrentar alguns desafios no meio do caminho. 

- Orientações sobre como usar o programa:
    * Como inicializar o jogo?
         Entre no arquivo game_DK.py e rode-o.
    * Como encontrar as entidades do jogo?
        Elas estão todas no arquivo game_DK.py. 
    * O que é a pasta game_base? 
        É a pasta onde se encontra toda a base que dá suporte, para além das entidades, ao game. É lá que você encontrará os códigos das estruturas, sistemas, fundo, variáveis globais e códigos extras ou complementares.
    * Todas as classes estão com docstrings para melhorar o entendimento  do programa.
    * Se ocorreu uma derrota, feche o jogo e abra o arquivo game_DK.py e rode-o novamente. Logo, o jogo reiniciará. 

- Orientações de jogabilidade?
    * Como mover o mário?
        Para mover o mário, basta utilizar as setas left, up, down e right do teclado. 
    * Como pular com o mário?
        Para pular com o mário, basta utilizar a tecla space do teclado.
    * Como subir escadas com o mário? 
        Para subir escadas, basta ir até uma escada mais próxima e apertar a tecla up do teclado.
    * Como descer escadas com o mário? 
        Para descer escadas, basta ir até uma escada mais próxima e apertar a tecla down do teclado.
    * Caso algum barril venha atingir o mário, ele perderá vida e retornará para sua posição inicial. 
    * Para destruir barris, será necessário utilizar marretas. 
    * Para conseguir utilizar marretas, será perciso ir à posição de marreta mais próxima e pular com o mário até alcançá-la.

- Nomes dos Integrantes da Equipe:
    * Breno Barreto - Nota = 2:
        - Contribuição:
            - Fiz o diagrama UML;
            - Tentei implementar os barris e aumentar o nível de dificuldade;
            - Me apresentei para ajudar mesmo sem conseguir desde que entrei no grupo;

    * João Cerqueira - Nota = 5:
        - Contribuição:
            - Maior parte do código
            - Implementou a movimentação do Mário;
            - Animações de andar;
            - Pulo do Mário;
            - Animações do Pulo;
            - Lógica do ambiente:
            - Contato com as plataformas;
            - Subir numa escada atravessada por uma plataforma;
            - Lógica de gravidade, como não cair no meio da escada;
            - Pôs todas as plataformas e escadas:
            - Lógica para subir nas escadas assim como no jogo, já que são um pouco acima uma da outra;
            - Lógica do Donkey Kong lançar os barris;
            - Os barris: Lógica para aparecimento, decisão de descida em uma tal escada, aparecimento;
            - O mário conseguir continuar na mesma animação ao parar;
            - Timing das animações do Donkey Kong;
        
    * Thiago Oliveira Franca - Nota = 4:
        - Contribuição:
            - Ajudei na verificacao de erros do mypy; 
            - Ajudei na implementacao da marreta do mário para a destruicção dos barris;
            - Ajudei na melhora da subida do Mario nas Escadas;
            - Ajudei na melhora da movimentacao dos barris;
            - Ajudei na lógica para quando o Mario vence ou perde;
            
    * Thiago Dias - Nota = 1:
        - Contribuição:
            - Ajudei no diagrama UML;
            - Ajudei na correção de bug;

    * Walisson Santos Oliveira - Nota = 5:
        - Contribuição:
            - Ajudei na organização e liderança do projeto;
            - Ajudei na montagem do diagrama UML;
            - Ajudei na implementação do Donkey Kong;
            - Ajudei na implementação da Pauline;
            - Ajudei na implementação do timing da animação do Donkey kong, em consonânica com o momento exato de lançar os barris; 
            - Ajudei na implementação dos barris;
            - Ajudei na implementação do sistema de vidas do mário;
            - Ajudei na implementação da marreta do mário para destruição dos barris;
            - Ajudei na implementação no sistema de pulo do mário;
            - Ajudei na implementação da lógica de vitória ou derrota;
            - Ajudei na verificação de erros no mypy;
            - Ajudei na documentação do código, por meio da implementação de docstrings;


