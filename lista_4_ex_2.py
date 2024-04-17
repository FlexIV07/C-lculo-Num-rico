import numpy as np

def f(x):

    return x**3 + np.log(x)



def regra_de_simpson(a, b, passos, f):

    x = np.linspace(a, b, passos+1)

    h = (b - a) / passos

    integral = f(a) + f(b)

    for i in range(1, passos, 2):

        integral += 4 * f(a + i * h)

    for i in range(2, passos-1, 2):

        integral += 2 * f(a + i * h)

    integral *= h / 3

    return integral



def regra_com_condicionais(a, b, max_passos, desired_error, f):

    n = 2 

    while n <= max_passos:

        integral = regra_de_simpson(a, b, n, f)


        proxima_integral = regra_de_simpson(a, b, n*2, f)

        error_estimate = abs(proxima_integral - integral)

        if error_estimate < desired_error:

            return integral, n

        n *= 2

    return None, None



erro_desjado = 1e-3
result, subintervals = regra_com_condicionais(1, 2, 4, erro_desjado, f)

print(result, subintervals)
