import sqlite3 as sql

print('1 - Запись\n2 - Чтение')
choice = int(input("> "))
con = sql.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `test` (`name` STRING, `surname` STRING)") 
    con.commit()

    if choice == 1:
        name = input("Name > ")
        surname = input("surname > ")
        cur.execute(f"INSERT INTO `test` VALUES ('{name}', '{surname}')")# запись данных

    elif choice == 2:
        cur.execute("SELECT * FROM `test`")
        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[1])

    else:
        print("Ошибка.")

    con.commit()
    cur.close()