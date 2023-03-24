from codes import *


errors = {
    1: {
        "type": CRITICAL,
    },
    2: {
        "type": CRITICAL,
    },
}

errors_colors = {
    CRITICAL: '\033[31m\033[1m{}\033[0m\033[22m',
    ATTENTION: '\033[33m\033[1m{}\033[0m\033[22m',
    WARNING: '\033[33m\033[1m{}\033[0m\033[22m',
}
