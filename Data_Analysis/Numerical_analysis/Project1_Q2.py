## 2번

import numpy as np
import matplotlib.pyplot as plt
import math

class RootEstimator:

    def __init__(self, a, b, c, eps = 0.001):
        self.a = a
        self.b = b
        self.c = c
        self.eps = eps
        return

    def f(self, x):
        return(x - self.a) * (x - self.b) * (x - self.c)

    def df(self, x):
        # f(x) = x ^ 3 -(a+b+c)* x^2 + (ab+ac+bc)*x - abc
        # chain rule
        return (x - self.a) * (x - self.b) +  (x - self.a) * (x - self.c) + (x - self.b) * (x - self.c)

    def g(self, x):
        d = - (self.a*self.b + self.a*self.c + self.b*self.c) # => x = g(x)
        return ((x - self.a) * (x - self.b) * (x - self.c)  + d*x) /d

    def plot_f_x(self):
        x = np.arange(self.a - 1, self.c + 1.1, 0.01)
        y = [self.f(x_i) for x_i in x]
        title = f'f(x) = (x - {self.a})(x - {self.b})(x - {self.c})'
        plt.plot(x, y)
        plt.title(title)
        plt.grid()
        plt.show()

        return

    def bisection_method(self, xl, xu):
      n_i = 0
      if self.f(xl) * self.f(xu) >= 0:
        print("There's no roots")
        return

      while xu - xl > self.eps:
        n_i += 1
        xr = (xl + xu) / 2
        D = self.f(xl) * self.f(xr)

        if D <= 0:
            xu = xr
        elif D > 0:
            xl = xr

        Et = np.abs((xu - xl) / xu)

        if n_i >=  2:
          Ea = np.abs((xr - (xl+xu)/2) / xr)
        else: Ea = np.nan

        print(f'n = {n_i} --> xl : {xl:.4f}, xu: {xu:.4f}, xr: {(xl + xu) / 2:4f}, Ea: {Ea:4f}%, error: {Et:.4f}%')

      return

    def fixedPointIteration_method(self, x_old):
      n_i = 0

      xx = np.arange(self.a - 1, self.c + 1.1, 0.01)
      y1 = xx
      plt.plot(xx, self.g(xx), label="x = g(x)")
      plt.plot(xx, y1, label="y = x")
      plt.legend()

      prev_Et = 100
      while abs(self.g(x_old) - x_old) >= self.eps:
        n_i += 1
        x_new = self.g(x_old)

        Et = np.abs((x_new - x_old) / x_new) * 100
        ratio = Et / prev_Et
        print(f'n = {n_i} --> result : {x_new:.4f}, error:{Et:.4f}, ratio = {ratio:.4f}')
        prev_Et = Et
        x_old = x_new

        plt.plot(x_new, self.g(x_new), 'm.')
      plt.show()

      return

    def newtonRaphson_method(self, x_old):
        n_i = 0 # number of iteration

        x = np.arange(self.a - 1, self.c + 1.1, 0.01)
        y = self.f(x)
        plt.plot(x, y)
        plt.grid()

        while abs(self.f(x_old) / self.df(x_old)) >= self.eps:
            n_i += 1

            x_new = x_old - (self.f(x_old) / self.df(x_old))

            plt.scatter(x_old, self.f(x_old))

            Et = np.abs((x_new - x_old) / x_new) * 100
            print(f'n = {n_i}, x_new = {x_new:.4f}, Error: {Et :4f}')
            x_old = x_new

        plt.show()

        return


if __name__ == "__main__":
    # 2 - 1
    a, b, c = 1, 2, 3
    xl = 0.5
    xu = 1.5
    re = RootEstimator(a, b, c)
    re.plot_f_x()
    # 2 - 2
    print("\n< bisection method >\n")
    re.bisection_method(xl, xu)
    print("\n< Simple fixed-point iteration method >\n")
    re.fixedPointIteration_method(xl)
    print("\n< Newton-Raphson method >\n")
    re.newtonRaphson_method(xl)