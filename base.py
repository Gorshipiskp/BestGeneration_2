from imports import *


class Error:
    def __init__(self, error_id: int):
        self.id = error_id

    def get_text(self, *add_ons, format_str=True):
        if format_str:
            return lang.errors[self.id].format(*add_ons)
        else:
            return lang.errors[self.id]

    def get_type(self):
        return errors.errors[self.id]['type']

    def get_info(self):
        return errors.errors[self.id]['type']

    def get_color(self):
        return errors.errors_colors[self.get_type()]

    def print(self, *add_ons):
        print(self.get_color().format(f"\n{self.get_text(*add_ons)}\n"))


#  Class of Database
class Database:

    def __init__(self, name: str = config.db_name, extension: str = config.db_extension, create: bool = True,
                 force_create: bool = False) -> None:
        self.name = name
        self.full_name = f"{name}.{extension}"
        self.connect = sqlite3.connect(self.full_name)
        self.cursor = self.connect.cursor()

        if create:
            self.create(force=force_create)

    # Returns name of DB (just name or name with extension)
    def get_name(self, full: bool = True) -> str:
        if full:
            return self.full_name
        else:
            return self.name

    # Checking if DB already exists
    def is_exists(self):
        return os.path.exists(self.full_name)

    # Returns length of needed table
    def get_length(self, table: str):
        return list(sqlite3.connect(self.full_name).cursor().execute(f"SELECT COUNT(*) FROM {table}"))[0][0]

    # Creating a DB
    def create(self, force: bool = False) -> None:
        # Force creating a DB even if it already exists
        if force:
            open(self.full_name, 'w+')
        # Creating a DB if it doesn't exist (checks if DB already exists)
        else:
            if not self.is_exists():
                open(self.full_name, 'w+')

    # Creating table in DB
    def create_table(self, name: str, columns: dict, force: bool = False) -> None:
        str_colums = list(f'{name} {" ".join(params[PARAMS])}' for name, params in columns.items())
        if force:
            self.cursor.execute(f"DROP TABLE IF EXISTS {name}")
            self.cursor.execute(f"CREATE TABLE {name}({','.join(str_colums)})")
        else:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name}({','.join(str_colums)})")

    # Deleting table in DB
    def delete_table(self, name: str, check=True) -> None:
        if check:
            self.cursor.execute(f"DROP TABLE IF EXISTS {name}")
        else:
            self.cursor.execute(f"DROP TABLE {name}")

    # Insert something into table
    def insert(self, table: str, inserted: dict) -> None:
        self.cursor.execute(
            f"INSERT INTO {table}({','.join(inserted.keys())}) VALUES ({','.join('?' * len(inserted))})",
            tuple(inserted.values()))

    # Insert much something into table
    def insert_many(self, table: str, columns: tuple, inserted: tuple) -> None:
        self.cursor.executemany(f"INSERT INTO {table}({','.join(columns)}) VALUES ({','.join('?' * len(inserted[0]))})",
                                inserted)

    # Update something in table
    def update(self, table: str, updated: tuple, conditions: bool = True) -> None:
        if conditions:
            self.cursor.execute(f"UPDATE {table} SET {updated[0]} = ? WHERE {updated[2]} = ?",
                                (updated[1], updated[3]))
        else:
            self.cursor.execute(f"UPDATE {table} SET {updated[0]} = ?", updated[1:len(updated)])

    # Update much something in table
    def update_many(self, table: str, values: tuple, inserted: tuple) -> None:
        self.cursor.executemany(f"UPDATE {table} SET {values[0]} = ? WHERE {values[1]} = ?", inserted)

    # Select something from table
    def select(self, table: str, selectable: str, src: str = None, value: str = None, conditions: bool = True) -> tuple:
        if conditions:
            return tuple(self.cursor.execute(f'SELECT {selectable} FROM {table} WHERE {src} = ?', (value,)))[0]
        else:
            return tuple(self.cursor.execute(f'SELECT {selectable} FROM {table}'))

    # Delete something from table
    def delete(self, table: str, src: str, value: str) -> None:
        self.cursor.execute(f'DELETE FROM {table} WHERE {src} = ?', (value,))

    # Delete much something from table
    def delete_many(self, table: str, src: str, values: tuple) -> None:
        self.cursor.executemany(f'DELETE FROM {table} WHERE {src} = ?', tuple(zip(values)))

    # Commit all changes
    def commit(self) -> None:
        self.connect.commit()
        self.connect = sqlite3.connect(self.full_name)
        self.cursor = self.connect.cursor()


