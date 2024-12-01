import os
from datetime import datetime

year = datetime.now().year
day = datetime.now().day

if not os.path.exists(f"{year}"):
    os.mkdir(f"{year}")

if not os.path.exists(f"{year}/{day}"):
    os.mkdir(f"{year}/{day}")

if not os.path.exists(f"{year}/{day}/input.txt"):
    open(f"{year}/{day}/input.txt", "w").close()

if not os.path.exists(f"{year}/{day}/input_test.txt"):
    open(f"{year}/{day}/input_test.txt", "w").close()

if not os.path.exists(f"{year}/{day}/part_1.py"):
    open(f"{year}/{day}/part_1.py", "w").close()

if not os.path.exists(f"{year}/{day}/part_2.py"):
    open(f"{year}/{day}/part_2.py", "w").close()
