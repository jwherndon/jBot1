import mysql.connector
from mysql.connector import Error
import datetime
import logging


class Storage:

    database_connection = None

    def __init__(self):
        self.create_connection('localhost', 'root', '4bot!tob4', 'discordbotstorage')

    def create_connection(self, host_name, user_name, user_password, db_name):
        try:
            self.database_connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            logging.debug(f"Connection to mysql://{host_name}/{db_name} successful")
        except Error as e:
            logging.error(f"The error '{e}' occurred")
            exit(-1)

    def create_new_player(self, name):
        if not self.player_exists(name):
            current_date = datetime.datetime.now(tz=datetime.timezone.utc)
            cmd = f"INSERT INTO players (name, created) VALUES ('{name}', '{current_date}');"
            logging.debug(cmd)
            try:
                cursor = self.database_connection.cursor()
                cursor.execute(cmd)
                self.database_connection.commit()
                logging.debug(f"Player {name} created")
                return True
            except Error as e:
                logging.error(f"The error '{e}' occurred")
                raise e
        else:
            logging.debug(f"Player {name} already exists")
            return False

    def player_exists(self, name):
        cmd = f"SELECT * FROM players WHERE name = '{name}';"
        logging.debug(cmd)
        try:
            results = self.execute_read_query(self.database_connection, cmd)
            logging.debug(results)
            if results:
                logging.debug(f"Player {name} exists")
                return True
            else:
                logging.debug(f"Player {name} does not exist")
                return False
        except Error as e:
            logging.error(f"The error '{e}' occurred")
            return False

    def set_player_last_played(self, name, value):
        datetime.datetime.now(tz=datetime.timezone.utc)
        cmd = f"UPDATE players SET last_played = '{value}' WHERE name = '{name}';"
        logging.debug(cmd)
        try:
            cursor = self.database_connection.cursor()
            cursor.execute(cmd)
            self.database_connection.commit()
            return True
        except Error as e:
            logging.error(f"The error '{e}' occurred")
            return None

    def check_player_credit(self, name, value):
        if self.player_exists(name):
            if self.get_player_currency(name) >= int(value):
                return True
            else:
                return False

    def get_player_currency(self, name):
        if self.player_exists(name):
            cmd = f"SELECT currency FROM players WHERE name = '{name}';"
            logging.debug(cmd)
            try:
                results = self.execute_read_query(self.database_connection, cmd)
                logging.debug(f"Currency of {name} is {results[0][0]}")
                return results[0][0]
            except Error as e:
                logging.error(f"The error '{e}' occurred")
                return None
        else:
            return None

    def set_player_currency(self, name, value):
        if self.player_exists(name):
            cmd = f"UPDATE players SET currency = {value} WHERE name = '{name}';"
            logging.debug(cmd)
            try:
                cursor = self.database_connection.cursor()
                cursor.execute(cmd)
                self.database_connection.commit()
                return True
            except Error as e:
                logging.error(f"The error '{e}' occurred")
                return None
        else:
            return None

    def add_player_currency(self, name, value):
        if self.player_exists(name):
            current_value = self.get_player_currency(name)
            new_value = int(current_value) + int(value)
            self.set_player_currency(name, new_value)
            return new_value
        else:
            return None

    def sub_player_currency(self, name, value):
        if self.player_exists(name):
            current_value = self.get_player_currency(name)
            new_value = int(current_value) - int(value)
            self.set_player_currency(name, new_value)
            return new_value
        else:
            return None

    def get_player_record(self, name):
        if self.player_exists(name):
            cmd = f"SELECT * FROM players WHERE name = '{name}';"
            logging.debug(cmd)
            try:
                results = self.execute_read_query(self.database_connection, cmd)
                logging.debug(results)
                return results
            except Error as e:
                logging.error(f"The error '{e}' occurred")
                return None
        else:
            return None

    @staticmethod
    def execute_read_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            logging.error(f"The error '{e}' occurred")
            return None
