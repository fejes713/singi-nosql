import mysql.connector
import datatypes

current_connection = None
current_cursor = None


def connection(host, user, password):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        global current_connection
        current_connection = mydb
        global current_cursor
        current_cursor = current_connection.cursor()
        return mydb
    except mysql.connector.Error as err:
        raise


def show_databases():
    current_cursor.execute("SHOW DATABASES")
    return current_cursor


def show_tables(database_name):
    current_cursor.execute("SHOW TABLES FROM {}".format(database_name))
    return current_cursor


def create_database(database_name):
    current_cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {}".format(database_name))


def use_database(database_name):
    current_cursor.execute("USE {}".format(database_name))


def show_table(database_name, table_name):
    use_database(database_name)
    current_cursor.execute("SELECT * FROM {}".format(table_name))
    return current_cursor.fetchall()


def show_columns(database_name, table_name):
    use_database(database_name)
    current_cursor.execute("SHOW COLUMNS from {}".format(table_name))
    return current_cursor


def drop_database(database_name):
    current_cursor.execute("DROP DATABASE IF EXISTS {}".format(database_name))


def delete(database_name, table_name, columns):
    use_database(database_name)
    sql = "DELETE FROM "+table_name+" WHERE "
    table_columns = [column for column in show_columns(
        database_name, table_name)]
    for index, column in enumerate(columns):
        if index > 0 and index < len(columns):
            sql += " AND "
        sql += table_columns[index][0]+" = %s"
    val = tuple(columns)
    current_cursor.execute(sql, val)
    current_connection.commit()


def insert(database_name, table_name, columns, values):
    use_database(database_name)
    sql = "INSERT INTO " + table_name + "("  # (name, address) VALUES (%s, %s)"
    first = False
    for index, column in enumerate(columns):
        if values[index].strip() == "":
            continue
        if first:
            sql += ", "
        sql += column
        first = True
    sql += ") VALUES ("
    first = False
    for index, v in enumerate(values):
        if v.strip() == "":
            continue
        if first:
            sql += ", "
        sql += "%s"
        first = True
    sql += ")"
    values = tuple([v for v in values if v != ""])
    types = [column for column in show_columns(database_name, table_name)]
    values = datatypes.sql_to_python(values, types)

    current_cursor.execute(sql, values)
    current_connection.commit()


def update(database_name, table_name, columns, values):
    use_database(database_name)
    sql = "UPDATE " + table_name + " SET "
    sql_values = []
    for index, column in enumerate(columns):
        if index > 0 and index < len(columns):
            sql += ", "
        sql += column + " = " + "%s"
        sql_values.append(str(values[index]))
    sql += " WHERE "
    columns_data = [column for column in show_columns(
        database_name, table_name)]
    first = False
    for index, column in enumerate(columns_data):
        if column[3] == "PRI":
            if first and index > 0 and index < len(columns_data):
                sql += ", "
            sql += columns[index] + " = " + "%s"
            sql_values.append(str(values[index]))
            first = True
    current_cursor.execute(sql, sql_values)
    current_connection.commit()


def search(database_name, table_name, columns, values):
    use_database(database_name)
    sql = "SELECT * FROM " + table_name + " WHERE "
    sql_values = []
    for index, column in enumerate(columns):
        if values[index].strip() == "":
            continue
        if index > 0 and index < len(columns):
            sql += " AND "
        sql += column + " = " + "%s"
        sql_values.append(str(values[index]))
    current_cursor.execute(sql, sql_values)
    return current_cursor

def search_partial(database_name, table_name, columns, values, select_columns):
    use_database(database_name)
    sql = "SELECT "
    if len(select_columns)>0:
        for column in select_columns:
            sql += column + ", "
        sql = sql[:-2]
    else:
        sql += "*"
    sql += " FROM " + table_name + " WHERE "
    sql_values = []
    for index, column in enumerate(columns):
        if values[index].strip() == "":
            continue
        if index > 0 and index < len(columns):
            sql += " AND "
        sql += column + " = " + "%s"
        sql_values.append(str(values[index]))
    current_cursor.execute(sql, sql_values)
    return current_cursor

def show_partial_table(database_name, table_name, columns):
    use_database(database_name)
    sql = "SELECT "
    for column in columns:
        sql += column + ", "
    sql = sql[:-2]
    sql += " FROM {}".format(table_name)
    current_cursor.execute(sql)
    return current_cursor.fetchall()