class Utilities:

    def __init__(self):
        pass

    if config.history_coding:
        @staticmethod
        def time_decode(time_d: str, table_f: dict = None):
            if table_f is None:
                table_f = numbers_24

            for key, val in table_f.items():
                time_d = time_d.replace(val, str(key))
            return time_d

    @staticmethod
    def is_near_number(number: int | float, rang: tuple[int | float, int | float]):
        return rang[0] <= number <= rang[1]

    @staticmethod
    def add_to_dict(blacklist: dict, key, addable) -> dict:
        try:
            blacklist[key].append(addable)
        except KeyError:
            blacklist.update({key: [addable]})
        return blacklist

    @staticmethod
    def zeros_start(*number: int or str, num_num: int = 2) -> str:
        strw = ''.join(str(i) for i in number[::-1])
        return f"{'0' * (num_num - len(strw))}{strw}"

    if config.history_coding:
        def decode_full(self, end_f: str | list) -> dict | str:
            if type(end_f) is list:
                return dict((self.decode_full(i), i) for i in end_f)
            else:
                return self.time_decode(time_codes2[int(self.time_decode(end_f))])

    if config.history and config.history_coding:
        @staticmethod
        def decode_history(per_name: str, hst: str) -> list:
            for code, decode in list(lang.histories.items())[::-1]:
                if decode == SELF_PERSON_NAME:
                    hst = hst.replace(code, per_name)
                else:
                    hst = hst.replace(code, decode)
            for time_f, time_code in all_time_codes.items():
                hst = hst.replace(time_code, time_f)
            return hst.split(lang.histories["0|"])[0:-1]

    @staticmethod
    def get_from_dict(dict_f: dict, key: str, on_error=KeyError):
        try:
            return dict_f[key]
        except KeyError:
            return on_error

    @staticmethod
    def get_spec_by_id(specs: dict, spec_id: int) -> list:
        return list(specs.keys())[spec_id]

    @staticmethod
    def get_dict_from_specs(specs: tuple | list, specs_id: dict) -> dict:
        return dict(zip(specs_id, specs))


