# -*- coding: utf-8 -*-
"""
JOGO DA COBRINHA

Created on Wed Apr 12 18:47:56 2017

- Virgínia Boina Dalvi.

"""

# ======================================================================
#
#   M A I N 
#
# ======================================================================
def main():

    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()
    
    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols   = int(input('Número de colunas do tabuleiro: '))
    x       = int(input('Posição x inicial da cobrinha : '))
    y       = int(input('Posição y inicial da cobrinha : '))
    t       = int(input('Tamanho da cobrinha           : '))

    # Obtendo x0 e y0 iniciais descontando as bordas
    # e admitindo posição inicial (0,0)
    x0=x+2
    y0=y+2

    # Verifica se o corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cabeça
    if (x - (t - 1)) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")
        
    else:

        ''' Inicia a variável d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t-1: 
            d = d * 10 + 2
            i = i + 1
        
        # Laço que controla a interação com o jogador
        direcao = 1
        while direcao != 5:
            # Mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d)
            
            # Lê o número do próximo movimento que será executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu próximo movimento: "))
            
            if direcao != 5:
                # Atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

    print()        
    print("Tchau!")
    

# ======================================================================

def num_digitos(n):
    """ (int) -> int

    Devolve o número de dígitos de um número.

    ENTRADA
    - n: número a ser verificado 

    """
   
    z = str(n)
    n = len(z)
    
    return n
 
    
# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrário.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    
    """

    if x == x0 and y == y0:
        return True
    
    while d%10 != 0:
    
    
        if d%10 == 1:
            x0 += 1
            if x == x0 and y == y0:
                return True
        if d%10 == 2:
            x0 -= 1
            if x == x0 and y == y0:
                return True
        if d%10 == 3:
            y0 += 1
            if x == x0 and y == y0:
                return True
        if d%10 == 4:
            y0 -= 1
            if x == x0 and y == y0:
                return True
        d = d//10
    
    return False


# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
         
    """

    conty = 1
    while conty <= nlinhas + 2:
        contx = 1
        # Impressaão das bordas
        print('#', end="")
        if (conty == 1 or conty == nlinhas + 2):
            cont=1
            while cont <= ncols:
                print('#', end="")
                cont = cont + 1
        
        while contx <= ncols + 1:
       
            if pos_ocupada(nlinhas, ncols, contx, conty, x0, y0, d):
                if x0 == contx and y0 == conty:
                    print('C', end="")
                else:
                    print('*', end="")
            else:
                if contx != 1 and contx != ncols+2 and conty != 1 and conty != nlinhas+2:
                    print('.', end="")
           
            contx = contx + 1
            
        # Impressão da borda final
        print('#', end="")
        print ("")
        conty = conty + 1
    


# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direção dada.    
    A função devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento é impossível (pois a cobra vai colidir consigo mesma ou
    com a parede), então a função devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃO CONSIGO MESMA" ou "COLISÃO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    - direcao: direção na qual a cabeça deve ser movida
    
    """
 
    if direcao == 1:
        x = x0 - 1
        y = y0
        
    if direcao == 2:
        x = x0 + 1
        y = y0
            
    if direcao == 3:
        x = x0
        y = y0 - 1
                
    if direcao == 4:
        x = x0
        y = y0 + 1
                
    if pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
        print()
        print("COLISÃO CONSIGO MESMA")
        print()
        
        return x0, y0, d
        
    if x == 1 or x == ncols+2 or y == 1 or y == nlinhas+2:
        print()
        print("COLISÃO COM A PAREDE")
        print()
        
        return x0, y0, d
                    
    # Determinação deslocamento
    d = d % (10 ** (num_digitos(d) - 1))    
    d = d*10 + direcao

    
    return x, y, d

# ======================================================================
main()     
