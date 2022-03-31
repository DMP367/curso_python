#%%

from os.path import isdir
from os import listdir

list_dir = listdir('/home/daniel/')

for i in list_dir:
    print(f'{i} é um diretorio: {isdir("/home/daniel/")}')