from importlib import import_module
from time import time

year = 2023
day = 1
part = 1

solution = import_module(f'year{year}.day{day:02d}.part{part}')


print("DATA : ", end='')
data = solution.prepare(f'year{year}/day{day:02d}/input.txt')
print("OK")


start_time = time()
print("FLAG :", solution.solve(data))
print(f"SOLVED IN : {time() - start_time:.3f} s")