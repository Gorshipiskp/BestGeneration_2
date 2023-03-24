import random
from config_defs import *
from codes import *

db_name = 'db_base'
db_extension = 'db'
base_table = 'PERSONS'
language = "russian"

start_count = 100
count_days = 5
round_accuracy = 4
max_deviation = 10

show_loading_progress = True
print_errors = True
restart = True
history = False
history_coding = False

names_m = ("Денис", "Бенджамин", "Дональд", "Иван")
names_f = ("Даша", "Алина", "Майя", "Таня")
surnames_m = ("Лебедев", "Франклин", "Трамп", "Самолётов", "Соловьёв")
surnames_f = ("Лебедева", "Франклин", "Трамп", "Самолётова", "Соловьёва")
patronymics_m = ("Андреевич", "Сергеевич", "Владимирович", "Михайлович")
patronymics_f = ("Андреевна", "Сергеевна", "Владимировна", "Михайловна")

base_parameters = {
    "id": {PARAMS: ('INT', PRIMARY_KEY), KEY: PRIMARY_KEY},
    "sex": {KEY: (random.choice, [('Мужской', 'Женский')]), PARAMS: ['TEXT']},
    "name": {KEY: [(random.choice, [names_m]), (random.choice, [names_f])], PARAMS: ['TEXT'],
             CONDITION: [check, [1, 'Женский']]},
    "surname": {KEY: [(random.choice, [surnames_m]), (random.choice, [surnames_f])], PARAMS: ['TEXT'],
                CONDITION: [check, [1, 'Женский']]},
    "patronymic": {KEY: [(random.choice, [patronymics_m]), (random.choice, [patronymics_f])], PARAMS: ['TEXT'],
                   CONDITION: [check, [1, 'Женский']]},
    "age": {PARAMS: ['INT'], DEFAULT: 0, EXPENDITURE_DAY: -1},
    "money": {PARAMS: ['INT'], DEFAULT: 0},
    "health": {PARAMS: ['REAL'], DEFAULT: 100, PRIORITY: 1.1, EXPENDITURE: 0.0085, MAX_RSTR: 125},
    "hungry": {PARAMS: ['REAL'], DEFAULT: 100, PRIORITY: 1.2, EXPENDITURE: 0.015, MAX_RSTR: 115},
    "thirst": {PARAMS: ['REAL'], DEFAULT: 100, PRIORITY: 1.3, EXPENDITURE: 0.4, MAX_RSTR: 115},
    "hygiene": {PARAMS: ['REAL'], DEFAULT: 100, PRIORITY: 0.9, EXPENDITURE: 0.04, MAX_RSTR: 100},
    "rest": {PARAMS: ['REAL'], DEFAULT: 100, PRIORITY: 1, EXPENDITURE: 0.025, MAX_RSTR: 150},
    "art": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "programming": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "sport": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "writing": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "beauty": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "creativity": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "IQ": {PARAMS: ['REAL'], KEY: (random.randint, (80, 120))},
    # "patiently": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    # "sociability": {PARAMS: ['REAL'], KEY: (random.randint, (0, 15))},
    "parents": {PARAMS: ['BLOB'], DEFAULT: FIRST_SPAWN},
}

if history:
    base_parameters.update({'history': {PARAMS: ['TEXT'], DEFAULT: ''}})

base_parameters_ids = dict((name, name_id) for name_id, name in enumerate(base_parameters.keys()))
