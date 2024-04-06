#shell script i dont want exeute each commands in temaninal
#thats y we use i want automate that process thats why we use shellscript
#for only Linux os

echo [$(date):"START"]

echo[$(date):"creating env with python 3.8 version"]

conda create --prefix ./env python=3.8 -y

echo [$(date)]: :"activating the enviroament"

source activate ./env

echo [$(date)]:"installing the  dev requirements"
 
pip install -r requiremsnts.txt

echo [$(date)]: "END"

