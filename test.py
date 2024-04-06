import os

path ="notebooks\research.research.ipynb"

dir ,file=os.path.split(path)

os.makedirs(dir)

"""with open(file,"w")as f:
    pass"""