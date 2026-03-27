import numpy as np
from scipy.optimize import minimize

# скорость сигнала (скорость света, м/с)
c = 3e8  

# координаты приёмников (антенн)
receivers = np.array([
    [0, 0],
    [1000, 0],
    [0, 1000]
])

# реальное положение объекта (для теста)
true_pos = np.array([400, 300])

# считаем "истинные" времена прихода сигнала
true_distances = np.linalg.norm(receivers - true_pos, axis=1)
toa = true_distances / c   

print(true_distances)

# функция ошибки (разница между измеренными и оценочными расстояниями)
def error_func(pos):
    estimated_distances = np.linalg.norm(receivers - pos, axis=1)
    return np.sum((estimated_distances - true_distances)**2)

# начальное приближение
initial_guess = np.array([0, 0])

# минимизация ошибки
result = minimize(error_func, initial_guess)

print("Истинное положение:", true_pos)
print("Оцененное положение:", result.x.round(2))
print("Истинные времена прихода сигналов (ToA):", toa.round(6))
