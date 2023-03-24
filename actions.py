import time
import random
from items import *
from codes import *


def older_3(pers):
    if pers['age'] >= 3:
        return True
    return False


actions = {
    'hungrr': {
        KEY: "hungry",
        HISTORY: "1| 2|",
        SELECT: (random.choice, (foods['food'], )),
        CONDITION: (older_3, ()),
    },
    'thisrr': {
        KEY: "thirst",
        HISTORY: "1| 3|",
        SELECT: (random.choice, (foods['drinks'], )),
    },
    'hlff': {
        KEY: "health",
        HISTORY: "1| 5|",
        SELECT: (random.choice, (medical, )),
    },
    'wrk': {
        KEY: "money",
        HISTORY: "1| 6|",
        SELECT: (random.choice, (jobs, )),
    },
    'rst': {
        KEY: "rest",
        HISTORY: "1| 7|",
        SELECT: (random.choice, (rests, )),
    },
    'hgn': {
        KEY: "hygiene",
        HISTORY: "1| 8|",
        SELECT: (random.choice, (hygiene, )),
    }
}
