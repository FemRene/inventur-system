import sqlite3


def getAllRowsAsList() -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM entrys")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3]))
    conn.commit()
    conn.close()
    return data


def getAllRowsByTypeAsList(type: str) -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"SELECT * FROM entrys WHERE type IS '{type}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3]))
    conn.commit()
    conn.close()
    return data


def deleteRowByID(id):
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"DELETE FROM entrys WHERE ID IS {id}")
    conn.commit()
    conn.close()


def insertNewRow(tag, type, raum):
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"INSERT INTO entrys (service_tag, type, raum) VALUES ('{tag}', '{type}', '{raum}');")
    conn.commit()
    conn.close()


def updateRow(id, tag, type, raum):
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"UPDATE entrys SET service_tag = '{tag}', type = '{type}', raum = '{raum}' WHERE ID IS {id}")
    conn.commit()
    conn.close()


def getAllTypesAsList() -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM types")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1]))
    conn.commit()
    conn.close()
    return data


def getAllTypesForBoxAsList() -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM types")
    records = c.fetchall()
    for record in records:
        data.append((record[0]))
    conn.commit()
    conn.close()
    return data


def getTypesByCategory(category: str) -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"SELECT * FROM types WHERE parent IS '{category}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0]))
    conn.commit()
    conn.close()
    return data


def getAllUsersAsList() -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4]))
    conn.commit()
    conn.close()
    return data


def getUserByName(name) -> list[()]:
    data = []
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE name IS '{name}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4]))
    conn.commit()
    conn.close()
    return data


def deleteUserByID(id):
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"DELETE FROM users WHERE ID IS {id}")
    conn.commit()
    conn.close()


def insertUser(role, name, password):
    conn = sqlite3.connect("storage.sql")
    c = conn.cursor()
    c.execute(f"INSERT INTO users (role, name, password) VALUES ('{role}', '{name}', '{password}');")
    conn.commit()
    conn.close()