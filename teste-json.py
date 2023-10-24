import json
from random import randint
import time

with open("lixeiras2.json", "r") as lixeiras_json:
    dados_lixeiras = json.load(lixeiras_json)

for keys in dados_lixeiras:
    sensor_enchimento = randint(0, 100)
    dados_lixeiras[keys].update({'Enchimento (%)':sensor_enchimento})
    if sensor_enchimento < 50:
        dados_lixeiras[keys].update({'Coleta':'Concluida'})
    elif sensor_enchimento >= 50 and sensor_enchimento < 75:
        dados_lixeiras[keys].update({'Coleta':'Pendente'})
    else:
        dados_lixeiras[keys].update({'Coleta':'Em andamento'})


with open("lixeiras2.json", "w") as lixeiras_json:
    json.dump(dados_lixeiras, lixeiras_json)