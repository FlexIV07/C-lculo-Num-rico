"""
º Ponto fixo:
    Para uma função f qualquer, se

    f(x*) = x*, x* é a raiz da função

    dizemos que x*, é um ponto fixo da função f(x*)

    fonte: https://www.youtube.com/watch?v=_PQXKn0djE8
"""

import math
import matplotlib.pyplot as plt


class FixPoint:

    def __init__(self, a_value: float, x0_value: float):
        self.a = a_value
        self.x0 = x0_value
        self.epsilon = 1e-6
        self.max_iter = 1000
        self.x_results_list = list()
        self.cont_qtd_inter_list = list()

    def g_func(self, x:float, a:float) -> float:
        return x * (x**2 + 3*a) / (3*x**2 + a) # simplificação da função
    
    def expect_a_srqrt(self, a:float) -> float:
        return math.sqrt(a)
    
    def inter_proc(self) -> float:
        x_prev = self.x0 # valor de x prévio
        cont_qtd_inter = 0 # variável para calcular a qtd de interações

        for _ in range(self.max_iter): # inicialização do looping com o max de interações até 1000

            x_next = self.g_func(x_prev, self.a) # calcula o próximo valo de x com base no x passado
            cont_qtd_inter += 1 # registra a interação
            self.x_results_list.append(x_next) # salva o valo de x em uma lista para a plotagem do gráfico
            self.cont_qtd_inter_list.append(cont_qtd_inter) # salva o num da interação para a plotagem do gráfico
            if abs(x_next - x_prev) < self.epsilon: # verifica se a função ainda
                return f"O valor da raiz de {self.a} é {x_next}" # caso não seja mais, retonra o valor da interação
            
            x_prev = x_next # caso ainda seja contínua, atribui o novo valor do x prévio
        return None # se a interação estourar a qtd máxima de interação a função retorna None
    
    def graphic(self):
        raiz_esperada = self.expect_a_srqrt(self.a)
        plt.style.use('seaborn')
        plt.plot(self.x_results_list,
                 self.cont_qtd_inter_list,
                 marker='o', 
                 linestyle='-', 
                 color='blue', 
                 label='Dados')
        plt.xlabel('Valore da Interação')
        plt.ylabel('Numero de interação')
        plt.title(f'Gráfico do Cálculo de Ponto Fixo de a: {self.a} com a raiz esperada de {raiz_esperada}')
        plt.show()