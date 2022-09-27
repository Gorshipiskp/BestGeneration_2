from imports import *


class Database:
    def __init__(self, name: str = config.db_name, extesion: str = config.db_extension, create: bool = True,
                 force_create: bool = False) -> None:
        self.name = name
        self.full_name = f"{name}.{extesion}"

        if create:
            self.create(check=not force_create)

    # Returns name of DB (just name or name with extension)
    def get_name(self, full: bool = True) -> str:
        if full:
            return self.full_name
        else:
            return self.name

    # Checking if DB already exists
    def is_exists(self):
        return os.path.exists(self.full_name)

    # Creating a DB
    def create(self, check: bool = False) -> None:

        # Creating a DB if it doesn't exist (checks if DB already exists)
        if check:
            if self.is_exists():
                return
            else:
                open(self.full_name, 'w+')
        # Force creating a DB even if it already exists
        else:
            open(self.full_name, 'w+')

    # Creating table in DB
    def create_table(self, name: str, columns: dict, force: bool = False) -> None:
        str_colums = list(f'{name} {" ".join(params)}' for name, params in columns.items())
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            if force:
                cursor.execute(f"CREATE TABLE {name}")
            else:
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {name}({','.join(str_colums)})")

    # Insert something into table
    def insert(self, table: str, inserted: tuple) -> None:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {table} VALUES ({','.join('?' * len(inserted))})", inserted)

    # Insert much something into table
    def insert_many(self, table: str, inserted: tuple) -> None:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            cursor.executemany(f"INSERT INTO {table} VALUES ({','.join('?' * len(inserted[0]))})", inserted)

    # Update something in table
    def update(self, table: str, inserted: tuple, conditions: bool = True) -> None:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            if conditions:
                cursor.execute(f"UPDATE {table} SET {inserted[0]} = ? WHERE {inserted[2]} = ?", (inserted[1], inserted[3]))
            else:
                cursor.execute(f"UPDATE {table} SET {inserted[0]} = ?", inserted[1:len(inserted)])

    # Update much something in table
    def update_many(self, table: str, values: tuple, inserted: tuple) -> None:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            cursor.executemany(f"UPDATE {table} SET {values[0]} = ? WHERE {values[1]} = ?", inserted)

    # Select something from table
    def select(self, table: str, selectable: str, src: str = None, value: str = None, conditions: bool = True) -> tuple:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            if conditions:
                return tuple(cursor.execute(f'SELECT {selectable} FROM {table} WHERE {src} = ?', (value, )))[0]
            else:
                return tuple(cursor.execute(f'SELECT {selectable} FROM {table}'))

    # Delete something from table
    def delete(self, table: str, src: str, value: str) -> None:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {table} WHERE {src} = ?', (value, ))

    # Delete much something from table
    def delete_many(self, table: str, src: str, values: tuple) -> None:
        with sqlite3.connect(self.full_name) as conn:
            cursor = conn.cursor()
            cursor.executemany(f'DELETE FROM {table} WHERE {src} = ?', tuple(zip(values)))
