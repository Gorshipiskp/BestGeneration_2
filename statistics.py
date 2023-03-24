from config import *
from base import Database
import os

db = Database()

os.startfile("start.py")
time.sleep(1)

for name, params in base_parameters.items():
    if params['parameters'][0].lower() == "INT".lower() and name != "id" and name != 'age':
        alll = tuple(i[0] for i in db.select(base_table, name, conditions=False))
        print(f'Average {name} = {round(sum(alll) / len(alll), 2)}')
