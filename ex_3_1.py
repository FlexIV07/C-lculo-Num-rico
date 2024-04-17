import sympy
import matplotlib.pyplot as plt

# valores_de_x = [0, 0.5, 1, 1.5, 2, 2.5, 3]
# valores_de_y = [1.8421, 2.4694, 2.4921, 1.9047, 0.8509, -0.4112, -1.5727]

pontos = [(0, 1.8421), (0.5, 2.4694), 
          (1, 2.4921), (1.5, 1.9047),
          (2, 0.8509), (2.5, -0.4112),
          (3, -1.5727)]

x = sympy.symbols("x")

# tres_pontos_consecutivos = pontos[:3]

# y0 = tres_pontos_consecutivos[0][1]
# x0 = tres_pontos_consecutivos[0][0]
# y1 = tres_pontos_consecutivos[1][1]
# x1 = tres_pontos_consecutivos[1][0]
# y2 = tres_pontos_consecutivos[2][1]
# x2 = tres_pontos_consecutivos[2][0]

# expressao_1 = (y0 * ( (x-x1) * (x-x2))) / ((x0-x1) * (x0-x2))
# expressao_2 = (y1 * ( (x-x0) * (x-x2))) / ((x1-x0) * (x1-x2))
# expressao_3 = (y2 * ( (x-x0) * (x-x1))) / ((x2-x0) * (x2-x1))

# funcao_completa = expressao_1 + expressao_2 + expressao_3

# print(funcao_completa)

# funcao_simplificada = sympy.simplify(funcao_completa)

# print(funcao_completa)


class TresPontos:

    x = sympy.symbols("x")

    def __init__(self, pontos):
        self.pontos = pontos
        self.pontos_divididos : list
        self.y0 : float
        self.x0 : float
        self.y1 : float
        self.x1 : float
        self.y2 : float
        self.x2 : float
        self.expressao_1 : sympy.core.mul.Mul
        self.expressao_2 : sympy.core.mul.Mul
        self.expressao_3 : sympy.core.mul.Mul
        self.funcao_completa : sympy.core.mul.Mul
        self.funcao_simplificada : sympy.core.mul.Mul
        self.valores_na_funcao_calculda = list()
        self.erros_absolutos = list()
        self.raizes_no_ponto = list()

    def slice_dos_pontos(self, tipo_de_divisao: str):
        if tipo_de_divisao == "INICIAL":
            self.pontos_divididos = self.pontos[0:3]
        
        if tipo_de_divisao == "INTERCALADA":
            lista_intercalada = list()
            
            ponto_1 = self.pontos[0]
            lista_intercalada.append(ponto_1)

            ponto_2 = self.pontos[2]
            lista_intercalada.append(ponto_2)

            ponto_3 = self.pontos[4]        
            lista_intercalada.append(ponto_3)

            self.pontos_divididos = lista_intercalada

        if tipo_de_divisao == "FINAL":
            self.pontos_divididos = self.pontos[-3:]

    def atribuicao_das_variaveis(self):        
        self.y0 = self.pontos_divididos[0][1]
        self.x0 = self.pontos_divididos[0][0]
        self.y1 = self.pontos_divididos[1][1]
        self.x1 = self.pontos_divididos[1][0]
        self.y2 = self.pontos_divididos[2][1]
        self.x2 = self.pontos_divididos[2][0]

    def expressoes(self):
        self.expressao_1 = (self.y0 * ( (x-self.x1) * (x-self.x2))) \
                          / ((self.x0-self.x1) * (self.x0-self.x2))
        
        self.expressao_2 = (self.y1 * ( (x-self.x0) * (x-self.x2))) \
                           / ((self.x1-self.x0) * (self.x1-self.x2))
        
        self.expressao_3 = (self.y2 * ( (x-self.x0) * (x-self.x1))) \
                           / ((self.x2-self.x0) * (self.x2-self.x1))
        
    def funcao_completa(self):
        self.funcao_completa = self.expressao_1 + self.expressao_2 + self.expressao_3
    
    def funcao_simplificada(self):
        self.funcao_simplificada = sympy.simplify(self.funcao_completa)

    def funcoes_no_ponto_calculada(self):
        for ponto in self.pontos:
            funcao_no_ponto = self.funcao_simplificada.subs(x, ponto[0])
            self.valores_na_funcao_calculda.append(funcao_no_ponto)
    
    def calcular_erro_absoluto(self):
        for i in range(len(self.pontos)):
            erro_no_ponto = self.pontos[i][1] - self.valores_na_funcao_calculda[i]
            self.erros_absolutos.append(erro_no_ponto)
    
    def raizes_da_funcao(self):
        raizes = sympy.solve(self.funcao_simplificada, x)
        
        raiz_1 = raizes[0]
        valor_no_ponto_raiz_1 = self.funcao_simplificada.subs(x, raiz_1)
        self.raizes_no_ponto.append((raiz_1, valor_no_ponto_raiz_1))

        raiz_2 = raizes[1]
        valor_no_ponto_raiz_2 = self.funcao_simplificada.subs(x, raiz_2)
        self.raizes_no_ponto.append((raiz_2, valor_no_ponto_raiz_2))


    
    def grafico_resultados(self):
        plt.style.use('Solarize_Light2')
        valores_de_x = [ponto[0] for ponto in self.pontos]
        valores_de_y = self.valores_na_funcao_calculda
        
        plt.plot(valores_de_x,
                 valores_de_y,
                 marker="o",
                 linestyle="-",
                 color="green",
                 label="Resultados")
        
        y_erro = list()

        for erro in self.erros_absolutos:
            if erro < 0:
                erro_ajustado = erro * -1
                y_erro.append(erro_ajustado)
            else:
                y_erro.append(erro)
        
        plt.errorbar(valores_de_x,
                     valores_de_y,
                     yerr=y_erro,
                     fmt="o")
        
        raizes_x = [self.raizes_no_ponto[0][0], self.raizes_no_ponto[1][0]]
        raizes_y = [self.raizes_no_ponto[0][1], self.raizes_no_ponto[1][1]]

        plt.scatter(raizes_x,
                 raizes_y,
                 marker="o",
                 color="red",
                 label="Raizes")

        plt.xlabel("VALORES DE X")
        plt.ylabel("VALORES CALCULADOS PELA INTERPOLACÃO")
        plt.title(f"RESULTADOS DA INTERPOLAÇÃO PARA A FUNÇÃO: {self.funcao_simplificada}")
        plt.show()
    
    def interporlar(self, metodo_de_divisao:str):
        self.slice_dos_pontos(metodo_de_divisao)
        self.atribuicao_das_variaveis()
        self.expressoes()
        self.funcao_completa()
        self.funcao_simplificada()
        self.funcoes_no_ponto_calculada()
        self.calcular_erro_absoluto()
        self.raizes_da_funcao()
        self.grafico_resultados()

