from base import *

start = time.time()
db = Database()
gen = Generation(db, table=config.base_table, num_days=config.count_days)

db.create_table(config.base_table, config.base_parameters, force=config.restart)

start2 = time.time()

if config.restart:
    gen.first_spawn()

print(f"ALL GENERATED {time.time() - start2} SEC")

gen.start_generation()

print(f"{time.time() - start} Secs - Total")
print(f"{(time.time() - start) / config.count_days:.4f} Sec/Day")
print(f"{(time.time() - start) / config.count_days / 24:.4f} Sec/Hour")
print(f"{(time.time() - start) / config.start_count} Sec/Hum")
print(f"{(time.time() - start) / config.count_days  / config.start_count} Sec/Hum (Day)")

input()