class Generation:

    def __init__(self, db_m: Database, num_days: int = config.count_days, table: str = config.base_table,
                 specs: dict = config.base_parameters, specs_ids: dict = config.base_parameters_ids) -> None:
        self.days = num_days
        self.db = db_m
        self.table = table
        self.specs_ids = specs_ids
        self.specs = specs

    @staticmethod
    def random_spawn(parameters: dict, id_human: int = -1) -> tuple:
        human = []
        for name, settings in parameters.items():
            key = Utilities().get_from_dict(settings, KEY)
            default = Utilities().get_from_dict(settings, DEFAULT)
            condition = Utilities().get_from_dict(settings, CONDITION)

            if condition != KeyError:
                cond_comp = condition[0](human, *condition[1])
            else:
                cond_comp = -1

            if key != KeyError and default != KeyError:
                Error(1).print(name, config.base_table)

            if key != KeyError:
                if key == PRIMARY_KEY:
                    human.append(id_human)
                else:
                    if cond_comp == -1:
                        human.append(key[0](*key[1]))
                    else:
                        human.append(key[cond_comp][0](*key[cond_comp][1]))
            elif default != KeyError:
                human.append(default)
        return tuple(human)

    def first_spawn(self) -> None:
        self.db.insert_many(config.base_table, tuple(config.base_parameters.keys()),
                            tuple(self.random_spawn(config.base_parameters, id_human) for id_human in
                                  range(1, config.start_count + 1)))
        self.db.commit()

    @staticmethod
    def can_afford(pers: dict, price: int | float):
        if pers[MONEY] > price:
            return True
        return False

    @staticmethod
    def get_time_stamp(hour_f: int):
        if config.history_coding:
            return all_time_codes[
                f"{Utilities().zeros_start(hour_f, num_num=2)}:{Utilities().zeros_start(random.randint(5, 55))}"]
        else:
            return f"{Utilities().zeros_start(hour_f, num_num=2)}:{Utilities().zeros_start(random.randint(5, 55))}"

    if config.history:
        def get_history_stamp(self, act_history: str, hour_f: int, per_name: str):
            if config.history_coding:
                return f"0|{self.get_time_stamp(hour_f)} {act_history}"
            else:
                return f"""{self.get_time_stamp(hour_f)} {' '.join(tuple(lang.histories[i].replace(
                    SELF_PERSON_NAME, per_name) for i in act_history.split(' ')))}. """

    def do_action(self, specs_f: dict, hour_f: int, item_f_f: dict, act: dict):
        specs_f[MONEY] -= item_f_f[PRICE]
        for name, val in item_f_f[REFILLABITILITY].items():
            specs_f[name] = round(specs_f[name] + val, config.round_accuracy)
        for name, val in item_f_f[EXPENDITURE].items():
            specs_f[name] = round(specs_f[name] - val, config.round_accuracy)
        if config.history:
            specs_f[HISTORY] += self.get_history_stamp(act[1][HISTORY], hour_f, specs_f[NAME])
        return specs_f

    @staticmethod
    def select_action(actions_f: dict, specs_vals_f, blacklist: dict, key_f: str = False):
        blacklisted_acts = tuple(blacklist.keys())
        if key_f:
            sel = random.choice(tuple((act_name, act_inf) for act_name, act_inf in actions_f.items() if
                                      act_inf[KEY] == key_f and act_inf[KEY] not in blacklisted_acts))
            return sel
        else:
            need_need = min(specs_vals_f, key=lambda x: specs_vals_f[x])
            try:
                return random.choice(tuple((act_name, act_inf) for act_name, act_inf in actions_f.items() if
                                           act_inf[KEY] == need_need and act_inf[KEY] not in blacklisted_acts))
            except IndexError:
                Error(2).print(need_need)

    def do_specify_action(self, specs_f, blacklist_f: dict, selected_act_f, specs_vals_f: dict, hour_f_f: int,
                          act_name: str):
        if len(tuple(blacklist_f.values())[0]) == len(tuple(selected_act_f[1][SELECT][1][0].keys())):
            for_act = self.select_action(actions, specs_vals_f, blacklist_f, act_name)
            selec_f = for_act[1][SELECT]
            items_f = self.get_items(selec_f)
            selected_item_f_f = selec_f[1][0][selec_f[0](tuple(x for x in items_f))]

            return self.do_action(specs_f, hour_f_f, selected_item_f_f, for_act)
        return specs_f

    @staticmethod
    def get_items(selec_f_f):
        return tuple(tuple(x.keys()) for x in selec_f_f[1])[0]

    @staticmethod
    def select_item(selec_f, items_f, blacklist_f, selected_act_f):
        try:
            selected_item = selec_f[0](tuple(x for x in items_f if x not in blacklist_f[selected_act_f[0]]))
        except KeyError:
            selected_item = selec_f[0](tuple(x for x in items_f))
        except IndexError:
            return IndexError
        return selected_item

    def do_new_action(self, specs: dict, hour_f: int, specs_vals: dict, day_id, blacklist: dict = None):
        if blacklist is None:
            blacklist = {}

        selected_act = self.select_action(actions, specs_vals, blacklist)
        selec = selected_act[1][SELECT]

        items = self.get_items(selec)
        selected_item = self.select_item(selec, items, blacklist, selected_act)

        if selected_item is IndexError:
            if random.choice(list(range(4))) > 0:
                specs = self.do_specify_action(specs, blacklist, selected_act, specs_vals, hour_f, MONEY)
                return specs
            else:
                if config.history:
                    specs[HISTORY] += self.get_history_stamp("1| 9|", hour_f, specs[NAME])
                return specs

        item = selec[1][0][selected_item]
        conds = Utilities().get_from_dict(selected_act[1], CONDITION, False)

        for need, val in item[REFILLABITILITY].items():
            if specs[need] + val > config.base_parameters[need][MAX_RSTR] + config.max_deviation:
                blacklist = Utilities().add_to_dict(blacklist, selected_act[0], selected_item)
                specs = self.do_new_action(specs, hour_f, specs_vals, day_id, blacklist)
                return specs

        if conds:
            if conds[0](specs, *conds[1]):
                if self.can_afford(specs, item[PRICE]):
                    specs = self.do_action(specs, hour_f, item, selected_act)
                else:
                    blacklist = Utilities().add_to_dict(blacklist, selected_act[0], selected_item)
                    specs = self.do_specify_action(specs, blacklist, selected_act, specs_vals, hour_f, MONEY)
            else:
                blacklist = Utilities().add_to_dict(blacklist, selected_act[0], selected_item)
                specs = self.do_new_action(specs, hour_f, specs_vals, day_id, blacklist)
        else:
            if self.can_afford(specs, item[PRICE]):
                specs = self.do_action(specs, hour_f, item, selected_act)
            else:
                blacklist = Utilities().add_to_dict(blacklist, selected_act[0], selected_item)
                if len(tuple(blacklist.values())[0]) == len(tuple(selected_act[1][SELECT][1][0].keys())):
                    specs = self.do_specify_action(specs, blacklist, selected_act, specs_vals, hour_f, MONEY)
                else:
                    specs = self.do_new_action(specs, hour_f, specs_vals, day_id, blacklist)
        return specs

    def generate_hour(self, specs: dict, hour_f: int, day_id, utils: Utilities = Utilities()) -> dict:
        specs_vals = {}
        for name in specs:
            exp_hour = utils.get_from_dict(self.specs[name], EXPENDITURE, on_error="False")
            if exp_hour != "False":
                try:
                    specs_vals.update({name: specs[name] / self.specs[name]['priority']})
                except KeyError:
                    pass
                specs[name] = round(specs[name] - exp_hour, config.round_accuracy)

        specs = self.do_new_action(specs, hour_f, specs_vals, day_id)
        return specs

    def generate_day(self, day_id: int, human: dict | list) -> None:
        utils = Utilities()
        specs_def = utils.get_dict_from_specs(self.db.select(self.table, "*", 'id', human[0]), self.specs_ids)
        specs = utils.get_dict_from_specs(self.db.select(self.table, "*", 'id', human[0]), self.specs_ids)

        for hour_f in range(24):
            specs = self.generate_hour(specs, hour_f, day_id)

        for i in specs:
            exp_day = utils.get_from_dict(self.specs[i], EXPENDITURE_DAY, on_error="False")
            if exp_day != "False":
                specs[i] = round(specs[i] - exp_day, config.round_accuracy)

        for edit in tuple((name, spe) for name, spe in specs.items() if specs[name] != specs_def[name]):
            self.db.update(self.table, (*edit, tuple(specs.keys())[0], tuple(specs.values())[0]))

    def start_generation(self) -> None:
        try:
            for day in range(1, self.days + 1):
                for human in self.db.select(self.table, '*', conditions=False):
                    self.generate_day(day, human)
                if config.show_loading_progress:
                    print(round(day / self.days * 100, config.round_accuracy), '%')
                self.db.commit()
        except KeyboardInterrupt:
            self.db.commit()


