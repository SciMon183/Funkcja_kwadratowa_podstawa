import numpy as np
from pylab import *
#zmienne
a = float(input("podaj współczynnik a: "))
b = float(input("podaj współczynnik b: "))
c = float(input("podaj współczynnik c: "))
delta = float(0)
x0 = float(0)
x1 = float(0)
x2 = float(0)
wp = float(0)
wq = float(0)
#funkcje
def delta_i_miejsca(a, b, c):
    #liczenie delty
    if a != 0:
        delta = b ** 2 - (4 * a * c)
    #liczenie miejsc zerowych
    if delta == 0:
        x0 = -b / (2 * a)
        print(f"twoja delta to {delta} a miejsce zerowe twojej funkcji to {x0}")
    elif delta > 0:
        x1 = (- b - (delta ** 0.5)) / (2 * a)
        x2 = (- b + (delta ** 0.5)) / (2 * a)
        print(f"twoja delta to {delta} a miejsca zerowe twojej funkcji to {x1} i {x2}")
    else:
        print(f"twoja delta to {delta} a twoja funkcja nie posiada miejsc zerowych")

def rysuj_wykres(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    x = np.linspace(-10, 10, 400)
    y = (a * (x ** 2)) + (b * x) + c
    x0 = -b / (2 * a)
    x1 = (-b - np.sqrt(delta)) / (2 * a)
    x2 = (-b + np.sqrt(delta)) / (2 * a)
    p = -b / (2 * a)
    q = -delta / (4 * a)

    # Oznaczenie miejsc zerowych
    if delta == 0:
        plt.scatter(x0, a * x0 ** 2 + b * x0 + c, color='black', label=f'Miejsce zerowe: x = {x0}')
    elif delta > 0:
        plt.scatter([x1, x2], [a * x1 ** 2 + b * x1 + c, a * x2 ** 2 + b * x2 + c], color='pink', label=f'Miejsca zerowe: x1 = {x1}, x2 = {x2}')

    # Wykres tabele i oznaczenia 
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres funkcji kwadratowej')
    # Oznaczenie wierzchołka
    plt.scatter(p, q, color='orange', label=f'Wierzchołek: ({p}, {q})')
    plt.legend()
    plt.grid(True)
    plt.show()
#wynik
if a == 0:
    print("By funkcja była kwadrafowa współczynnik a nie może być równy zero")
else:
    delta_i_miejsca(a, b, c)
    rysuj_wykres(a, b, c)