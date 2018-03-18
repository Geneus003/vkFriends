import sqlite3

rouletDB = sqlite3.connect("test.db")

cursorTask = rouletDB.execute("SELECT id, name, secs from TASK")

for row in cursorTask:
    print(row[0])
    print(row[1])
    print(row[2])

rouletDB.close()