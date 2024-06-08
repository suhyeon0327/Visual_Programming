import os

print(f'{os.path.realpath(__file__)=}')
print(f'{__name__=}')

c_module_path = os.path.realpath(__file__)
c_module_dir = os.path.dirname(c_module_path)
print(c_module_dir)
print(c_module_dir + "./week4/img/sun.png")

print