import numpy as np
import matplotlib.pyplot as plt

def calcular_pi(n):
    m = 0  # Contador de pontos dentro do círculo unitário no primeiro quadrante
    for _ in range(n):
        x, y = np.random.rand(), np.random.rand()  # Gerar um par de números aleatórios entre 0 e 1
        if x**2 + y**2 <= 1:  # Verificar se o ponto está dentro do círculo unitário
            m += 1
    pi_n = 4 * m / n
    return pi_n

# Definir o número de pontos a serem gerados em cada iteração
num_iteracoes = 100
num_pontos = 1000

# Calcular a sequência de valores de pi para diferentes números de pontos
valores_pi = [calcular_pi(num_pontos) for _ in range(num_iteracoes)]

# Calcular os valores reais de pi
pi_real = np.pi
# Calcular os erros em relação ao valor real de pi
erros = [abs(pi - pi_real) for pi in valores_pi]

# Plotar o gráfico da evolução do erro
plt.plot(range(1, num_iteracoes + 1), erros)
plt.xlabel('Número de pontos gerados')
plt.ylabel('Erro em relação a π')
plt.title('Evolução do erro para valores crescentes de n')
plt.grid(True)
plt.show()