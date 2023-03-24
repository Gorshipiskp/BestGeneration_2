from codes import *

foods = {
    'drinks': {
        'Coca-Cola': {
            PRICE: 60,
            REFILLABITILITY: {
                'thirst': 10,
            },
            EXPENDITURE: {
                "health": 0.00025,
            }
        },
        'Juice': {
            PRICE: 120,
            REFILLABITILITY: {
                'thirst': 7,
            },
            EXPENDITURE: {
                "health": 0.00005,
            }
        },
    },
    'food': {
        'Ramen': {
            PRICE: 20,
            REFILLABITILITY: {
                'hungry': 13,
            },
            EXPENDITURE: {
                "health": 0.0002,
            }
        },
        'Snickers': {
            PRICE: 35,
            REFILLABITILITY: {
                'hungry': 5,
            },
            EXPENDITURE: {
                "health": 0.00005,
            }
        },
    },
}

medical = {
    'Ascorbic acid': {
        PRICE: 10,
        REFILLABITILITY: {
            'hungry': 1,
            'health': 0.1,
        },
        EXPENDITURE: {}
    },
    'Painkillers': {
        PRICE: 535,
        REFILLABITILITY: {
            'health': 0.35,
        },
        EXPENDITURE: {}
    },
    'Antibiotics': {
        PRICE: 380,
        REFILLABITILITY: {
            'health': 0.95,
        },
        EXPENDITURE: {}
    },
}

jobs = {
    'Freelance': {
        PRICE: 0,
        REFILLABITILITY: {
            'money': 15,
        },
        EXPENDITURE: {
            'health': 0.001
        }
    },
    'Gardener': {
        PRICE: 0,
        REFILLABITILITY: {
            'money': 35,
            'health': 0.05,
        },
        EXPENDITURE: {}
    },
    'Miner': {
        PRICE: 0,
        REFILLABITILITY: {
            'money': 125,
            'health': 0.15,
        },
        EXPENDITURE: {}
    },
}

rests = {
    'Park': {
        PRICE: 100,
        REFILLABITILITY: {
            'rest': 2,
            'health': 0.1,
        },
        EXPENDITURE: {}
    },
    'Attractions': {
        PRICE: 1500,
        REFILLABITILITY: {
            'rest': 5,
        },
        EXPENDITURE: {}
    },
    'Play Computer Games': {
        PRICE: 0,
        REFILLABITILITY: {
            'rest': 3.5,
        },
        EXPENDITURE: {
            'health': 0.1,
        }
    },
}

hygiene = {
    'Take a Shower': {
        PRICE: 50,
        REFILLABITILITY: {
            'hygiene': 60,
            'health': 0.0175,
        },
        EXPENDITURE: {}
    },
    'Hot Bathtub': {
        PRICE: 150,
        REFILLABITILITY: {
            'hygiene': 80,
            'health': 0.03,
        },
        EXPENDITURE: {}
    },
}
