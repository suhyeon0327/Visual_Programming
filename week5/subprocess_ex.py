import subprocess

ret_v = subprocess.run(['dir'], shell=True, capture_output=True, encoding='cp949')
ret_v = subprocess.run(['notepad.exe'], shell=True, capture_output=True, encoding='cp949')

a = 'dir'
b = a.split
b