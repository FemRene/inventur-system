import random
import sqlite3
import string

db = "storage.sql"


def getAllRowsAsList() -> list['']:
    """
    :return:
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM entrys")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3]))
    conn.commit()
    conn.close()
    return data


def getAllRowsByTypeAsList(param1: str) -> list['']:
    """
    :param param1:
    :return:
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM entrys WHERE type IS '{param1}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3]))
    conn.commit()
    conn.close()
    return data


def deleteRowByID(id):
    """
    :param id:
    :return:
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"DELETE FROM entrys WHERE ID IS {id}")
    conn.commit()
    conn.close()


def insertNewRow(tag, type, raum):
    """
    :param tag:
    :param type:
    :param raum:
    :return:
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"INSERT INTO entrys (service_tag, type, raum) VALUES ('{tag}', '{type}', '{raum}');")
    conn.commit()
    conn.close()


def updateRow(id, tag, type, raum):
    """

    :param id:
    :param tag:
    :param type:
    :param raum:
    :return:
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"UPDATE entrys SET service_tag = '{tag}', type = '{type}', raum = '{raum}' WHERE ID IS {id}")
    conn.commit()
    conn.close()


def getAllTypesAsList() -> list['']:
    """

    :return:
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM types")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1]))
    conn.commit()
    conn.close()
    print(data)
    return data


def getAllTypesForBoxAsList() -> list['']:
    """
    Get all Types as a List
    :return: list of all Types
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM types")
    records = c.fetchall()
    for record in records:
        data.append((record[0]))
    conn.commit()
    conn.close()
    print(data)
    return data


def getTypesByCategory(category: str) -> list['']:
    """
    NOT YET USED
    :param category:
    :return:
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM types WHERE parent IS '{category}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0]))
    conn.commit()
    conn.close()
    return data


def getAllUsersAsList() -> list['']:
    """
    Get all registered Users
    :return: list of all Users
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4]))
    conn.commit()
    conn.close()
    return data


def getUserByName(name) -> list['']:
    """
    Get the table row of the User by his Name
    :param name: Name of the User
    :return: list of User-Data
    """
    data = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE name IS '{name}'")
    records = c.fetchall()
    for record in records:
        data.append((record[0], record[1], record[2], record[3], record[4]))
    conn.commit()
    conn.close()
    return data


def deleteUserByID(id):
    """
    Deletes a User by its ID
    :param id: ID of the User
    :return: nothing
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"DELETE FROM users WHERE ID IS {id}")
    conn.commit()
    conn.close()


def insertUser(role, name, password):
    """
    Adds a new User
    :param role: Role of the User (E.g. nutzer, administrator, gast)
    :param name: Name of the User
    :param password: Password for the new User (empty for random password)
    :return: nothing
    """
    if not password:
        password = __generate_random_string(10)
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"INSERT INTO users (role, name, password) VALUES ('{role}', '{name}', '{password}');")
    conn.commit()
    conn.close()


def __generate_random_string(length=10):
    """
    Generates a Random String
    :param length: characters Length of the return (default is 10)
    :return: random String)
    """
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
