import matplotlib.pyplot as plt
import numpy as np

def rys_wyk(wzor):
    x = np.linspace(-10, 10, 400)
    y = eval(wzor)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=wzor, color='blue')
    plt.title('Wykres funkcji: ' + wzor)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()



wzor = input("Podaj wzor funkcji: ")

rys_wyk(wzor)