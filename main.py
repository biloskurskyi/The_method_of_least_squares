import matplotlib.pyplot as plt
from sympy import Symbol
from numpy import linalg
import sympy

print('The method of least squares for a linear function')
_ = 'y=kx+b'
print(_.center(40))
x = []
y = []
num_xy = int(input('Input number of points: '))
step = int(input('input step for x: '))
x1 = 0
for i in range(num_xy):
    if i == 0:
        print('Input x[' + str(i) + ']: ', end='')
        x1 = float(input())
    elif i != 0 and step > 0:
        x1 += step
        print('Next x[' + str(i) + ']: ' + str(x1))
    print('Input y[' + str(i) + ']: ', end='')
    y1 = float(input())
    x.append(x1)
    y.append(y1)
print('Your x:', *x)
print('Your y:', *y)
sum_mult_xy = 0
for i in range(num_xy):
    mult_xy = x[i] * y[i]
    sum_mult_xy += x[i] * y[i]
print('Sum of mult x[i] and y[i]:', sum_mult_xy)
sum_x = 0
for i in range(num_xy):
    sum_x += x[i]
print('Sum of x:', sum_x)
sum_y = 0
for i in range(num_xy):
    sum_y += y[i]
print('Sum of x:', sum_y)
sqrt_sum_x = 0
cnt_i = 0
for i in range(num_xy):
    sqrt_sum_x += x[i] ** 2
    cnt_i = i + 1
print('Sum of sqrt x:', sqrt_sum_x)
k = (num_xy * sum_mult_xy - sum_x * sum_y) / (num_xy * sqrt_sum_x - sum_x ** 2)
b = (sum_y - k * sum_x) / num_xy
print('coefficients k is ' + str(k) + ', b is ' + str(b))
print('Our linear function: ')
_2 = 'y = ' + str(k) + 'x +(' + str(b) + ')'
print(_.center(40))
y_fun = []
x_step = x[0]
x_fun = []
num_xy_2 = int(input('Input number of iteration: '))
for i in range(num_xy_2):
    y_fun_ = k * x_step + b
    y_fun.append(y_fun_)
    x_fun.append(x_step)
    x_step += step
print('Your x:', *x_fun)
print('Your y:', *y_fun)
print(_2.center(40))
plt.title(_2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
for i in range(num_xy_2):
    if i in x and i in x_fun:
        plt.scatter(x, y, color='red')
    if i == cnt_i:
        plt.scatter(x_fun[i], y_fun[i], color='blue')
    if i not in x and i in x_fun:
        plt.scatter(x_fun[i], y_fun[i], color='blue')
plt.plot(x_fun, y_fun, color='green')
plt.grid()
plt.show()
print('---')
print('The method of least squares for a function in power')
_ = 'y=x^m'
print(_.center(40))
x2_fun = sympy.sympify(input('Enter your function: '))
print('Input a: ', end='')
a = int(input())
print('Input b: ', end='')
b = int(input())
x2 = Symbol('x')
n = 4
step2 = (b - a) / n


x_arr = []
y_arr = []
for i in range(n+1):
    x_arr.append(a + i * step2)
print('points on x:', *x_arr)
for i in x_arr:
    y_arr.append(x2_fun.subs(x2, i))
print('points on y:', *y_arr)


def s1(f1, f2, x_arr):
    sum_ = 0
    for i in range(len(x_arr)):
        sum_ += f1.subs(x2, x_arr[i]) * f2.subs(x2, x_arr[i])
    return sum_


def s2(f, x_arr, y_arr):
    sum_ = 0
    for i in range(len(x_arr)):
        sum_ += y_arr[i] * f.subs(x2, x_arr[i])
    return sum_


def squares_method(x_arr, y_arr):
    m = 5
    func = 0
    ind_funcs = []
    for i in range(m):
        ind_funcs.append(x2 ** i)
    matrix = []
    for i2 in range(m):
        arr_ = []
        for i2 in range(m):
            arr_.append(0)
        matrix.append(arr_)
    for i1 in range(m):
        for j1 in range(m):
            matrix[i1][j1] = float(s1(ind_funcs[j1], ind_funcs[i1], x_arr))
    print(matrix)
    arr = []
    for i4 in range(m):
        arr.append(0)
    for j2 in range(m):
        arr[j2] = float(s2(ind_funcs[j2], x_arr, y_arr))
    print(arr)

    a_coef = linalg.solve(matrix, arr)

    for i3 in range(m):
        func += a_coef[i3] * ind_funcs[i3]
    return func



func1 = squares_method(x_arr, y_arr)
print('Our function by squares method:', func1)
n2 = 1000
step3 = (b - a) / n2
x_mass2 = []
for i in range(n2 + 1):
    x_mass2.append(a + i * step3)
y_mass2 = []
for i in x_mass2:
    y_mass2.append(x2_fun.subs(x2, i))
y2_arr = []
for i in x_mass2:
    y2_arr.append(func1.subs(x2, i))
_2 = 'y = ' + str(func1)
plt.title(_2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.plot(x_mass2, y_mass2, color='blue')
plt.plot(x_mass2, y2_arr, color='red')
plt.grid()
plt.show()
