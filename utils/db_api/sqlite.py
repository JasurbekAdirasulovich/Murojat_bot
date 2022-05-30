import sqlite3
import datetime
date = datetime.datetime.now()
date = date.date()


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id integer primary key autoincrement,
            Username varchar(255),
            UserId int UNIQUE
            );
"""
        self.execute(sql, commit=True)

    def create_table_message(self):
        sql = """
        CREATE TABLE Xabar (
            id integer primary key autoincrement,
            FISH varchar(255),
            tel_raqam varchar(255),
            manzil varchar(255),
            userId int,
            xabar text,
            sana text,
            vaqt varchar(255)
            );
    """
        self.execute(sql, commit=True)


    def create_table_pravila(self):
        sql = """
        CREATE TABLE Qoidalar (
            id integer primary key autoincrement,
            Qoida_uz varchar(500) UNIQUE Null,
            Qoida_en varchar(500) NULL,
            Qoida_ru varchar(500) NULL 
            );
    """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, Username: str, UserId: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(Username, UserId) VALUES(?, ?)
        """
        self.execute(sql, parameters=(Username, UserId), commit=True)

    def add_post(self,FISH: str,tel_raqam: str,manzil: str, userId: int, xabar: str, sana: str, vaqt: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Xabar(FISH, tel_raqam, manzil, userId, xabar, sana, vaqt) VALUES(?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(FISH, tel_raqam, manzil, userId, xabar, sana, vaqt), commit=True)


    def add_pravila(self,Qoida_uz: str, Qoida_en: str, Qoida_ru: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Qoidalar(Qoida_uz, Qoida_en, Qoida_ru) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(Qoida_uz, Qoida_en, Qoida_ru), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_all_post(self):
        sql = """
        SELECT FISH, xabar, sana, vaqt FROM Xabar
        """
        return self.execute(sql, fetchall=True)


    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(UserId) FROM Users;", fetchone=True)

    def count_post(self):
        return self.execute("SELECT COUNT(xabar) FROM Xabar;", fetchone=True)


    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
