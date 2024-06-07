import tkinter as tk
from tkinter import messagebox
import math
from functools import reduce
import sympy

# Funções Matemáticas

def verificar_primo(num):
    return sympy.isprime(num)

def calcular_mmc(a, b):
    return abs(a * b) // math.gcd(a, b)

def calcular_mdc(a, b):
    return math.gcd(a, b)

def verificar_par_ou_impar(num):
    return 'Par' if num % 2 == 0 else 'Ímpar'

def fatoracao(num):
    return sympy.factorint(num)

def verificar_multiplo(a, b):
    return a % b == 0

def verificar_divisibilidade(a, b):
    return a % b == 0

# Funções da Interface

def show_result(result):
    messagebox.showinfo("Resultado", result)

def handle_verificar_primo():
    num = int(entry1.get())
    result = "Primo" if verificar_primo(num) else "Não é primo"
    show_result(result)

def handle_calcular_mmc():
    a, b = int(entry1.get()), int(entry2.get())
    result = f"MMC de {a} e {b}: {calcular_mmc(a, b)}"
    show_result(result)

def handle_calcular_mdc():
    a, b = int(entry1.get()), int(entry2.get())
    result = f"MDC de {a} e {b}: {calcular_mdc(a, b)}"
    show_result(result)

def handle_verificar_par_ou_impar():
    num = int(entry1.get())
    result = verificar_par_ou_impar(num)
    show_result(result)

def handle_fatoracao():
    num = int(entry1.get())
    result = fatoracao(num)
    result_str = ' * '.join([f"{k}^{v}" for k, v in result.items()])
    show_result(result_str)

def handle_verificar_multiplo():
    a, b = int(entry1.get()), int(entry2.get())
    result = f"{a} é múltiplo de {b}" if verificar_multiplo(a, b) else f"{a} não é múltiplo de {b}"
    show_result(result)

def handle_verificar_divisibilidade():
    a, b = int(entry1.get()), int(entry2.get())
    result = f"{a} é divisível por {b}" if verificar_divisibilidade(a, b) else f"{a} não é divisível por {b}"
    show_result(result)

# Configuração da Interface Gráfica

root = tk.Tk()
root.title("Calculadora Matemática")

tk.Label(root, text="Número 1:").grid(row=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Número 2:").grid(row=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Verificar Primo", command=handle_verificar_primo).grid(row=2, column=0)
tk.Button(root, text="Calcular MMC", command=handle_calcular_mmc).grid(row=2, column=1)
tk.Button(root, text="Calcular MDC", command=handle_calcular_mdc).grid(row=3, column=0)
tk.Button(root, text="Verificar Par ou Ímpar", command=handle_verificar_par_ou_impar).grid(row=3, column=1)
tk.Button(root, text="Fatoração", command=handle_fatoracao).grid(row=4, column=0)
tk.Button(root, text="Verificar Múltiplo", command=handle_verificar_multiplo).grid(row=4, column=1)
tk.Button(root, text="Verificar Divisibilidade", command=handle_verificar_divisibilidade).grid(row=5, column=0)

root.mainloop()
