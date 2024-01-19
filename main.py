# import matplotlib.pyplot as plt
import numpy as np
from pylab import *
#funkcje
def delta_i_miejsca(a, b, c):
    if a != 0:
        delta = b ** 2 - (4 * a * c)
    if delta == 0:
        x0 = -b / (2 * a)
        print(f"twoja delta to {delta} a miejsce zerowe twojej funkcji to {x0}")
    elif delta > 0:
        x1 = (- b - (delta ** 0.5)) / (2 * a)
        x2 = (- b + (delta ** 0.5)) / (2 * a)
        print(f"twoja delta to {delta} a miejsca zerowe twojej funkcji to {x1} i {x2}")
    else:
        print(f"twoja delta to {delta} a twoja funkcja nie posiada miejsc zerowych")
def p_i_q(float):
    if a != 0:
        p = float(- b / (2 * a))
        q = float(- delta / (4 * a))
        print(f"współżędne wieszchołka to x = {p}, y = {q}")
def zamiana(int):
    if a != 0:
        print(f"podałeś funkcję w postaci ogólnej. To twoja funkcja w postaci kanonocznej: f(x) = {a}(x - {p})^2 + {q} \noraz w postaci iloczynowej: f(x) = {a}(x - {x1})(x - {x2})")
def rysuj_wykres(a, b, c):
    if a == 0:
        print("By funkcja była kwadratowa współczynnik a nie może być równy zero")
        return

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Funkcja nie ma miejsc zerowych na płaszczyźnie rzeczywistej.")
        return

    x = np.linspace(-10, 10, 400)
    y = a * x ** 2 + b * x + c

    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funkcja kwadratowa skurwysyny')

    # Oznaczenie miejsc zerowych
    if delta == 0:
        x0 = -b / (2 * a)
        plt.scatter(x0, a * x0 ** 2 + b * x0 + c, color='red', label=f'Miejsce zerowe: x = {x0}')
    elif delta > 0:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        plt.scatter([x1, x2], [a * x1 ** 2 + b * x1 + c, a * x2 ** 2 + b * x2 + c], color='red',
                    label=f'Miejsca zerowe: x1 = {x1}, x2 = {x2}')

    # Oznaczenie wierzchołka
    p = -b / (2 * a)
    q = -delta / (4 * a)
    plt.scatter(p, q, color='green', label=f'Wierzchołek: ({p}, {q})')

    plt.legend()
    plt.grid(True)
    plt.show()

#zmienne
a = float(input("podaj współczynnik a: "))
b = float(input("podaj współczynnik b: "))
c = float(input("podaj współczynnik c: "))
delta = float(0)
x0 = float(0)
x1 = float(0)
x2 = float(0)
p = float(0)
q = float(0)

#wynik
if a == 0:
    print("By funkcja była kwadrafowa współczynnik a nie może być równy zero")
else:
    delta_i_miejsca(a, b, c)
    p_i_q(float)
    zamiana(int)
    rysuj_wykres(a, b, c)
