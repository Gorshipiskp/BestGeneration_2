from codes import *

errors = {
    1: "В колонке ({0}) в таблице ({1}) одновременно указано значение key и default",
    2: "Для действия {0} нет заданных предметов",
}

base_translates = {
    1: "Ничего не делал",
}

histories = {
    "0|": r'\/',
    '1|': SELF_PERSON_NAME,
    '2|': 'Поел',
    '3|': 'Попил',
    '4|': SELECT_ITEM,
    '5|': 'Принял',
    '6|': 'Работал',
    '7|': 'Отдыхал',
    '8|': 'Помылся',
    '9|': 'Ничего не делал',
}

actions = {
    'hungrr': {
        'name': 'Поесть',
    },
    'thisrr': {
        'name': 'Попить',
    },
    'hlff': {
        'name': 'Лечиться',
    },
    'wrk': {
        'name': 'Работать',
    },
    'rst': {
        'name': 'Отдыхать',
    },
    'hgn': {
        'name': 'Помыться',
    }
}