class Action:
    def __init__(self, ac_id: int):
        self.id = ac_id
        self.action = 2

    def get_id(self):
        return self.id

    def get_name(self):
        return lang.actions[self.id]["name"]


for act_id, infs in actions.items():
    infs.update({NAME: Action(act_id).get_name()})

if config.history_coding:
    time_codes, numbers_24, all_time_codes = {}, {
        '1': '[',
        '2': ']',
        '3': '{',
        '4': '}',
        '5': '>',
        '6': '<',
        '7': '/',
        '8': '?',
        '9': '.',
        '10': 'a',
        '11': 'A',
        '12': 'b',
        '13': 'B',
        '14': 'c',
        '15': 'C',
        '16': 'd',
        '17': 'D',
        '18': 'e',
        '19': 'E',
        '20': 'f',
        '21': 'F',
        '22': 'g',
        '23': 'G',
        '24': 'h',
        '25': 'H',
        '26': 'i',
        '27': 'I',
        '28': 'j',
        '29': 'J',
        '30': 'k',
        '31': 'K',
        '32': 'l',
        '33': 'L',
        '34': 'm',
        '35': 'M',
        '36': 'n',
        '37': 'N',
        '38': 'o',
        '39': 'O',
        '40': 'p',
        '41': 'P',
        '42': 'q',
        '43': 'Q',
        '44': 'r',
        '45': 'R',
        '46': 's',
        '47': 'S',
        '48': 't',
        '49': 'T',
        '50': 'u',
        '51': 'U',
        '52': 'v',
        '53': 'V',
        '54': 'w',
        '55': 'W',
        '56': 'x',
        '57': 'X',
        '58': 'y',
        '59': 'Y',
        '0': 'Z',
        '01': ')',
        '02': '(',
        '03': '+',
        '04': '=',
        '05': '-',
        '06': '_',
        '07': '*',
        '08': '/',
        '09': '%',
        '00': ';',
        ":": 'z',
    }, {}

    for hour in range(0, 24):
        for minute in range(0, 60):
            nums = ''.join(
                numbers_24[i] for i in list(f"{Utilities().zeros_start(hour)}:{Utilities().zeros_start(minute)}"))
            time_codes.update({Utilities().time_decode(nums): nums})

    time_codes2 = dict((time_id, time_val) for time_id, time_val in enumerate(time_codes.values()))

    for time_id, time_val in time_codes2.items():
        rd = str(Utilities().zeros_start(time_id, num_num=4))
        rd_dec = f"{numbers_24[rd[0:2]]}{numbers_24[rd[2:3]]}{numbers_24[rd[3:4]]}"
        all_time_codes.update({Utilities().time_decode(time_val): rd_dec})
