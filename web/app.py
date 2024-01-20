#!/usr/bin/env python
import cgi
import cgitb
import numpy as np
import json

# Włącz obsługę błędów CGI
cgitb.enable()

# Odbierz dane z AJAX
form = cgi.FieldStorage()
a = float(form.getvalue('a'))
b = float(form.getvalue('b'))
c = float(form.getvalue('c'))
delta = 0
x0, x1, x2 = 0, 0, 0

# Funkcje
def delta_i_miejsca(a, b, c):
    global delta, x0, x1, x2
    # Liczenie delty
    if a != 0:
        delta = b ** 2 - (4 * a * c)
    # Liczenie miejsc zerowych
    if delta == 0:
        x0 = -b / (2 * a)
        return {'delta': delta, 'miejsce_zerowe': [x0]}
    elif delta > 0:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        return {'delta': delta, 'miejsca_zerowe': [x1, x2]}
    else:
        return {'delta': delta, 'miejsca_zerowe': []}

# Wynik
if a == 0:
    print("By funkcja była kwadratowa współczynnik a nie może być równy zero")
else:
    wynik = delta_i_miejsca(a, b, c)
    # Dodaj nagłówek Content-type
    print("Content-type: application/json\n")
    # Wypisz wynik w formie JSON
    print(json.dumps(wynik))
