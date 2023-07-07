import os
from platform import system
from subprocess import call

if system() == 'Windows':
    try:
        call(['tar', '--version'], stdout=open(os.devnull, 'w'))
    except FileNotFoundError:
        raise Exception('tar not found, please install it')
else:
    try:
        call(['unzip', '-v'], stdout=open(os.devnull, 'w'))
    except FileNotFoundError:
        raise Exception('unzip not found, please install it')

listalivp=os.listdir()
print(listalivp)
for e in listalivp:
    if '.livp' in e:
        os.system(f'tar -xf "{e}"') if system() == 'Windows' else os.system(f'unzip -q "{e}"')
        os.system(f'del "{e}"') if system() == 'Windows' else os.system(f'rm "{e}"')
    else:
        pass

listaspacchettati=os.listdir()

os.system(f'python convert.py {os.getcwd()}')
for e in listaspacchettati:
    if '.mov' in e or ".heic" in e:
        os.system(f'del "{e}"') if system() == 'Windows' else os.system(f'rm "{e}"')
    else:
        pass