class QuatroPontos:

    x = sympy.symbols("x")

    def __init__(self, pontos):
        self.pontos = pontos
        self.pontos_divididos : list
        self.y0 : float
        self.x0 : float
        self.y1 : float
        self.x1 : float
        self.y2 : float
        self.x2 : float
        self.y3 : float
        self.x3 : float
        self.expressao_1 : sympy.core.mul.Mul
        self.expressao_2 : sympy.core.mul.Mul
        self.expressao_3 : sympy.core.mul.Mul
        self.expressao_4 : sympy.core.mul.Mul
        self.funcao_completa : sympy.core.mul.Mul
        self.funcao_simplificada : sympy.core.mul.Mul
        self.valores_na_funcao_calculda = list()
        self.erros_absolutos = list()
        self.raizes_no_ponto = list()



    def slice_dos_pontos(self, tipo_de_divisao: str):
        if tipo_de_divisao == "INICIAL":
            self.pontos_divididos = self.pontos[0:4]
        
        if tipo_de_divisao == "INTERCALADA":
            lista_intercalada = list()
            
            ponto_1 = self.pontos[0]
            lista_intercalada.append(ponto_1)

            ponto_2 = self.pontos[2]
            lista_intercalada.append(ponto_2)

            ponto_3 = self.pontos[4]        
            lista_intercalada.append(ponto_3)

            ponto_4 = self.pontos[6]
            lista_intercalada.append(ponto_4)

            self.pontos_divididos = lista_intercalada

        if tipo_de_divisao == "FINAL":
            self.pontos_divididos = self.pontos[-4:]

    def atribuicao_das_variaveis(self):        
        self.y0 = self.pontos_divididos[0][1]
        self.x0 = self.pontos_divididos[0][0]
        self.y1 = self.pontos_divididos[1][1]
        self.x1 = self.pontos_divididos[1][0]
        self.y2 = self.pontos_divididos[2][1]
        self.x2 = self.pontos_divididos[2][0]
        self.y3 = self.pontos_divididos[3][1]
        self.x3 = self.pontos_divididos[3][0]

    def expressoes(self):
        self.expressao_1 = (self.y0 * ( (x-self.x1) * (x-self.x2) * (x-self.x3))) \
                          / ((self.x0-self.x1) * (self.x0-self.x2) * (self.x0-self.x3))
        
        self.expressao_2 = (self.y1 * ( (x-self.x0) * (x-self.x2) * (x-self.x3))) \
                           / ((self.x1-self.x0) * (self.x1-self.x2) * (self.x1-self.x3))
        
        self.expressao_3 = (self.y2 * ( (x-self.x0) * (x-self.x1) * (x-self.x3))) \
                           / ((self.x2-self.x0) * (self.x2-self.x1) * (self.x2-self.x3))
        
        self.expressao_4 = (self.y3 * ( (x-self.x0) * (x-self.x1) * (x-self.x2))) \
                           / ((self.x3-self.x0) * (self.x3-self.x1) * (self.x3-self.x2))
        
    def funcao_completa(self):
        self.funcao_completa = self.expressao_1 + self.expressao_2 + self.expressao_3 + self.expressao_4
    
    def funcao_simplificada(self):
        self.funcao_simplificada = sympy.simplify(self.funcao_completa)

    def funcoes_no_ponto_calculada(self):
        for ponto in self.pontos:
            funcao_no_ponto = self.funcao_simplificada.subs(x, ponto[0])
            self.valores_na_funcao_calculda.append(funcao_no_ponto)
    
    def calcular_erro_absoluto(self):
        for i in range(len(self.pontos)):
            erro_no_ponto = self.pontos[i][1] - self.valores_na_funcao_calculda[i]
            self.erros_absolutos.append(erro_no_ponto)
    
    def calcular_raizes(self):
        raizes = sympy.solve(self.funcao_simplificada, x)

        raiz_1 = raizes[0].as_real_imag()[0]
        valor_no_ponto_raiz_1 =  self.funcao_simplificada.subs(x, raiz_1)
        self.raizes_no_ponto.append((raiz_1, valor_no_ponto_raiz_1))

        raiz_2 = raizes[1].as_real_imag()[0]
        valor_no_ponto_raiz_2 = self.funcao_simplificada.subs(x, raiz_2)
        self.raizes_no_ponto.append((raiz_2, valor_no_ponto_raiz_2))

        raiz_3 = raizes[2].as_real_imag()[0]
        valor_no_ponto_raiz_3 = self.funcao_simplificada.subs(x, raiz_3)
        self.raizes_no_ponto.append((raiz_3, valor_no_ponto_raiz_3))

    
    def grafico_resultados(self):
        plt.style.use('Solarize_Light2')
        valores_de_x = [ponto[0] for ponto in self.pontos]
        valores_de_y = self.valores_na_funcao_calculda
        
        plt.plot(valores_de_x,
                 valores_de_y,
                 marker="o",
                 linestyle="-",
                 color="green",
                 label="Resultados")
        
        y_erro = list()

        for erro in self.erros_absolutos:
            if erro < 0:
                erro_ajustado = erro * -1
                y_erro.append(erro_ajustado)
            else:
                y_erro.append(erro)
        
        plt.errorbar(valores_de_x,
                     valores_de_y,
                     yerr=y_erro,
                     fmt="o")
        
        raizes_x = [self.raizes_no_ponto[0][0], self.raizes_no_ponto[1][0], self.raizes_no_ponto[2][0]]
        raizes_y = [self.raizes_no_ponto[0][1], self.raizes_no_ponto[1][1], self.raizes_no_ponto[2][1]]

        # raizes_x = [self.raizes_no_ponto[1][0], self.raizes_no_ponto[2][0]]
        # raizes_y = [self.raizes_no_ponto[1][1], self.raizes_no_ponto[2][1]]

        plt.scatter(raizes_x,
                 raizes_y,
                 marker="o",
                 color="red",
                 label="Raizes")

        plt.xlabel("VALORES DE X")
        plt.ylabel("VALORES CALCULADOS PELA INTERPOLACÃO")
        plt.title(f"RESULTADOS DA INTERPOLAÇÃO PARA A FUNÇÃO: {self.funcao_simplificada}")
        plt.show()
    
    def interporlar(self, metodo_de_divisao:str):
        self.slice_dos_pontos(metodo_de_divisao)
        self.atribuicao_das_variaveis()
        self.expressoes()
        self.funcao_completa()
        self.funcao_simplificada()
        self.funcoes_no_ponto_calculada()
        self.calcular_erro_absoluto()
        self.calcular_raizes()
        self.grafico_resultados()
    
